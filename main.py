import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MyApp(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MyApp, self).__init__(*args, **kwargs)
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("http://google.com"))
		self.setCentralWidget(self.browser)
		self.showMaximized()

		# Add Navbar
		navabar = QToolBar()
		self.addToolBar(navabar)
		self.url_bar = QLineEdit()

		# Add Actions
		back_btn = QAction('Back', self)
		back_btn.triggered.connect(self.browser.back)
		navabar.addAction(back_btn)

		forward_btn = QAction('Forward', self)
		forward_btn.triggered.connect(self.browser.forward)
		navabar.addAction(forward_btn)

		reload_btn = QAction('Reload', self)
		reload_btn.triggered.connect(self.browser.reload)
		navabar.addAction(reload_btn)

		home_btn = QAction('Home', self)
		home_btn.triggered.connect(self.go_home)
		navabar.addAction(home_btn)

		self.url_bar.returnPressed.connect(self.go_url)
		navabar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url)

	def go_home(self):
		self.browser.setUrl(QUrl("http://google.com"))

	def go_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

	def update_url(self, q):
		self.url_bar.setText(q.toString())

	
def main():
	# creating PyQt5 application
	app = QApplication(sys.argv)

	# setting application name
	app.setApplicationName("Leon Browser")

	# creating a main window object
	window = MyApp()

	# loop
	app.exec_()


if __name__ == '__main__':
	main()
