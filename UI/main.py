
import sys  # We need sys so that we can pass argv to QApplication
import mainWindow1  # This file holds our MainWindow and all design related things
# it also keeps events etc that we defined in Qt Designer
from PyQt5.QtCore import QObject
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, mainWindow1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.currentPlaylist = QMediaPlaylist()
        self.player = QMediaPlayer()
        self.userAction = -1			#0- stopped, 1- playing 2-paused
        self.connect()
        self.player.setVolume(60)
		#Status bar
        self.statusBar().showMessage('Project Recommend')
        self.homeScreen()

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
    def homeScreen(self):
        self.setWindowTitle('Offline Music Recommender')
    def connect(self):
        self.pushButton.clicked.connect(self.playHandler)
        

    def playHandler(self):
        self.userAction = 1
        self.statusBar().showMessage('Playing at Volume %d'%self.player.volume())
        if self.player.state() == QMediaPlayer.StoppedState :
            if self.player.mediaStatus() == QMediaPlayer.NoMedia:
				#self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.currentFile)))
                print(self.currentPlaylist.mediaCount())
                if self.currentPlaylist.mediaCount() == 0:
                    self.openFile()
                if self.currentPlaylist.mediaCount() != 0:
                    self.player.setPlaylist(self.currentPlaylist)
            elif self.player.mediaStatus() == QMediaPlayer.LoadedMedia:
                self.player.play()
            elif self.player.mediaStatus() == QMediaPlayer.BufferedMedia:
                self.player.play()
            elif self.player.state() == QMediaPlayer.PlayingState:
                pass
        elif self.player.state() == QMediaPlayer.PausedState:
                self.player.play()




if __name__ == '__main__':  # if we're running file directly and not importing
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                 # it run the main function
