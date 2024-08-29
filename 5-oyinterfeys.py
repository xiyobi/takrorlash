from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from PyQt5.QtGui import QIcon
from time import sleep

from os import system
system("cls")  
app = QApplication([])
oyna = QWidget()

oyna.setWindowTitle("Takarorlash")
oyna.setWindowIcon(QIcon("images.jpg"))
    
oyna.setGeometry(400,300,400,600)
oyna.setStyleSheet("""
background-color:white;
""")
    
y = 150
    #soz.setGeometry(200,80,400,300)
names = ['Asal','Zarina','Shohruh','Farangiz','Doniyor']
for ism in names:
    soz = QLabel(oyna)
    soz.move(100,y)
    y += 40 
    soz.setStyleSheet("""
        font-size: 29px;
        color: red ;
        font-family : Times New Roman                    
                        """)
    soz.setText(ism)
knopka = QPushButton(oyna)
knopka.setText("1")
# knopka.setText("close")
knopka.setText("hide")
knopka.setGeometry(90,350,200,50)
knopka.setStyleSheet("""
                font-size: 22px;
                color:blue;
                background-color:
            """)
count = 0
def bosildi():

    
    # oyna.close()
    oyna.hide()
    sleep(2)
    oyna.show()
        # global count
        # count += 1
        # knopka.setText(str(count)) 
        # print("Bosildi count = ",count)
knopka.clicked.connect(bosildi)

    #ism = input("Ismingizni kiriting: ")
    # soz.setText(ism)
    # print(soz.text())
oyna.show()
app.exec()