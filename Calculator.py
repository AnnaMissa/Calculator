from PyQt5 import QtCore, QtGui, QtWidgets
import math


b = ''
c = ''
op = ''


def numb(a):
    global b
    if b == '':
        b = a
    else:
        b = b + a

def getnumb(a):
    if a.find('.') == -1:
        a = int(a)
    else:
        a = float(a)
    return a


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(70, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(120, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(170, 280, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(170, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(170, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(170, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(70, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(20, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(120, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(20, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 191, 51))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(90, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 223, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.but1) #1
        self.pushButton_2.clicked.connect(self.but2) #2
        self.pushButton_3.clicked.connect(self.but3) #3
        self.pushButton_4.clicked.connect(self.but4) #4
        self.pushButton_5.clicked.connect(self.but5) #5
        self.pushButton_6.clicked.connect(self.but6) #6
        self.pushButton_7.clicked.connect(self.but7) #7
        self.pushButton_8.clicked.connect(self.but8) #8
        self.pushButton_9.clicked.connect(self.but9) #9
        self.pushButton_11.clicked.connect(self.but11) #0

        self.pushButton_10.clicked.connect(self.but10)  # +/-
        self.pushButton_12.clicked.connect(self.but12)  # .

        self.pushButton_13.clicked.connect(self.but13) # =
        self.pushButton_14.clicked.connect(self.but14)  # +
        self.pushButton_15.clicked.connect(self.but15)  # -
        self.pushButton_16.clicked.connect(self.but16)  # *
        self.pushButton_17.clicked.connect(self.but17)  # /
        self.pushButton_18.clicked.connect(self.but18)  # x2
        self.pushButton_19.clicked.connect(self.but19)  # sqrt
        self.pushButton_21.clicked.connect(self.but21)  # 1/x

        self.pushButton_22.clicked.connect(self.but22)  # CE
        self.pushButton_23.clicked.connect(self.but23)  # C
        self.pushButton_24.clicked.connect(self.but24)  # del


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "+/-"))
        self.pushButton_11.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "="))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setText(_translate("MainWindow", "*"))
        self.pushButton_17.setText(_translate("MainWindow", "/"))
        self.pushButton_18.setText(_translate("MainWindow", "x²"))
        self.pushButton_19.setText(_translate("MainWindow", "√"))
        self.pushButton_21.setText(_translate("MainWindow", "1/x"))
        self.pushButton_22.setText(_translate("MainWindow", "CE"))
        self.pushButton_23.setText(_translate("MainWindow", "C"))
        self.pushButton_24.setText(_translate("MainWindow", "←"))

    def insert_text(self, a):
        self.textEdit.insertPlainText(a)
        numb(a)

    def insert_c_op(self, c, op):
        self.textEdit.insertPlainText(c)
        self.textEdit.insertPlainText(' ')
        self.textEdit.insertPlainText(op)
        self.textEdit.insertPlainText(' ')

    def check_for_zero(self, b, c):
        if b == 0:
            c = 'DivByZeroError'
            self.textEdit.insertPlainText(c)
            b = ''
        else:
            b = c / b
            if b.is_integer():
                b = int(b)
        return b

    def but1(self): #1
        a = '1'
        self.insert_text(a)

    def but2(self): #2
        a = '2'
        self.insert_text(a)

    def but3(self): #3
        a = '3'
        self.insert_text(a)

    def but4(self): #4
        a = '4'
        self.insert_text(a)

    def but5(self): #5
        a = '5'
        self.insert_text(a)

    def but6(self): #6
        a = '6'
        self.insert_text(a)

    def but7(self): #7
        a = '7'
        self.insert_text(a)

    def but8(self): #8
        a = '8'
        self.insert_text(a)

    def but9(self): #9
        a = '9'
        self.insert_text(a)

    def but10(self): #+/-
        global b, c, op
        if b != '0' and b != '' and c == '':
            b = getnumb(b)
            b = -b
            b = str(b)
            self.textEdit.clear()
            self.textEdit.insertPlainText(b)
        elif b != '0' and b != '' and c != '':
            b = getnumb(b)
            b = -b
            b = str(b)
            self.textEdit.clear()
            self.insert_c_op(c, op)
            self.textEdit.insertPlainText(b)

    def but11(self): #0
        global b
        a = '0'
        if b == '':
            b = a
            self.textEdit.insertPlainText(a)
        elif b != '0':
            b = b + a
            self.textEdit.insertPlainText(a)

    def but12(self): # .
        global b, c, op
        a = '.'
        if b.find('.') == -1:
            if b == '' or b == '0':
                b = '0.'
            else:
                b = b + a
        self.textEdit.clear()
        if c != '':
            self.insert_c_op(c, op)
        self.textEdit.insertPlainText(b)

    def but13(self): #=
        global b, c, op
        self.textEdit.insertPlainText(' = ')
        if len(b) > 0:
            b = getnumb(b)
            c = getnumb(c)
            self.textEdit.clear()
            if op == '+':
                b = c + b
            elif op == '-':
                b = c - b
            elif op == '*':
                b = c * b
            elif op == '/':
                b = self.check_for_zero(b, c)
            b = str(b)
            self.textEdit.insertPlainText(b)
            c = ''
            op = ''
        else:
            b = c
            c = ''
            op = ''
            self.textEdit.clear()
            self.textEdit.insertPlainText(b)

    def but14(self): #+
        global b, c, op
        self.textEdit.insertPlainText(' + ')
        if c == '' and op == '':
            c = b
            b = ''
            op = '+'
        elif op == '+':
            b = getnumb(b)
            c = getnumb(c)
            b = c + b
            self.textEdit.clear()
            self.textEdit.insertPlainText(str(b))
            c = str(b)
            b = ''
            self.textEdit.insertPlainText(' + ')
        elif op != '+' and b == '':
            op = '+'
            self.textEdit.clear()
            self.textEdit.insertPlainText(c)
            self.textEdit.insertPlainText(' + ')
        elif op != '+' and b != '':
            b = getnumb(b)
            c = getnumb(c)
            self.textEdit.clear()
            if op == '-':
                b = c - b
            elif op == '*':
                b = c * b
            elif op == '/':
                b = self.check_for_zero(b, c)
            self.textEdit.insertPlainText(str(b))
            self.textEdit.insertPlainText(' + ')
            c = str(b)
            b = ''
            op = '+'

    def but15(self): #-
        global b, c, op
        self.textEdit.insertPlainText(' - ')
        if c == '' and op == '':
            c = b
            b = ''
            op = '-'
        elif op == '-':
            b = getnumb(b)
            c = getnumb(c)
            b = c - b
            self.textEdit.clear()
            self.textEdit.insertPlainText(str(b))
            self.textEdit.insertPlainText(' - ')
            c = str(b)
            b = ''
        elif op != '-' and b == '':
            op = '-'
            self.textEdit.clear()
            self.textEdit.insertPlainText(c)
            self.textEdit.insertPlainText(' - ')
        elif op != '-' and b != '':
            b = getnumb(b)
            c = getnumb(c)
            self.textEdit.clear()
            if op == '+':
                b = c + b
            elif op == '*':
                b = c * b
            elif op == '/':
                b = self.check_for_zero(b, c)
            self.textEdit.insertPlainText(str(b))
            self.textEdit.insertPlainText(' - ')
            c = str(b)
            b = ''
            op = '-'

    def but16(self): #*
        global b, c, op
        self.textEdit.insertPlainText(' * ')
        if c == '' and op == '':
            c = b
            b = ''
            op = '*'
        elif op == '*':
            b = getnumb(b)
            c = getnumb(c)
            b = c * b
            self.textEdit.clear()
            self.textEdit.insertPlainText(str(b))
            c = str(b)
            b = ''
            self.textEdit.insertPlainText(' * ')
        elif op != '*' and b == '':
            op = '*'
            self.textEdit.clear()
            self.textEdit.insertPlainText(c)
            self.textEdit.insertPlainText(' * ')
        elif op != '*' and b != '':
            b = getnumb(b)
            c = getnumb(c)
            self.textEdit.clear()
            if op == '+':
                b = c + b
            elif op == '-':
                b = c - b
            elif op == '/':
                b = self.check_for_zero(b, c)
            self.textEdit.insertPlainText(str(b))
            self.textEdit.insertPlainText(' * ')
            c = str(b)
            b = ''
            op = '*'

    def but17(self): #/
        global b, c, op
        self.textEdit.insertPlainText(' / ')
        if c == '' and op == '':
            c = b
            b = ''
            op = '/'
        elif op == '/':
            b = getnumb(b)
            c = getnumb(c)
            self.textEdit.clear()
            if b == 0:
                c = 'DivByZeroError'
                self.textEdit.insertPlainText(c)
                b = ''
            else:
                b = c / b
                if b.is_integer():
                    b = int(b)
            self.textEdit.insertPlainText(str(b))
            c = str(b)
            b = ''
            self.textEdit.insertPlainText(' / ')
        elif op != '/' and b != '':
            b = getnumb(b)
            c = getnumb(c)
            if op == '+':
                b = c + b
            elif op == '-':
                b = c - b
            elif op == '*':
                b = c * b
            self.textEdit.clear()
            self.textEdit.insertPlainText(str(b))
            self.textEdit.insertPlainText(' / ')
            c = str(b)
            b = ''
            op = '/'

    def but18(self): #x2
        global b, c, op
        if c != '' and b == '':
            c = getnumb(c)
            b = c * c
        else:
            b = getnumb(b)
            b = b * b
        c = ''
        op = ''
        b = str(b)
        self.textEdit.clear()
        self.textEdit.insertPlainText(b)

    def but19(self): #sqrt
        global b, c, op
        if c != '' and b == '':
            c = getnumb(c)
            b = math.sqrt(c)
        else:
            b = getnumb(b)
            b = math.sqrt(b)
        c = ''
        op = ''
        self.textEdit.clear()
        if b.is_integer():
            b = int(b)
        b = str(b)
        self.textEdit.insertPlainText(b)

    def but21(self): #1/x
        global b, c, op
        self.textEdit.clear()
        if c != '' and b == '':
            c = getnumb(c)
            if c != 0:
                b = 1 / c
            else:
                b = 'DivByZeroError'
                self.textEdit.insertPlainText(b)
                b = ''
        else:
            b = getnumb(b)
            if b != 0:
                b = 1 / b
            else:
                b = 'DivByZeroError'
                self.textEdit.insertPlainText(b)
                b = ''
        c = ''
        op = ''
        b = str(b)
        self.textEdit.insertPlainText(b)

    def but22(self): #CE
        global b, c, op
        b = ''
        c = ''
        op = ''
        self.textEdit.clear()

    def but23(self): #C
        global b, c, op
        if c == '' and b != '':
            b = ''
            op = ''
        elif c != '':
            b = ''
            self.textEdit.clear()
            self.insert_c_op(c, op)

    def but24(self): #del
        global b, c, op
        if b != '':
            a = len(b)
            b = b[:a-1]
            self.textEdit.clear()
            if c != '':
                self.insert_c_op(c, op)
            self.textEdit.insertPlainText(b)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())