# DoPad

A simple, lightweight web-based notepad built with Flask and SQLite. DoPad allows you to create and access notes instantly by using any URL path as a unique identifier.

## Features

- URL-based note creation: Simply visit any path (e.g., `/my-note`) to start writing.
- Auto-saving: Your changes are automatically saved as you type.
- Automatic persistence: Notes are stored in a local SQLite database.
- Minimalist interface: Focused on writing without distractions.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DoPad.git
   cd DoPad
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`.

## Usage

- **Home Page**: Visit the root URL to see the welcome message.
- **Create/View Note**: Enter any slug in the URL (e.g., `http://localhost:5000/travel-list`) to open a note page.
- **Editing**: Any changes made in the editor are saved automatically (depending on the frontend implementation).

## Future Roadmap

### API Access (CLI)

Planned support for `curl` to interact with notes directly from the terminal:

- **Fetch a note**:
  ```bash
  curl http://localhost:5000/api/get/my-slug
  ```
- **Update a note**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"content": "new text"}' http://localhost:5000/api/save/my-slug
  ```

### Planned Features

- **Password Protection**: Add optional passcodes to secure specific notes.
- **Markdown Support**: Toggle between a raw editor and a rendered markdown preview.
- **Dark Mode**: A simple preference toggle for better readability at night.
- **Note Expiration**: Set notes to automatically delete after a certain period (e.g., 24 hours, 7 days).
- **Export Options**: Download notes as `.txt` or `.md` files.
- **Search**: Quickly find notes based on their content or slug names.

## License

This project is open-source and available under the GNU General Public License v3.0.
