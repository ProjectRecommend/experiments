# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editMetadata_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditMetaData(object):
    def setupUi(self, EditMetaData):
        EditMetaData.setObjectName("EditMetaData")
        EditMetaData.resize(434, 371)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditMetaData.sizePolicy().hasHeightForWidth())
        EditMetaData.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditMetaData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(EditMetaData)
        self.titleLabel.setIndent(5)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.artistLabel = QtWidgets.QLabel(EditMetaData)
        self.artistLabel.setIndent(5)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.artistLineEdit)
        self.albumLabel = QtWidgets.QLabel(EditMetaData)
        self.albumLabel.setIndent(5)
        self.albumLabel.setObjectName("albumLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.albumLabel)
        self.albumLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.albumLineEdit.setObjectName("albumLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.albumLineEdit)
        self.albumArtistLabel = QtWidgets.QLabel(EditMetaData)
        self.albumArtistLabel.setIndent(5)
        self.albumArtistLabel.setObjectName("albumArtistLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.albumArtistLabel)
        self.albumArtistLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.albumArtistLineEdit.setObjectName("albumArtistLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.albumArtistLineEdit)
        self.genreLabel = QtWidgets.QLabel(EditMetaData)
        self.genreLabel.setIndent(5)
        self.genreLabel.setObjectName("genreLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.genreLabel)
        self.genreLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.genreLineEdit.setObjectName("genreLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genreLineEdit)
        self.yearLabel = QtWidgets.QLabel(EditMetaData)
        self.yearLabel.setIndent(5)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yearLineEdit)
        self.publisherLabel = QtWidgets.QLabel(EditMetaData)
        self.publisherLabel.setIndent(5)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherLineEdit = QtWidgets.QLineEdit(EditMetaData)
        self.publisherLineEdit.setObjectName("publisherLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publisherLineEdit)
        self.lyricsLabel = QtWidgets.QLabel(EditMetaData)
        self.lyricsLabel.setIndent(5)
        self.lyricsLabel.setObjectName("lyricsLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel)
        self.lyricsLineEdit = QtWidgets.QLineEdit(EditMetaData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lyricsLineEdit.sizePolicy().hasHeightForWidth())
        self.lyricsLineEdit.setSizePolicy(sizePolicy)
        self.lyricsLineEdit.setObjectName("lyricsLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lyricsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditMetaData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditMetaData)
        self.buttonBox.accepted.connect(EditMetaData.accept)
        self.buttonBox.rejected.connect(EditMetaData.reject)
        QtCore.QMetaObject.connectSlotsByName(EditMetaData)

    def retranslateUi(self, EditMetaData):
        _translate = QtCore.QCoreApplication.translate
        EditMetaData.setWindowTitle(_translate("EditMetaData", "Edit Song MetaData"))
        self.titleLabel.setText(_translate("EditMetaData", "Track Title"))
        self.artistLabel.setText(_translate("EditMetaData", "Artist"))
        self.albumLabel.setText(_translate("EditMetaData", "Album"))
        self.albumArtistLabel.setText(_translate("EditMetaData", "Album Artist"))
        self.genreLabel.setText(_translate("EditMetaData", "Genre"))
        self.yearLabel.setText(_translate("EditMetaData", "Year"))
        self.publisherLabel.setText(_translate("EditMetaData", "Publisher"))
        self.lyricsLabel.setText(_translate("EditMetaData", "Lyrics"))

