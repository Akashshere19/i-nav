import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector as conn

#for login screen
class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        loadUi("inav_login.ui",self)
        print('hello this is 1st screen')

        #if self.Button.clicked:
        self.Button.clicked.connect(self.gotscreen)
        #if self.Button.clicked:
            #self.mapmonitor.clicked.connect(self.gotscreen2)

        #Button=QPushButton()
        #Button.setsizepolicy(QSizePolicy.Expanding)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    def gotscreen(self):
        screen2= Screen2()
        username = self.username.text()
        password = self.password.text()
        db = conn.connect(host='localhost',user='root',password='akash19',db='pyqt')
        cursor = db.cursor()
        #cursor.execute("create table Inav(username varchar(20),password varchar(20))")

        if username == "inav" and password == "inav":
            #data = ("insert into inav(username,password) values(%s,%s)")
            #val =(username,password)
            #cursor.execute(data,val)
            cursor.execute("select * from Inav")
            myresult = cursor.fetchall()
            for i in myresult:
                print('username:',i[0],'password:',i[1])
            print('successfully logged in with user:',username,'and password is:',password)
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #else:
            #print('user input is invalid')
# for 2nd screen i.e MAP_Monitor
class Screen2(QMainWindow):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("Map_monitor.ui",self)
        #print('Hello this is 2nd screen')
        self.Button.clicked.connect(self.gotscreen2)

    def gotscreen2(self):
            main2 = Mainwindow()
            widget.addWidget(main2)
            widget.setCurrentIndex(widget.currentIndex() + 1)

# for 3rd screen i.e QUEUE_Monitor
class Screen3(QDialog):
    def __init__(self):
        super(Screen3,self).__init__()
        loadUi("Queue_monitor.ui",self)
        #print('done')
        self.DeleteButton.clicked.connect(self.gotscreen3)

    def gotscreen3(self):
            main3 = Screen4()
            widget.addWidget(main3)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 4th screen i.e Traffic_control
class Screen4(QDialog):
    def __init__(self):
        super(Screen4,self).__init__()
        loadUi("traffic_control.ui",self)
        #print('done')
        self.nextButton.clicked.connect(self.gotscreen4)

    def gotscreen4(self):
            main4 = Mainwindow()
            widget.addWidget(main4)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 5th screen i.e Traffic_control_monitor
class Screen5(QDialog):
    def __init__(self):
        super(Screen5,self).__init__()
        loadUi("user_interface.ui",self)
        #print('done')
        self.nextButton.clicked.connect(self.gotscreen5)

    def gotscreen5(self):
            main5 = Screen6()
            widget.addWidget(main5)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 6th screen i.e car_interrupt
class Screen6(QDialog):
    def __init__(self):
        super(Screen6,self).__init__()
        loadUi("car_interrupt.ui",self)
        #print('done')
        self.pushButton_7.clicked.connect(self.gotscreen6)

    def gotscreen6(self):
            main6 = Screen7()
            widget.addWidget(main6)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 7th screen i.e data_logging
class Screen7(QDialog):
    def __init__(self):
        super(Screen7,self).__init__()
        loadUi("data_logging.ui",self)
        #print('done')
        self.payout.clicked.connect(self.gotscreen7)

    def gotscreen7(self):
            main7 = Screen8()
            widget.addWidget(main7)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 8th screen i.e Traffic_control_monitor
class Screen8(QDialog):
    def __init__(self):
        super(Screen8,self).__init__()
        loadUi("pay_out_car.ui",self)
        #print('done')
        self.carproccess.clicked.connect(self.gotscreen8)
        

    def gotscreen8(self):
            main8 = Screen9()
            widget.addWidget(main8)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 9th screen i.e Traffic_control_monitor
class Screen9(QDialog):
    def __init__(self):
        super(Screen9,self).__init__()
        loadUi("car_proccess.ui",self)
        #print('done')
        self.carmessage.clicked.connect(self.gotscreen9)

    def gotscreen9(self):
            main9 = Screen10()
            widget.addWidget(main9)
            widget.setCurrentIndex(widget.currentIndex() + 1)
# for 10th screen i.e Traffic_control_monitor
class Screen10(QDialog):
    def __init__(self):
        super(Screen10,self).__init__()
        loadUi("car_message.ui",self)
        #print('done')
        self.login.clicked.connect(self.gotscreen10)


    def gotscreen10(self):
            main10 = Mainwindow()
            widget.addWidget(main10)
            widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main = Mainwindow()
scr2 = Screen2()
scr3 = Screen3()
scr4=Screen4()
scr5=Screen5()
scr6=Screen6()
scr7=Screen7()
scr8=Screen8()
scr9=Screen9()
scr10=Screen10()
widget.addWidget(main)
widget.addWidget(scr2)
widget.addWidget(scr3)
widget.addWidget(scr4)
widget.addWidget(scr5)
widget.addWidget(scr6)
widget.addWidget(scr7)
widget.addWidget(scr8)
widget.addWidget(scr9)
widget.addWidget(scr10)
#widget.setFixedHeight(520)
#widget.setFixedWidth(800)
widget.showNormal()
#widget.showFullScreen()
try:
    sys.exit(app.exec_())
except:
    print('exiting')