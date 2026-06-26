from flask import Flask, render_template, request, jsonify
import sqlite3


app = Flask(__name__)

DATABASE = "notes.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            slug TEXT PRIMARY KEY,
            content TEXT DEFAULT ''         
        )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return """
    <h1>DoPad</h1>
    <p>Visit any URL to create a note.</p>
    """


@app.route("/<slug>")
def note(slug):
    conn = get_db()

    note = conn.execute(
        "SELECT * FROM notes WHERE slug = ?",
        (slug,)
    ).fetchone()

    if note is None:
        conn.execute(
            "INSERT INTO notes(slug, content) VALUES (?, ?)",
            (slug, "")
        )
        conn.commit()

        note = conn.execute(
            "SELECT * FROM notes WHERE slug = ?",
            (slug,)
        ).fetchone()
    
    conn.close()

    return render_template(
        "index.html",
        slug = slug,
        content = note["content"]
    )



@app.route("/save/<slug>", methods=["POST"])
def save(slug):
    data = request.get_json()

    conn = get_db()

    conn.execute(
        "UPDATE notes SET content = ? WHERE slug = ?",
        (
            data["content"],
            slug
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success" : True
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)