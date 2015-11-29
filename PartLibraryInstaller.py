#!/usr/bin/env python
# -*- coding: utf-8 -*-

#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2015 Jonathan Wiedemann <contact@freecad-france.com>    *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

__title__="FreeCAD Parts Library Installer"
__author__ = "Jonathan Wiedemann"
__url__ = "http://www.freecadweb.org"

'''
FreeCAD Parts Library installer macro

INSTALLATION

Copy paste the code bellow in the FreeCAD python console

'''

import FreeCAD, FreeCADGui, Part, zipfile, tempfile, Mesh
import os, tempfile, zipfile
from PySide import QtGui, QtCore
#from subprocess import call

class InstallerDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setObjectName("InstallerConfig")
        self.resize(318, 202)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtGui.QLabel(self)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")

        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")

        self.label2 = QtGui.QLabel(self.groupBox)
        self.label2.setObjectName("label2")

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        
        self.gridLayout.addWidget(self.label2,0,0)
        self.gridLayout.addWidget(self.lineEdit,1,0)
        self.gridLayout.addWidget(self.pushButton,1,1)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox2 = QtGui.QGroupBox(self)
        self.groupBox2.setObjectName("groupBox2")

        self.gridLayout2 = QtGui.QGridLayout(self.groupBox2)
        self.gridLayout2.setObjectName("gridLayout2")

        self.label3 = QtGui.QLabel(self.groupBox2)
        self.label3.setObjectName("label3")

        self.lineEdit2 = QtGui.QLineEdit(self.groupBox2)
        self.lineEdit2.setObjectName("lineEdit2")

        self.pushButton2 = QtGui.QPushButton(self.groupBox2)
        self.pushButton2.setObjectName("pushButton2")
        
        self.gridLayout2.addWidget(self.label3,0,0)
        self.gridLayout2.addWidget(self.lineEdit2,1,0)
        self.gridLayout2.addWidget(self.pushButton2,1,1)

        self.verticalLayout.addWidget(self.groupBox2)
        
        self.label4 = QtGui.QLabel(self)
        self.label4.setObjectName("label4")

        self.verticalLayout.addWidget(self.label4)
        
        self.progressbar = QtGui.QProgressBar(self)
        self.progressbar.setObjectName("progressbar")
        self.progressbar.setRange(0,0)
        self.progressbar.hide()

        self.verticalLayout.addWidget(self.progressbar)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.choosefolder)
        #QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged()"), self.update_information)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("clicked()"), self.setdefaulturl)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Dialog", "FreeCAD Part Library Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Informations \nThe library need 500Mo free.\nThe FreeCAD GUI will freeze during clone operation.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Part Library Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "Enter the path install of the FreeCAD Part Library.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("Dialog", "Enter the path install of the FreeCAD Part Library.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Choose folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("Dialog", "Choose folder", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox2.setTitle(QtGui.QApplication.translate("Dialog", "Share you parts !", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Dialog", "If you have a git fork of the Library.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit2.setToolTip(QtGui.QApplication.translate("Dialog", "Enter the URL of the push server here", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setText(QtGui.QApplication.translate("Dialog", "Use official", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setToolTip(QtGui.QApplication.translate("Dialog", "Use the official FreeCAD-library repository", None, QtGui.QApplication.UnicodeUTF8))
        #self.label4.setText(QtGui.QApplication.translate("Dialog", "Informations :\n", None, QtGui.QApplication.UnicodeUTF8))

    def choosefolder(self):
        self.folderDialog = QtGui.QFileDialog.getExistingDirectory(None,u"Choose where to put FreeCAD library folder")
        self.lineEdit.setText(self.folderDialog + "/")

    def setdefaulturl(self):
        self.lineEdit2.setText("https://github.com/FreeCAD/FreeCAD-library.git")
        
    def accept(self):
        #repo_dir = self.folderDialog
        repo_dir = self.lineEdit.text() + "FreeCAD-Part-Library"
        git_url = self.lineEdit2.text()
        if git_url == "":
            git_url = "https://github.com/FreeCAD/FreeCAD-library.git"
        zipurl = "https://github.com/wood-galaxy/FreeCAD-ReadTheDocs/archive/master.zip"
        
        try:
            import git
            gitOK = True
        except:
            FreeCAD.Console.PrintWarning("python-git not found. Git-related functions are disabled\n")
            gitOK = False
        try:
            import urllib
            import shutil
            legacyOK = True
        except:
            FreeCAD.Console.PrintWarning("urllib and/or shutil not found. I don't know how to download something with your computer\n")
            legacyOK = False
        if gitOK == True :
            gitclone = git.Repo.clone_from(git_url, repo_dir)
            param = FreeCAD.ParamGet('User parameter:Plugins/partlib').SetString('destination',repo_dir)
            usermacrosfolder = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').GetString('MacroPath')
            src = repo_dir + '/PartsLibrary.FCMacro'
            dst = usermacrosfolder + '/PartsLibrary.FCMacro'
            os.symlink(src, dst)
            """
            elif legacyOK == True :
                # download library in temp folder
                # create temp folder
                d=tempfile.mktemp()
                os.makedirs(d)
                # download master.zip in temp folder
                zipfilename = d + '/partslibrary.zip'
                tg = urllib.urlretrieve(zipurl,zipfilename)
    
                # open and extract it directly in the user chossen folder
                fh = open(zipfilename, 'rb')
                zfile = zipfile.ZipFile(fh)
                zfile.extractall(repo_dir)
            """
            QtGui.QDialog.accept(self)
        
d = InstallerDialog()
d.show()