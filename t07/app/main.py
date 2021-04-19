import sys, random
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, \
                            QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QLabel, QPushButton, \
                            QDesktopWidget, QFrame, QFileDialog, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QTransform, QBrush, QColor, QPen, QCursor, QIcon, QImage, QPalette, QDrag
from PyQt5 import QtCore
from methods import Method



class Window(QMainWindow):

    __method = None

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
        self.__interface()

    def __interface(self):
        # Background
        img = QImage("../assets/images/city.webp")
        sImage = img.scaled(QtCore.QSize(1000, 650))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Buttons
        self.cramer = QPushButton('Cramer' , self)
        self.cramer.setObjectName("cramer")
        self.cramer.setGeometry(0, 0, 200, 50)
        self.cramer.clicked.connect(self.__clicker)

        self.gauss = QPushButton('Gauss' , self)
        self.gauss.setObjectName("gauss")
        self.gauss.setGeometry(200, 0, 200, 50)
        self.gauss.clicked.connect(self.__clicker)

        self.seidel = QPushButton('Seidel' , self)
        self.seidel.setObjectName("seidel")
        self.seidel.setGeometry(400, 0, 200, 50)
        self.seidel.clicked.connect(self.__clicker)

        self.jordan_gauss = QPushButton('Jordan-Gauss' , self)
        self.jordan_gauss.setObjectName("jordan-gauss")
        self.jordan_gauss.setGeometry(600, 0, 200, 50)
        self.jordan_gauss.clicked.connect(self.__clicker)

        self.jacobi = QPushButton('Jacobi' , self)
        self.jacobi.setObjectName("jacobi")
        self.jacobi.setGeometry(800, 0, 200, 50)
        self.jacobi.clicked.connect(self.__clicker)

        
        self.line = QPlainTextEdit(self)
        self.line.setGeometry(90, 200, 200, 80)
        self.line.setFocus()
        self.line.setPlaceholderText('Write matrix in extended format')
        


        self.file = QPushButton('Choose file' , self)  
        self.file.setObjectName("file")
        self.file.setAcceptDrops(True)
        self.file.setGeometry(90, 400, 200, 50)
        self.file.clicked.connect(self.__file_open)

        self.submit = QPushButton('Solve it' , self)  
        self.submit.setObjectName("solve")
        self.submit.setGeometry(90, 500, 200, 50)
        # self.submit.setVisible(False)
        # self.submit.
        self.submit.clicked.connect(self.__solve)

        

    def __clicker(self, event):
        self.__method = self.sender().objectName()


    def __solve(self):
        if self.__method == None and self.file_path:
            text = open(self.file_path, 'r+').read()

            matrix = text.split('\n')
            vector = matrix[len(matrix) - 1]
            matrix.pop(len(matrix) - 1)

            for i in range(0, len(matrix)):
                matrix[i] = matrix[i].split(' ')
            
            # for i in range(0, matrix):
            #     for j in range(0, matrix[i]):
            #         if (matrix[i][j] == ''):
            #            matrix.remove(matrix[i][j])     
            print(vector)
            print(matrix)
        else:
            text = self.line.toPlainText()
            print(text)

    def __file_open(self):
        self.file_path = QFileDialog(self).getOpenFileName()[0]
        path = self.file_path.split('/')
        title = '.../' + path[len(path) - 1]
        self.file.setText(title)
        # self.submit.
        self.submit.setVisible(True)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()

