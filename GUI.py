from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import threading
from Convert import Convert
from Scutti import Scutti

scutti = Scutti()
c = Convert()



class Ui_Scutti(object):
    def setupUi(self, Scutti):
        Scutti.setObjectName("Scutti")
        Scutti.resize(720, 720)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        Scutti.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Scutti)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabNav = QtWidgets.QTabWidget(Scutti)
        self.tabNav.setObjectName("tabNav")
        self.tabHome = QtWidgets.QWidget()
        self.tabHome.setObjectName("tabHome")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabHome)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblScutti = QtWidgets.QLabel(self.tabHome)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(48)
        self.lblScutti.setFont(font)
        self.lblScutti.setAlignment(QtCore.Qt.AlignCenter)
        self.lblScutti.setObjectName("lblScutti")
        self.gridLayout_3.addWidget(self.lblScutti, 0, 0, 1, 1)
        self.lblCollection = QtWidgets.QLabel(self.tabHome)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(26)
        self.lblCollection.setFont(font)
        self.lblCollection.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCollection.setObjectName("lblCollection")
        self.gridLayout_3.addWidget(self.lblCollection, 1, 0, 1, 1)
        self.txtCollection = QtWidgets.QTextEdit(self.tabHome)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(36)
        self.txtCollection.setFont(font)
        self.txtCollection.setObjectName("txtCollection")
        self.gridLayout_3.addWidget(self.txtCollection, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tabHome)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")

        # Radio Buttons
        self.rbManual = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(18)
        self.rbManual.setFont(font)
        self.rbManual.setObjectName("rbManual")
        self.gridLayout.addWidget(self.rbManual, 0, 0, 1, 1)
        self.rbAutomatic = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(18)
        self.rbAutomatic.setFont(font)
        self.rbAutomatic.setObjectName("rbAutomatic")
        self.gridLayout.addWidget(self.rbAutomatic, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 1)

        # Set Manual As Default Mode
        self.rbManual.setChecked(True)

        # Combo Box
        self.cmbSelect = QtWidgets.QComboBox(self.tabHome)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.cmbSelect.setFont(font)
        self.cmbSelect.setObjectName("cmbSelect")
        self.cmbSelect.addItem("")
        self.cmbSelect.addItem("")
        self.gridLayout_3.addWidget(self.cmbSelect, 4, 0, 1, 1)

        # Start Button
        self.btnStart = QtWidgets.QPushButton(self.tabHome, clicked = lambda: self.run())
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout_3.addWidget(self.btnStart, 5, 0, 1, 1)
        self.tabNav.addTab(self.tabHome, "")
        self.tabConvert = QtWidgets.QWidget()
        self.tabConvert.setObjectName("tabConvert")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabConvert)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblConvert = QtWidgets.QLabel(self.tabConvert)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(22)
        self.lblConvert.setFont(font)
        self.lblConvert.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblConvert.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConvert.setObjectName("lblConvert")
        self.verticalLayout_3.addWidget(self.lblConvert)

        # Convert Button
        self.btnConvertOpen = QtWidgets.QPushButton(self.tabConvert, clicked = lambda: self.convert())
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.btnConvertOpen.setFont(font)
        self.btnConvertOpen.setObjectName("btnConvertOpen")
        self.verticalLayout_3.addWidget(self.btnConvertOpen)
        self.tabNav.addTab(self.tabConvert, "")
        self.tabFilter = QtWidgets.QWidget()
        self.tabFilter.setObjectName("tabFilter")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabFilter)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTemplate = QtWidgets.QLabel(self.tabFilter)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(28)
        self.lblTemplate.setFont(font)
        self.lblTemplate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTemplate.setObjectName("lblTemplate")
        self.verticalLayout_2.addWidget(self.lblTemplate)
        self.btnTemplate = QtWidgets.QPushButton(self.tabFilter)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.btnTemplate.setFont(font)
        self.btnTemplate.setObjectName("btnTemplate")
        self.verticalLayout_2.addWidget(self.btnTemplate)
        self.btnMatchDirectory = QtWidgets.QPushButton(self.tabFilter)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.btnMatchDirectory.setFont(font)
        self.btnMatchDirectory.setObjectName("btnMatchDirectory")
        self.verticalLayout_2.addWidget(self.btnMatchDirectory)
        self.label = QtWidgets.QLabel(self.tabFilter)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.sliderThreshold = QtWidgets.QSlider(self.tabFilter)
        self.sliderThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.sliderThreshold.setObjectName("sliderThreshold")
        self.verticalLayout_2.addWidget(self.sliderThreshold)
        self.btnMatchStart = QtWidgets.QPushButton(self.tabFilter)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(24)
        self.btnMatchStart.setFont(font)
        self.btnMatchStart.setObjectName("btnMatchStart")
        self.verticalLayout_2.addWidget(self.btnMatchStart)
        self.tabNav.addTab(self.tabFilter, "")

        # Settings Tab
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabSettings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tabSettings)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -59, 680, 728))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblWidth = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblWidth.setFont(font)
        self.lblWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWidth.setObjectName("lblWidth")
        self.gridLayout_4.addWidget(self.lblWidth, 0, 0, 1, 1)

        # Width Input
        self.txtWidth = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtWidth.setFont(font)
        self.txtWidth.setObjectName("txtWidth")
        self.gridLayout_4.addWidget(self.txtWidth, 1, 0, 1, 1)
        self.lblHeight = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblHeight.setFont(font)
        self.lblHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeight.setObjectName("lblHeight")
        self.gridLayout_4.addWidget(self.lblHeight, 2, 0, 1, 1)

        # Height Input
        self.txtHeight = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtHeight.setFont(font)
        self.txtHeight.setObjectName("txtHeight")
        self.gridLayout_4.addWidget(self.txtHeight, 3, 0, 1, 1)
        self.lblXStart = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblXStart.setFont(font)
        self.lblXStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXStart.setObjectName("lblXStart")
        self.gridLayout_4.addWidget(self.lblXStart, 4, 0, 1, 1)

        # XStart Input
        self.txtXStart = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtXStart.setFont(font)
        self.txtXStart.setObjectName("txtXStart")
        self.gridLayout_4.addWidget(self.txtXStart, 5, 0, 1, 1)
        self.lblYStart = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblYStart.setFont(font)
        self.lblYStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblYStart.setObjectName("lblYStart")
        self.gridLayout_4.addWidget(self.lblYStart, 6, 0, 1, 1)

        # YStart
        self.txtYStart = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtYStart.setFont(font)
        self.txtYStart.setObjectName("txtYStart")
        self.gridLayout_4.addWidget(self.txtYStart, 7, 0, 1, 1)
        self.lblCaptureKey = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblCaptureKey.setFont(font)
        self.lblCaptureKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCaptureKey.setObjectName("lblCaptureKey")
        self.gridLayout_4.addWidget(self.lblCaptureKey, 8, 0, 1, 1)

        # Capture Key Input
        self.txtCaptureKey = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtCaptureKey.setFont(font)
        self.txtCaptureKey.setObjectName("txtCaptureKey")
        self.gridLayout_4.addWidget(self.txtCaptureKey, 9, 0, 1, 1)
        self.lblQuitKey = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblQuitKey.setFont(font)
        self.lblQuitKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQuitKey.setObjectName("lblQuitKey")
        self.gridLayout_4.addWidget(self.lblQuitKey, 10, 0, 1, 1)

        # Quit Key Input
        self.txtQuitKey = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtQuitKey.setFont(font)
        self.txtQuitKey.setObjectName("txtQuitKey")
        self.gridLayout_4.addWidget(self.txtQuitKey, 11, 0, 1, 1)
        self.lblInterval = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblInterval.setFont(font)
        self.lblInterval.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInterval.setObjectName("lblInterval")
        self.gridLayout_4.addWidget(self.lblInterval, 12, 0, 1, 1)

        # Interval Input
        self.txtInterval = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtInterval.setFont(font)
        self.txtInterval.setObjectName("txtInterval")
        self.gridLayout_4.addWidget(self.txtInterval, 13, 0, 1, 1)
        self.lblIDelay = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.lblIDelay.setFont(font)
        self.lblIDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIDelay.setObjectName("lblIDelay")
        self.gridLayout_4.addWidget(self.lblIDelay, 14, 0, 1, 1)

        # Delay Input
        self.txtDelay = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(20)
        self.txtDelay.setFont(font)
        self.txtDelay.setObjectName("txtDelay")
        self.gridLayout_4.addWidget(self.txtDelay, 15, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.tabNav.addTab(self.tabSettings, "")
        self.verticalLayout.addWidget(self.tabNav)

        self.retranslateUi(Scutti)
        self.tabNav.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Scutti)

    def retranslateUi(self, Scutti):
        _translate = QtCore.QCoreApplication.translate
        Scutti.setWindowTitle(_translate("Scutti", "Scutti"))
        self.lblScutti.setText(_translate("Scutti", "Scutti"))
        self.lblCollection.setText(_translate("Scutti", "Collection Name"))
        self.rbManual.setText(_translate("Scutti", "Manual"))
        self.rbAutomatic.setText(_translate("Scutti", "Automatic"))
        self.cmbSelect.setItemText(0, _translate("Scutti", "Screenshot"))
        self.cmbSelect.setItemText(1, _translate("Scutti", "Camera"))
        self.btnStart.setText(_translate("Scutti", "Start"))
        self.tabNav.setTabText(self.tabNav.indexOf(self.tabHome), _translate("Scutti", "Home"))
        self.lblConvert.setText(_translate("Scutti", "Convert video file into Photos"))
        self.btnConvertOpen.setText(_translate("Scutti", "Convert File"))
        self.tabNav.setTabText(self.tabNav.indexOf(self.tabConvert), _translate("Scutti", "Convert"))
        self.lblTemplate.setText(_translate("Scutti", "Upload a template picture to match to photos in a directory"))
        self.btnTemplate.setText(_translate("Scutti", "Template Photo"))
        self.btnMatchDirectory.setText(_translate("Scutti", "Directory"))
        self.label.setText(_translate("Scutti", "Threshold"))
        self.btnMatchStart.setText(_translate("Scutti", "Start"))
        self.tabNav.setTabText(self.tabNav.indexOf(self.tabFilter), _translate("Scutti", "Filter && Sort"))
        self.lblWidth.setText(_translate("Scutti", "Width"))
        self.lblHeight.setText(_translate("Scutti", "Height"))
        self.lblXStart.setText(_translate("Scutti", "X Start"))
        self.lblYStart.setText(_translate("Scutti", "Y Start"))
        self.lblCaptureKey.setText(_translate("Scutti", "Capture Key"))
        self.lblQuitKey.setText(_translate("Scutti", "Quit Key"))
        self.lblInterval.setText(_translate("Scutti", "Interval"))
        self.lblIDelay.setText(_translate("Scutti", "Initial Delay"))
        self.tabNav.setTabText(self.tabNav.indexOf(self.tabSettings), _translate("Scutti", "Settings"))

    # Convert Video To Pictures
    def convert(self):
        self.update()
        file = QFileDialog.getOpenFileName()
        if file: 
            task = threading.Thread(target=c.start, args=(scutti.getcollection(), file[0]))
            task.start()

    
    # Update Values
    def update(self):

        # Collection
        if len(self.txtCollection.toPlainText()) > 0: 
            scutti.setcollection(self.txtCollection.toPlainText())
            print('Collection set:', scutti.getcollection())

        # Settings Page Updates
        if len(self.txtWidth.toPlainText()) > 0: 
            scutti.setWidth(int(self.txtWidth.toPlainText()))
            print('Width set:', scutti.getWidth())
        
        if len(self.txtHeight.toPlainText()) > 0:
            scutti.setHeight(int(self.txtHeight.toPlainText()))
            print('Height set:', scutti.getHeight())

        if len(self.txtXStart.toPlainText()) > 0:
            scutti.setXStart(int(self.txtXStart.toPlainText()))
            print('XStart set:', scutti.getXStart())

        if len(self.txtYStart.toPlainText()) > 0:
            scutti.setYStart(int(self.txtYStart.toPlainText()))
            print('YStart set:', scutti.getYStart())

        if len(self.txtInterval.toPlainText()) > 0:
            scutti.setInterval(int(self.txtInterval.toPlainText()))
            print('Interval set:', scutti.getInterval())
        
        if len(self.txtDelay.toPlainText()) > 0:
            scutti.setDelay(int(self.txtDelay.toPlainText()))
            print('Delay set:', scutti.getDelay())
        
        if len(self.txtCaptureKey.toPlainText()) > 0:
            if len(self.txtCaptureKey.toPlainText()) >= 2:
                print('Capture key must be 1 key')
                return
            scutti.setSnapKey(self.txtCaptureKey.toPlainText())
            print('Capture key set:', scutti.getSnapKey())
    
        if len(self.txtQuitKey.toPlainText()) > 0:
            if len(self.txtQuitKey.toPlainText()) >= 2:
                print('Quit key must be 1 key')
                return
            scutti.setQuitKey(self.txtQuitKey.toPlainText())
            print('Quit key set:', scutti.getQuitKey())
        
        # Error handling
        scutti.seemsLegit()

    # Runtime Logic
    def run(self):
        self.update()
        if threading.active_count() >= 4:
            print('Already running a process.')
            print('To start a new process, end the current one by pressing', scutti.getQuitKey())
            return

        # Set Collection
        scutti.soundSnippets
        scutti.setcollection(self.txtCollection.toPlainText())

        # Choose function
        if self.cmbSelect.currentText() == 'Screenshot' and self.rbManual.isChecked():
            print('Manual Screenshot Selected')
            task = threading.Thread(target=scutti.sctManual)
            task.start()
        elif self.cmbSelect.currentText() == 'Screenshot' and self.rbAutomatic.isChecked():
            task = threading.Thread(target=scutti.sctAuto)
            task.start()
        elif self.cmbSelect.currentText() == 'Camera' and self.rbManual.isChecked():
            task = threading.Thread(target=scutti.camManual)
            task.start()
        elif self.cmbSelect.currentText() == 'Camera' and self.rbAutomatic.isChecked():
            task = threading.Thread(target=scutti.camAuto)
            task.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Scutti()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
