import sys, random
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag
from PyQt5 import QtCore
from methods import Method



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.solve = Method()
        # self.setObjectName("main")
        self.setWindowTitle("Solving of Systems of linear equations")
        self.setWindowIcon(QIcon('../assets/images/icon.png'))
        self.setStyleSheet(open('../assets/css/style.css').read())
        self.setMinimumSize(1000, 650)
        self.setMaximumSize(1000, 650)
        self.setGeometry(300, 100, 800, 600)
        self.interface()

    def interface(self):
        # Background
        img = QImage("../assets/images/city.webp")
        sImage = img.scaled(QtCore.QSize(1000, 650))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Buttons
        self.cramer = QPushButton('Cramer' , self)
        self.cramer.setGeometry(0, 0, 200, 50)
        self.cramer.clicked.connect(self.clicker)

        self.gauss = QPushButton('Gauss' , self)
        self.gauss.setGeometry(200, 0, 200, 50)
        self.gauss.clicked.connect(self.clicker)

        self.seidel = QPushButton('Seidel' , self)
        self.seidel.setGeometry(400, 0, 200, 50)
        self.seidel.clicked.connect(self.clicker)

        self.jordan_gauss = QPushButton('Jordan-Gauss' , self)
        self.jordan_gauss.setGeometry(600, 0, 200, 50)
        self.jordan_gauss.clicked.connect(self.clicker)

        self.jacobi = QPushButton('Jacobi' , self)
        self.jacobi.setGeometry(800, 0, 200, 50)
        self.jacobi.clicked.connect(self.clicker)

        
        self.line = QPlainTextEdit(self)
        self.line.setGeometry(90, 200, 200, 80)
        self.line.setPlaceholderText('Write matrix...')
        # self.line.

        self.file = QPushButton('Choose file' , self)  
        self.file.setObjectName("file")
        self.file.setGeometry(90, 400, 200, 50)
        self.file.clicked.connect(self.file_open)

        self.submit = QPushButton('Solve it' , self)  
        self.submit.setObjectName("solve")
        self.submit.setGeometry(90, 500, 200, 50)
        self.submit.setVisible(False)
        # self.file.clicked.connect(self.solve)

        

    def clicker(self):
        print('Clicked')

    def file_open(self):
        self.file_path = QFileDialog(self).getOpenFileName()[0]
        path = self.file_path.split('/')
        title = '.../' + path[len(path) - 1]
        self.file.setText(title)
        self.submit.setVisible(True)


def main():
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()

