class LPParser:
    def __init__(self, matrix, start_node, term_node, type, fun, data_t):
        self.start_point, self.termination_point = start_node, term_node
        self.max_graph_size = 18
        self.type_of_graph = type
        self.function = fun
        self.fun_statement = ""
        self.data_type = data_t
        self.bounds = [''] * self.max_graph_size
        self.variables = [''] * self.max_graph_size
        # self.matrix = matrix
        self.matrix = [[0, 1, 1, 0, 0], [0, 0, 0, 8, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        self.size_of_graph = len(matrix)
        self.others_matrix = []
        for i in range(0, self.size_of_graph):
            temp = []
            for j in range(0, self.max_graph_size):
                temp.append('')
            self.others_matrix.append(temp)

        print(self  .others_matrix)

    def convertIntToLetter(self, value):
        return chr(value + 97)

    def getVariables(self, matrix):
        k = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                j = j + i
                if j < len(matrix):
                    if i is not j:
                        self.variables[k] = self.convertIntToLetter(i) + "_" + self.convertIntToLetter(j)
                        k += 1

        lenm = len(self.variables)
        while lenm > 0:
            lenm -= 1
            if self.variables[lenm] is '':
                self.variables = self.variables[:-1]

    def printMatrixFunction(self, matrix):
        fun = ""
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if matrix[i][j] is not 0:
                    if matrix[i][j] is 1:
                        fun += self.convertIntToLetter(i) + "_" + self.convertIntToLetter(j) + " + "
                    else:
                        fun += str((matrix[i][j]))
                        fun += self.convertIntToLetter(i) + "_" + self.convertIntToLetter(j) + " + "
        fun = fun[:-2]
        return fun

    def parseMatrixToCode(self, matrix):

        column_i = 0
        column_j = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if matrix[i][j] is not 0:
                    if column_i > 0 and self.others_matrix[i][column_i - 2] is '':
                        column_i -= 2
                    if column_j > 0 and self.others_matrix[j][column_j - 2] is '':
                        column_j -= 2

                    self.others_matrix[i][column_i], self.others_matrix[i][column_i + 1] = "+", \
                                                                                           self.convertIntToLetter(
                                                                                               i) + "_" + self.convertIntToLetter(
                                                                                               j)
                    self.others_matrix[j][column_j], self.others_matrix[j][column_j + 1] = "-", \
                                                                                           self.convertIntToLetter(
                                                                                               i) + "_" + self.convertIntToLetter(
                                                                                               j)
                    column_i += 2
                    column_j += 2

    def repairMatrix(self):

        for i in range(0, len(self.others_matrix)):
            for j in range(0, len(self.others_matrix)):
                if self.others_matrix[i][0] is "+":
                    self.others_matrix[i][0] = ""

        elements = len(self.others_matrix[0])
        while elements > 0:
            elements -= 1
            for i in range(0, len(self.others_matrix)):
                for j in range(0, len(self.others_matrix[i]) - 1):
                    if self.others_matrix[i][j] is '':
                        self.others_matrix[i][j], self.others_matrix[i][j + 1] = \
                            self.others_matrix[i][j + 1], self.others_matrix[i][j]

        for i in range(0, len(self.others_matrix)):
            lenm = len(self.others_matrix[i])
            while lenm > 0:
                lenm -= 1
                if self.others_matrix[i][lenm] is '':
                    self.others_matrix[i] = self.others_matrix[i][:-1]

        for i in range(0, len(self.others_matrix)):
            if i is 0:
                self.bounds[i] = ' '.join(self.others_matrix[i]) + " = 1"
                print(' '.join(self.others_matrix[i]) + " = 1")
            elif i is len(self.others_matrix) - 1:
                self.bounds[i] = ' '.join(self.others_matrix[i]) + " = -1"
                print(' '.join(self.others_matrix[i]) + " = -1")
            else:
                self.bounds[i] = ' '.join(self.others_matrix[i]) + " = 0"
                print(' '.join(self.others_matrix[i]) + " = 0")

    def prepareToWrite(self):
        self.fun_statement = self.printMatrixFunction(self.matrix)
        self.parseMatrixToCode(self.matrix)
        self.repairMatrix()
        self.getVariables(self.matrix)
        self.writeToFile()

    def writeToFile(self):
        with open('test_file.lp', 'w') as file:
            file.truncate()
            file.write('/* Objective function */\n')
            file.write(self.function + ': ')
            file.write(self.fun_statement + ';\n\n')
            file.write('/* Variable bounds */ \n\n')

            for i in range(0, len(self.bounds)):
                file.write(self.bounds[i] + '\n')

            file.write(self.data_type + ": ")
            file.write(', '.join(self.variables))
            file.write(";\n")

        file.close()

    def run(self):
        self.prepareToWrite()


matrix = [[0, 1, 1, 0, 0], [0, 0, 0, 8, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
LPParser(matrix, 1, 5, "un", "min", "bin").run()
