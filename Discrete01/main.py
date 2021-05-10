from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QWidget
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette, QBrush
from PyQt5 import QtCore
import numpy as np
import sys
# Methods from previous tasks
from sets import Sets


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.sets = Sets()

        self.setObjectName("main")
        self.setWindowTitle("Sets")
        self.setWindowIcon(QIcon('./assets/images/icon.png'))
        self.setStyleSheet(open('./assets/css/style.css').read())
        self.setMinimumSize(1000, 650)
        self.setMaximumSize(1000, 650)
        self.setGeometry(300, 100, 800, 600)

        self.initUI()
        

    def initUI(self):
        
        # Background
        img = QImage("./assets/images/city.webp")
        sImage = img.scaled(QtCore.QSize(1000, 650))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.union = QPushButton('Union' , self)
        self.union.setObjectName("union")
        self.union.setGeometry(0, 0, 200, 50)
        self.union.clicked.connect(self.solve)

        self.intersection = QPushButton('Intersection' , self)
        self.intersection.setObjectName("intersection")
        self.intersection.setGeometry(200, 0, 200, 50)
        self.intersection.clicked.connect(self.solve)

        self.diff = QPushButton('Difference' , self)
        self.diff.setObjectName("difference")
        self.diff.setGeometry(400, 0, 200, 50)
        self.diff.clicked.connect(self.solve)

        self.symm_diff = QPushButton('Symmetrical diff.' , self)
        self.symm_diff.setObjectName("symmetrical_difference")
        self.symm_diff.setGeometry(600, 0, 200, 50)
        self.symm_diff.clicked.connect(self.solve)

        self.include = QPushButton('Include' , self)
        self.include.setObjectName("include")
        self.include.setGeometry(800, 0, 200, 50)
        self.include.clicked.connect(self.solve)

        
        self.A = QLineEdit(self)
        self.A.setGeometry(90, 200, 200, 50)
        self.A.setFocus()
        self.A.setPlaceholderText('Write set A')

        self.B = QLineEdit(self)
        self.B.setGeometry(90, 300, 200, 50)
        self.B.setPlaceholderText('Write set B')


        self.swap = QPushButton('Swap' , self)
        self.swap.setObjectName("swap")
        self.swap.setGeometry(90, 400, 200, 50)
        self.swap.clicked.connect(self.toswap)

        # Result widget
        self.result = QLabel(self)
        self.result.setObjectName("result")
        self.result.setGeometry(450, 150, 400, 300)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setVisible(False)

    def toswap(self):
        temp = self.A.text()
        self.A.setText(self.B.text())
        self.B.setText(temp)

    def convert(self):
        A = self.A.text().split(' ')
        B = self.B.text().split(' ')

        A = list(filter(None, A))
        B = list(filter(None, B))

        A = list(set(A))
        B = list(set(B))

        print(A)
        print(B)

        return A, B

    def solve(self):
        action = self.sender().objectName()
        A, B = self.convert()
        
        if action == 'union':
            res = self.sets.union(A, B)
        elif action == 'intersection':
            res = self.sets.intersection(A, B)
        elif action == 'difference':
            res = self.sets.difference(A, B)
        elif action == 'symmetrical_difference':
            res = self.sets.symmetrical_difference(A, B)
        elif action == 'include':
            res = self.sets.include(A, B)
        
        if type(res) != list:
            if res == True:
                result = f"<h2>RESULT</h2><p>A included in B</p>"
            else:
                result = f"<h2>RESULT</h2><p>A isn`t included in B</p>"
        else:
            res = sorted(res)
            result = f"<h2>RESULT</h2><p>{' '.join(res)}</p>"
        self.result.setText(result)
        self.result.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

