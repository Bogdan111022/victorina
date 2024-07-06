from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500,500)




quest_lbl = QLabel("У якому році перший канал отримав золоту кнопку від ютуб?")
v_2005 = QRadioButton("2005")
v_2010 = QRadioButton("2010")
v_2015 = QRadioButton("2015")
v_2020 = QRadioButton("2020")

quest2_lbl = QLabel ("у якому році був створений ютуб")
v2_2017 = QRadioButton("10 липня 2017 року")
v2_2015 = QRadioButton("14 лютого 2005 року")
v2_2000 = QRadioButton("20 червня 2000 року")
v2_2010 = QRadioButton("1 квітня 2010 року")



main_line = QVBoxLayout()
main_line.addWidget(quest_lbl)


horizontal_linia = QHBoxLayout()
horizontal_linia.addWidget(v_2005)
horizontal_linia.addWidget(v_2010)
main_line.addLayout(horizontal_linia)

line2 = QHBoxLayout()
line2.addWidget(v_2015)
line2.addWidget(v_2020)
main_line.addLayout(line2)


main_line.addWidget(quest2_lbl)



def show_win():
    win_msg = QMessageBox()
    win_msg.setText("Ти переміг!!")
    win_msg.exec()

v_2005.clicked.connect(show_win)
window.setLayout(main_line)
window.show()
app.exec()