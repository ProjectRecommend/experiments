# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(705, 600))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("Offline Music Recommender")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ic_main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(705, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 701, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RecommendLocal = QtWidgets.QTableView(self.gridLayoutWidget)
        self.RecommendLocal.setObjectName("RecommendLocal")
        self.gridLayout.addWidget(self.RecommendLocal, 0, 1, 1, 1)
        self.RecommedOnline = QtWidgets.QTableView(self.gridLayoutWidget)
        self.RecommedOnline.setObjectName("RecommedOnline")
        self.gridLayout.addWidget(self.RecommedOnline, 1, 1, 1, 1)
        self.Playlist = QtWidgets.QTableView(self.gridLayoutWidget)
        self.Playlist.setObjectName("Playlist")
        self.gridLayout.addWidget(self.Playlist, 0, 0, 2, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 450, 701, 131))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Timeline = QtWidgets.QHBoxLayout()
        self.Timeline.setObjectName("Timeline")
        self.CurrentTime = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CurrentTime.setFont(font)
        self.CurrentTime.setIndent(2)
        self.CurrentTime.setObjectName("CurrentTime")
        self.Timeline.addWidget(self.CurrentTime)
        self.ProgressBar = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.ProgressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProgressBar.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setTickInterval(0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Timeline.addWidget(self.ProgressBar)
        self.TotalTime = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.TotalTime.setFont(font)
        self.TotalTime.setIndent(2)
        self.TotalTime.setObjectName("TotalTime")
        self.Timeline.addWidget(self.TotalTime)
        self.gridLayout_3.addLayout(self.Timeline, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.SongTitle = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SongTitle.setFont(font)
        self.SongTitle.setIndent(5)
        self.SongTitle.setObjectName("SongTitle")
        self.gridLayout_2.addWidget(self.SongTitle, 0, 0, 1, 1)
        self.SongAlbum = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SongAlbum.setFont(font)
        self.SongAlbum.setIndent(5)
        self.SongAlbum.setObjectName("SongAlbum")
        self.gridLayout_2.addWidget(self.SongAlbum, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        self.SongArtist = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SongArtist.setFont(font)
        self.SongArtist.setIndent(5)
        self.SongArtist.setObjectName("SongArtist")
        self.gridLayout_2.addWidget(self.SongArtist, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Prev = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/ic_skip_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev.setIcon(icon1)
        self.Prev.setIconSize(QtCore.QSize(25, 25))
        self.Prev.setDefault(False)
        self.Prev.setFlat(True)
        self.Prev.setObjectName("Prev")
        self.horizontalLayout.addWidget(self.Prev)
        self.Stop = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/ic_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon2)
        self.Stop.setIconSize(QtCore.QSize(25, 25))
        self.Stop.setFlat(True)
        self.Stop.setObjectName("Stop")
        self.horizontalLayout.addWidget(self.Stop)
        self.PlayPause = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PlayPause.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/ic_play_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPause.setIcon(icon3)
        self.PlayPause.setIconSize(QtCore.QSize(25, 25))
        self.PlayPause.setFlat(True)
        self.PlayPause.setObjectName("PlayPause")
        self.horizontalLayout.addWidget(self.PlayPause)
        self.Next = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Next.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/ic_skip_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon4)
        self.Next.setIconSize(QtCore.QSize(25, 25))
        self.Next.setDefault(False)
        self.Next.setFlat(True)
        self.Next.setObjectName("Next")
        self.horizontalLayout.addWidget(self.Next)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 2, 2, 1)
        self.Volume = QtWidgets.QHBoxLayout()
        self.Volume.setObjectName("Volume")
        self.VolumeDecr = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.VolumeDecr.setEnabled(False)
        self.VolumeDecr.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/ic_volume_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeDecr.setIcon(icon5)
        self.VolumeDecr.setIconSize(QtCore.QSize(15, 15))
        self.VolumeDecr.setFlat(True)
        self.VolumeDecr.setObjectName("VolumeDecr")
        self.Volume.addWidget(self.VolumeDecr)
        self.VolumeSeekBar = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.VolumeSeekBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VolumeSeekBar.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.VolumeSeekBar.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSeekBar.setTickInterval(0)
        self.VolumeSeekBar.setObjectName("VolumeSeekBar")
        self.Volume.addWidget(self.VolumeSeekBar)
        self.VolumeIncr = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.VolumeIncr.setEnabled(False)
        self.VolumeIncr.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/ic_volume_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeIncr.setIcon(icon6)
        self.VolumeIncr.setIconSize(QtCore.QSize(15, 15))
        self.VolumeIncr.setFlat(True)
        self.VolumeIncr.setObjectName("VolumeIncr")
        self.Volume.addWidget(self.VolumeIncr)
        self.Mute = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Mute.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/ic_volume_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mute.setIcon(icon7)
        self.Mute.setIconSize(QtCore.QSize(20, 20))
        self.Mute.setFlat(True)
        self.Mute.setObjectName("Mute")
        self.Volume.addWidget(self.Mute)
        self.gridLayout_2.addLayout(self.Volume, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/ic_folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_File.setIcon(icon8)
        font = QtGui.QFont()
        font.setKerning(False)
        self.actionOpen_File.setFont(font)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionAbout_Project = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/ic_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Project.setIcon(icon9)
        self.actionAbout_Project.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionAbout_Project.setObjectName("actionAbout_Project")
        self.actionFetch_Recommendation = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/ic_music_note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFetch_Recommendation.setIcon(icon10)
        self.actionFetch_Recommendation.setObjectName("actionFetch_Recommendation")
        self.actionEdit_MetaData = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/ic_border_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_MetaData.setIcon(icon11)
        self.actionEdit_MetaData.setObjectName("actionEdit_MetaData")
        self.actionSee_Source_on_Github = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/GitHub-Mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSee_Source_on_Github.setIcon(icon12)
        self.actionSee_Source_on_Github.setObjectName("actionSee_Source_on_Github")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuEdit.addAction(self.actionFetch_Recommendation)
        self.menuEdit.addAction(self.actionEdit_MetaData)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuAbout.addAction(self.actionSee_Source_on_Github)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.CurrentTime.setText(_translate("MainWindow", "Time"))
        self.TotalTime.setText(_translate("MainWindow", "Time"))
        self.SongTitle.setText(_translate("MainWindow", "SongName"))
        self.SongAlbum.setText(_translate("MainWindow", "Album"))
        self.SongArtist.setText(_translate("MainWindow", "Singer"))
        self.Prev.setToolTip(_translate("MainWindow", "<html><head/><body><p>Previous</p></body></html>"))
        self.Stop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Stop</p></body></html>"))
        self.PlayPause.setToolTip(_translate("MainWindow", "<html><head/><body><p>Play/Pause</p></body></html>"))
        self.Next.setToolTip(_translate("MainWindow", "<html><head/><body><p>Next</p></body></html>"))
        self.Mute.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mute</p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_File.setText(_translate("MainWindow", "Add Music Folder"))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project"))
        self.actionFetch_Recommendation.setText(_translate("MainWindow", "Fetch Recommendation"))
        self.actionEdit_MetaData.setText(_translate("MainWindow", "Edit MetaData"))
        self.actionSee_Source_on_Github.setText(_translate("MainWindow", "See Source Code"))

