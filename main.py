import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow) : 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView() 
        self.browser.setUrl(QUrl("https://google.com/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


#NAVBAR

        navbar = QToolBar()
        self.addToolBar(navbar)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        frwrd_btn = QAction('Forward', self)
        frwrd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(frwrd_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com/"))
    
    def navigate_to_url(self):
        url_text = self.url_bar.text()
        self.browser.setUrl(QUrl(url_text))
    
    def update_url(self, t_1):
        self.url_bar.setText(t_1.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Safe Browser')
window = MainWindow()
app.exec_()
