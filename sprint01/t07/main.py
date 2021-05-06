from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, \
                            QFileDialog, QPlainTextEdit, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette, QBrush
from PyQt5 import QtCore
import numpy as np
import re
import sys
import copy
# Methods from previous tasks
from methods import Method


class ErrorWindow(QWidget):
    

    def __init__(self):
        super().__init__()
        
    
    def show(self, message):      
        self.setGeometry(600, 400, 320, 200)
        QMessageBox.question(self, 'Alert', message, QMessageBox.Ok)
        


class Window(QWidget):

    def __init__(self, error):
        super().__init__()

        self.error = error
        self.solve_method = Method()

        self.setObjectName("main")
        self.setWindowTitle("Solving of Systems of linear equations")
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
        self.result.setGeometry(450, 150, 400, 350)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setVisible(False)

        self.check = QPushButton('Check it' , self)
        self.check.setObjectName("checkit")
        self.check.setGeometry(575, 550, 150, 35)
        self.check.clicked.connect(self.checkit)
        self.check.setVisible(False)


    def checkit(self):
        if self.check.text() == 'Check it':
            self.result.setText(self.checkup_data)
            self.check.setText('Back')
        else:
            self.result.setText(self.result_data)
            self.check.setText('Check it')


    def convert(self, temp):
        matrix, vector = [], []
        # print(temp)
        for i in range(len(temp) - 1):
            if re.search(r'[0-9]', temp[i]):
                matrix += [temp[i].split(' ')]

        # print(matrix)
        for i in range(len(matrix)):
            if '' in matrix[i]:
                matrix[i].remove('')

        # print(matrix)        
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
        try:
            text = self.line.toPlainText() + '\n'
            if re.search(r'[0-9]', text) == None:
                return self.error.show('Please input matrix!')    
            if re.search(r'[^0-9\-]', text) == None:
                return self.error.show('Invalid input!')    
            temp = text.split('\n')
        except Exception as e:
            print(e)
            return self.error.show('Unable to read matrix')
                

        try:       
            matrix, vector = self.convert(temp)
        except Exception as e:
            print(e)
            return self.error.show('Invalid matrix')
            
        if self.solve_method.degeneracy(matrix, vector) == False:       
            return self.error.show('Matrix is degeneracy')
        # print(np.matrix(matrix))
        # print(np.matrix(vector))
        method = self.sender().objectName()
        print(matrix)
        if matrix is not None:
            status, result = self.route(copy.deepcopy(matrix), copy.deepcopy(vector), method, len(matrix)) 
        print(result)
        # Show mistake
        if status != True:
            return self.error.show(result)

        

        string = f'<h1>{method.upper()}</h1><h3>Roots:</h3>'
        for i in range(len(result)):
            string += f'<p>x<sub>{i}</sub> = {result[i]} </p>'
        
        # Data that show after solving of SLAE
        self.result_data = string
        self.checkup_data = self.checking(matrix, vector, result)

        # Setting string in label that show roots of SLAE
        self.result.setText(self.result_data)
        self.result.setVisible(True)
        self.check.setVisible(True)       


    def file_open(self):

        path = QFileDialog(self).getOpenFileName()[0]
        if path == '':
            return False

        p = path.split('/')
        title = '.../' + p[len(p) - 1]
        self.file.setText(title)

        # Set text from file to textarea
        try:
            text = open(path, 'r+').read()      
            while text[0] != '\n':
                text = text[1:]
            text = text[1:]
        except Exception as e:
            print(e)
            return self.error.show('Unable to open file')

        self.line.setPlainText(text)   


    def checking(self, matrix, vector, roots):
        print(matrix, vector, roots)
        print(self.solve_method.checking(matrix, vector, roots))
        string = '<h2>Checking</h2>'
        for i in range(len(matrix)):
            string += '<p>'
            for j in range(len(matrix[i])):
                if j != 0:
                    string += ' + '
                string += f'{matrix[i][j]}*{roots[j]}'  
                      
            string += f' = {vector[i]}</p>'
        return string


    def route(self, matrix=None, vector=None, method=None, size=None):

        if method == 'cramer':
            if size > 3:
                return False, 'Size of matrix is too big to use Cramer`s method'
            return self.solve_method.cramer(matrix, vector)
        elif method == 'gauss':
            return self.solve_method.gauss(matrix, vector)
        elif method == 'seidel':
            return self.solve_method.seidel(matrix, vector)
        elif method == 'jordan-gauss':
            return self.solve_method.jordan_gauss(matrix, vector)
        elif method == 'jacobi':
            return self.solve_method.jacobi(matrix, vector)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    error = ErrorWindow()
    window = Window(error)
    window.show()
    sys.exit(app.exec_())

