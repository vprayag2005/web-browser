from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from urllib.parse import quote_plus

class WebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Web Browser")

        self.layout = QVBoxLayout()
        self.horizondal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.reload_btn = QPushButton("⟳")
        self.reload_btn.setMinimumHeight(30)


        self.horizondal.addWidget(self.back_btn)
        self.horizondal.addWidget(self.forward_btn)
        self.horizondal.addWidget(self.reload_btn)
        self.horizondal.addWidget(self.url_bar)
        self.horizondal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))

        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)

        self.layout.addLayout(self.horizondal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        url = url.strip()
        if not url:
            return
        if "." not in url or url.startswith("localhost"):
            search_url = f"https://www.google.com/search?q={quote_plus(url)}"
            self.url_bar.setText(search_url)
            self.browser.setUrl(QUrl(search_url))
            return
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = WebBrowser()
app.exec_()