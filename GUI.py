from msilib.schema import ComboBox
from turtle import onclick
from Scutti import Scutti
from PyQt5 import QtCore, QtGui, QtWidgets

scutti = Scutti()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 645)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")

        # settings Page
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settingsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblSettings = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(36)
        font.setBold(False)
        self.lblSettings.setFont(font)
        self.lblSettings.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSettings.setObjectName("lblSettings")
        self.verticalLayout_2.addWidget(self.lblSettings)
        self.lblWidth = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblWidth.setFont(font)
        self.lblWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWidth.setObjectName("lblWidth")
        self.verticalLayout_2.addWidget(self.lblWidth)

        # Width
        self.txtWidth = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtWidth.setFont(font)
        self.txtWidth.setObjectName("txtWidth")
        self.verticalLayout_2.addWidget(self.txtWidth)
        self.lblHeight = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblHeight.setFont(font)
        self.lblHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeight.setObjectName("lblHeight")
        self.verticalLayout_2.addWidget(self.lblHeight)

        #Height
        self.txtHeight = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtHeight.setFont(font)
        self.txtHeight.setObjectName("txtHeight")
        self.verticalLayout_2.addWidget(self.txtHeight)
        self.lblXStart = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblXStart.setFont(font)
        self.lblXStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXStart.setObjectName("lblXStart")
        self.verticalLayout_2.addWidget(self.lblXStart)
        self.txtXStart = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtXStart.setFont(font)
        self.txtXStart.setObjectName("txtXStart")
        self.verticalLayout_2.addWidget(self.txtXStart)
        self.lblYStart = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblYStart.setFont(font)
        self.lblYStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblYStart.setObjectName("lblYStart")
        self.verticalLayout_2.addWidget(self.lblYStart)
        self.txtYStart = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtYStart.setFont(font)
        self.txtYStart.setObjectName("txtYStart")
        self.verticalLayout_2.addWidget(self.txtYStart)
        self.lblSnapKey = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblSnapKey.setFont(font)
        self.lblSnapKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSnapKey.setObjectName("lblSnapKey")
        self.verticalLayout_2.addWidget(self.lblSnapKey)
        self.txtSnapKey = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtSnapKey.setFont(font)
        self.txtSnapKey.setObjectName("txtSnapKey")
        self.verticalLayout_2.addWidget(self.txtSnapKey)
        self.lblQuitKey = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        self.lblQuitKey.setFont(font)
        self.lblQuitKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQuitKey.setObjectName("lblQuitKey")
        self.verticalLayout_2.addWidget(self.lblQuitKey)
        self.txtQuitKey = QtWidgets.QTextEdit(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        self.txtQuitKey.setFont(font)
        self.txtQuitKey.setObjectName("txtQuitKey")
        self.verticalLayout_2.addWidget(self.txtQuitKey)

        # Home Button 
        self.btnHomeNav = QtWidgets.QPushButton(self.settingsPage, clicked = lambda: self.toHome() )
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(12)
        self.btnHomeNav.setFont(font)
        self.btnHomeNav.setObjectName("btnHomeNav")
        self.verticalLayout_2.addWidget(self.btnHomeNav)
        self.stackedWidget.addWidget(self.settingsPage)
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.gridLayout = QtWidgets.QGridLayout(self.homePage)
        self.gridLayout.setObjectName("gridLayout")

        # Start Button
        self.btnStart = QtWidgets.QPushButton(self.homePage, clicked = lambda: self.run())
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        font.setBold(False)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")

        # Combo box
        self.gridLayout.addWidget(self.btnStart, 11, 0, 2, 1)
        self.cmbSelect = QtWidgets.QComboBox(self.homePage)
        self.cmbSelect.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        font.setBold(False)
        self.cmbSelect.setFont(font)
        self.cmbSelect.setObjectName("cmbSelect")
        self.cmbSelect.addItem("")
        self.cmbSelect.addItem("")
        self.cmbSelect.addItem("")
        self.cmbSelect.addItem("")
        self.gridLayout.addWidget(self.cmbSelect, 10, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.homePage)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        #Collection
        self.txtCollection = QtWidgets.QTextEdit(self.homePage)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(20)
        self.txtCollection.setFont(font)
        self.txtCollection.setObjectName("txtCollection")
        self.gridLayout.addWidget(self.txtCollection, 6, 0, 1, 1)
        self.lblCollection = QtWidgets.QLabel(self.homePage)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblCollection.setFont(font)
        self.lblCollection.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCollection.setObjectName("lblCollection")
        self.gridLayout.addWidget(self.lblCollection, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        #Settings
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.btnSettingsNav = QtWidgets.QPushButton(self.homePage, clicked = lambda: self.toSettings())
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(12)
        self.btnSettingsNav.setFont(font)
        self.btnSettingsNav.setObjectName("btnSettingsNav")
        self.gridLayout.addWidget(self.btnSettingsNav, 15, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 14, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 350, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 13, 0, 1, 1)
        self.stackedWidget.addWidget(self.homePage)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scutti"))
        self.lblSettings.setText(_translate("Form", "Settings"))
        self.lblWidth.setText(_translate("Form", "Width"))
        self.lblHeight.setText(_translate("Form", "Height"))
        self.lblXStart.setText(_translate("Form", "X Start"))
        self.lblYStart.setText(_translate("Form", "Y Start"))
        self.lblSnapKey.setText(_translate("Form", "Capture Key"))
        self.lblQuitKey.setText(_translate("Form", "Quit Key"))
        self.btnHomeNav.setText(_translate("Form", "Home"))
        self.btnStart.setText(_translate("Form", "Start"))
        self.cmbSelect.setItemText(0, _translate("Form", "Manual Screenshot"))
        self.cmbSelect.setItemText(1, _translate("Form", "Automatic Screenshot"))
        self.cmbSelect.setItemText(2, _translate("Form", "Manual Camera"))
        self.cmbSelect.setItemText(3, _translate("Form", "Automatic Camera"))
        self.label.setText(_translate("Form", "Scutti"))
        self.lblCollection.setText(_translate("Form", "Collection Name"))
        self.btnSettingsNav.setText(_translate("Form", "Settings"))

    # Navigation  
    def toSettings(self):
        self.stackedWidget.setCurrentIndex(0)
    
    # Navigation  
    def toHome(self):
        self.update()
        self.stackedWidget.setCurrentIndex(1)

    # Update Values
    def update(self):

        if len(self.txtWidth.toPlainText()) > 0: 
            scutti.setWidth(int(self.txtWidth.toPlainText()))
            print(scutti.getWidth())
        
        if len(self.txtHeight.toPlainText()) > 0:
            scutti.setHeight(int(self.txtHeight.toPlainText()))

        if len(self.txtXStart.toPlainText()) > 0:
            scutti.setXStart(int(self.txtXStart.toPlainText()))

        if len(self.txtYStart.toPlainText()) > 0:
            scutti.setYStart(int(self.txtYStart.toPlainText()))
        
        if len(self.txtSnapKey.toPlainText()) > 0:
            if len(self.txtSnapKey.toPlainText()) >= 2:
                print('Capture key must be 1 key')
                return
            scutti.setSnapKey(self.txtSnapKey.toPlainText())
    
        if len(self.txtQuitKey.toPlainText()) > 0:
            if len(self.txtQuitKey.toPlainText()) >= 2:
                print('Quit key must be 1 key')
                return
            scutti.setQuitKey(self.txtQuitKey.toPlainText())
        
        scutti.seemsLegit()

    # Runtime Logic
    def run(self):

        # Set Collection
        scutti.setcollection(self.txtCollection.toPlainText())

        # Choose function
        if self.cmbSelect.currentText() == 'Manual Screenshot':
            scutti.sctManual()
        elif self.cmbSelect.currentText() == 'Automatic Screenshot':
            scutti.sctAuto()
        elif self.cmbSelect.currentText() == 'Manual Camera':
            scutti.camManual()
        elif self.cmbSelect.currentText() == 'Automatic Camera':
            scutti.camAuto()
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
