from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from PyQt5.QtGui import QIcon

from os import system
zikirlar  = ["SubhanAlloh","Alhamdulillah","Allohu Akbar"]
zikirlarindex = 0
count = 0
system("cls")  
app = QApplication([])
oyna = QWidget()

oyna.setWindowTitle("Zikirlar")

oyna.setGeometry(400,300,400,600)
oyna.setStyleSheet("""
background-color:#97d1ce;
""")
zikirlarLable = QLabel(zikirlar[zikirlarindex],oyna)
zikirlarLable.setStyleSheet("""
    font-size: 29px;
    color: red ;
    font-family : Times New Roman                    
                        """)
zikirlarLable.adjustSize()
zikirlarLable.move((oyna.width()-zikirlarLable.width())//2,150)    

knopka = QPushButton(oyna)
knopka.setGeometry(150,350,60,60)
knopka.setText("0")
knopka.setStyleSheet("""
                font-size: 22px;
                color:blue;
                background-color: lighyellow
            """)
def bosildi():
    global count,zikirlar,zikirlarindex
    count += 1
    if count == 33:
        count = 0
        zikirlarindex = (zikirlarindex + 1 )%3
    zikirlarLable.setText(zikirlar[zikirlarindex])
    zikirlarLable.adjustSize()
    knopka.setText(str(count))
knopka.clicked.connect(bosildi)

oyna.show()
app.exec()