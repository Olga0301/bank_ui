from threading import  Thread

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QPushButton, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(669, 480)
        Form.setMinimumSize(QSize(480, 320))
        Form.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #457b9d;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QCheckBox{\n"
"	font-family: \"Arial\";\n"
"	font-size: 14px;\n"
"	font-style: bold;\n"
"	background-color: #a8dadc;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: #1d3557;\n"
"	border-radius: 25px;\n"
"	height: 50px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #a8dadc;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: #1d3557;\n"
"	border-radius: 25px;\n"
"	height: 50px;\n"
"	font-family: \"Arial\";\n"
"	font-size: 40px;\n"
"	font-style: bold;\n"
"	color: #1d3557;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")


        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_data = {
            '202': self.checkBox,
            '154': self.checkBox_2,
            '194': self.checkBox_3,
            '198': self.checkBox_4
        }

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self._check_data)

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"BELPOST", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u041a\u0420\u0415\u0414\u0418\u0422 \u041e\u0410\u041e \u0411\u0415\u041b\u0410\u0420\u0423\u0421\u0411\u0410\u041d\u041a", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u041f\u041e\u0427\u0422\u041e\u0412\u042b\u0419 \u0414\u0415\u041d\u0415\u0416\u041d\u042b\u0419 \u041f\u0415\u0420\u0415\u0412\u041e\u0414", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u0412\u042b\u041f\u041b\u0410\u0422\u0410 \u041f\u0415\u041d\u0421\u0418\u0419 \u0418 \u041f\u041e\u0421\u041e\u0411\u0418\u0419", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u041f\u0420\u0418\u0415\u041c \u041f\u041b\u0410\u0422\u0415\u0416\u0415\u0419", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c", None))
    # retranslateUi

    def _check_data(self):
        from utils import get_response
        res = ''
        for key, value in self.checkBox_data.items():
            if value.isChecked():
                res += f'&services[]={key}'

        thread = Thread(target=get_response, args=(res, ))
        thread.start()
