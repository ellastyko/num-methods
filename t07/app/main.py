import sys
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, \
                            QFileDialog, QPlainTextEdit, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette, QBrush
from PyQt5 import QtCore
from methods import Method
import re
import html

class ErrorWindow(QWidget):
    

    def __init__(self):
        super().__init__()
        
    
    def show(self, message):      
        self.setGeometry(600, 400, 320, 200)
        QMessageBox.question(self, 'Alert', message, QMessageBox.Ok)
        


class Window(QWidget):

    solve_method = None
    file_path = None

    def __init__(self, error):
        super().__init__()

        self.error = error
        self.solve_method = Method()

        self.setObjectName("main")
        self.setWindowTitle("Solving of Systems of linear equations")
        self.setWindowIcon(QIcon('../assets/images/icon.png'))
        self.setStyleSheet(open('../assets/css/style.css').read())
        self.setMinimumSize(1000, 650)
        self.setMaximumSize(1000, 650)
        self.setGeometry(300, 100, 800, 600)

        self.initUI()
        

    def initUI(self):
        

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
        self.cramer.clicked.connect(self.__solve)

        self.gauss = QPushButton('Gauss' , self)
        self.gauss.setObjectName("gauss")
        self.gauss.setGeometry(200, 0, 200, 50)
        self.gauss.clicked.connect(self.__solve)

        self.seidel = QPushButton('Seidel' , self)
        self.seidel.setObjectName("seidel")
        self.seidel.setGeometry(400, 0, 200, 50)
        self.seidel.clicked.connect(self.__solve)

        self.jordan_gauss = QPushButton('Jordan-Gauss' , self)
        self.jordan_gauss.setObjectName("jordan-gauss")
        self.jordan_gauss.setGeometry(600, 0, 200, 50)
        self.jordan_gauss.clicked.connect(self.__solve)

        self.jacobi = QPushButton('Jacobi' , self)
        self.jacobi.setObjectName("jacobi")
        self.jacobi.setGeometry(800, 0, 200, 50)
        self.jacobi.clicked.connect(self.__solve)

        
        self.line = QPlainTextEdit(self)
        self.line.setGeometry(90, 200, 200, 80)
        self.line.setFocus()
        self.line.setPlaceholderText('Write matrix in extended format')


        self.file = QPushButton('Choose file' , self)  
        self.file.setObjectName("file")
        self.file.setAcceptDrops(True)
        self.file.setGeometry(90, 400, 200, 50)
        self.file.clicked.connect(self.file_open)



        # Result widget
        self.result = QLabel(self)
        self.result.setObjectName("result")
        self.result.setGeometry(450, 150, 400, 400)
        # layout = QVBoxLayout(self.result)
           

    def convert(self, temp):
        matrix, vector = [], []
        for i in range(len(temp) - 1):
            if temp[i] != '':
                matrix += [temp[i].split(' ')]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == int(len(matrix[i]) - 1):
                    vector.append(matrix[i][j])
                    matrix[i].pop(j)

        return matrix, vector
            
    # After submit of entered matrix
    def __solve(self):

        matrix, vector = [], []
        if self.file_path != None:
            # Обработка файла .txt
            try:
                text = open(self.file_path, 'r+').read()                 
                temp = text.split('\n') 
                temp.pop(0)
            except Exception as e:
                print(e)
                self.error.show('Unable to open file')
                return 
        else:
            try:
                text = self.line.toPlainText() + '\n'     
                temp = text.split('\n')
            except Exception as e:
                print(e)
                self.error.show('Unable to read matrix')
                return


        try:       
            matrix, vector = self.convert(temp)
        except Exception as e:
            self.error.show('Invalid matrix')
            return

        if self.solve_method.degeneracy(matrix, vector) == False:
            self.error.show('Matrix is degeneracy')
            return
        # print(np.matrix(matrix))
        # print(np.matrix(vector))
        if matrix is not None:
            result = self.route(matrix, vector, self.sender().objectName(), len(matrix)) 
        
        string = '<h3>Roots:</h3>'
        for i in range(len(result)):
            string += f'<p>x<sub>{i}</sub> = {result[i]} </p>'
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setText(string)
        print(result)
        


    def file_open(self):

        self.file_path = QFileDialog(self).getOpenFileName()[0]
        if self.file_path == '':
            self.file_path = None
            return False

        path = self.file_path.split('/')
        title = '.../' + path[len(path) - 1]
        self.file.setText(title)


    def route(self, matrix=None, vector=None, method=None, size=None):
        
        if method == 'cramer':
            if size > 3:
                return self.error.show('Size of matrix is too big to use Cramer`s method')
            return self.solve_method.cramer(matrix, vector)
        elif method == 'gauss':
            return self.solve_method.gauss(matrix, vector)
        elif method == 'seidel':
            return self.solve_method.seidel(matrix, vector)
        elif method == 'jordan_gauss':
            return self.solve_method.jordan_gauss(matrix, vector)
        elif method == 'jacobi':
            return self.solve_method.jacobi(matrix, vector)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    error = ErrorWindow()
    window = Window(error)
    window.show()
    sys.exit(app.exec_())

