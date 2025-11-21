# Web Browser

A simple and lightweight web browser built with Python using PyQt5 and QtWebEngine.

## Description

This is a desktop web browser application that provides basic web browsing functionality with a clean and intuitive user interface. The browser is built using PyQt5 framework and QtWebEngine for rendering web pages.

## Features

- **URL Navigation**: Navigate to websites by entering URLs in the address bar
- **Smart Search**: Automatically searches Google when you enter search terms instead of URLs
- **Back/Forward Navigation**: Navigate through your browsing history with dedicated buttons
- **Reload Page**: Refresh the current page with a single click
- **Protocol Handling**: Automatically adds "http://" prefix to URLs when needed
- **Default Homepage**: Opens Google as the default homepage

## Requirements

- Python 3.x
- PyQt5
- PyQt5-QtWebEngine

## Installation

1. Clone this repository:
```bash
git clone https://github.com/vprayag2005/web-browser.git
cd web-browser
```

2. Install the required dependencies:
```bash
pip install PyQt5 PyQtWebEngine
```

## Usage

Run the browser by executing the main Python file:

```bash
python main.py
```

### How to Use:
- **Enter a URL**: Type a website address (e.g., `github.com` or `https://github.com`) in the address bar and press Enter or click the "Go" button
- **Search**: Type search terms in the address bar to perform a Google search
- **Navigate Back**: Click the `<` button to go to the previous page
- **Navigate Forward**: Click the `>` button to go to the next page
- **Reload**: Click the `⟳` button to refresh the current page

## Project Structure

```
web-browser/
├── main.py          # Main application file containing the WebBrowser class
└── README.md        # Project documentation
```

## How It Works

The application uses:
- **PyQt5**: For creating the graphical user interface
- **QWebEngineView**: For rendering and displaying web content
- **QLineEdit**: For the URL address bar
- **QPushButton**: For navigation controls

The browser intelligently detects whether user input is a URL or a search query and handles it accordingly.

## License

This project is open source and available for educational purposes.
