class alMatric():
    def __init__(self):
        self.matrices = []
        self.row = 0
        self.col = 0
        self.notsizedef = True
        self.n = 0
        self.counter = 0
        
    # Method for get Each matrix
    def getMatrix(self,rows,cols):
        self.n +=1
        tempRow = []
        for row in range(rows):
            tempCol =[]
            for col in range(cols):
                l = int(input("Element : ({0},{1}) ".format(row+1,col+1)))
                tempCol.append(l)
            tempRow.append(tempCol)
        matric = tempRow
        return matric
    
    # Method For Adding Matrix in List 
    def putData(self,div=False):
        if div:
            row = int(input("\nNo. OF ROWS : "))
            col = int(input("No. OF COLS : "))
            print("\n")
            self.matrices.append([self.getMatrix(row,col),[row,col]])
        else:
            if self.notsizedef:
                self.row = int(input("No. OF ROWS : "))
                self.col = int(input("No. OF COLS : "))
                print("\n")
                self.matrices.append(self.getMatrix(self.row,self.col))
                self.notsizedef = False
            else:
                print("\n")
                self.matrices.append(self.getMatrix(self.row,self.col))

    # Method TO display all existing Matrix in List
    def dispData(self):
        print("\n")
        for count,matrix in enumerate(self.matrices,start=1):
            print(count,end="\t")
            print(matrix)
            

    # Method for addition
    def matrixAdd(self):
        try:
            temprow = []
            for i in range(self.row):
                tempcol =[]
                for j in range(self.col):
                    sum=0
                    for s in range(self.n):
                        sum += self.matrices[s][i][j]
                    tempcol.append(sum)
                temprow.append(tempcol)
                
            return temprow
        except:
            self.matrices =[]
            self.matrixAdd()

    # Method for Subtraction
    def matrixSub(self):
        try:
            temprow = []
            for i in range(self.row):
                tempcol =[]
                for j in range(self.col):
                    sum=0
                    flag = 1
                    for s in range(self.n):
                        if flag == 1:
                            sum += self.matrices[s][i][j]
                            flag +=1
                        else:
                            sum -= self.matrices[s][i][j]
                    tempcol.append(sum)
                temprow.append(tempcol)
            return temprow
        except:
            self.matrices=[]
            self.matrixSub()

    # Method for Multiplication
    def matrixMul(self,matA,matB):
        matres = []
        for row in range(matA[1][0]):
            temprow=[]
            for col in range(matB[1][1]):
                sum = 0
                for cond in range(matA[1][1]):
                    print(f"{matA[0][row][cond]} * {matB[0][cond][col]}")
                    sum += matA[0][row][cond] * matB[0][cond][col]

                print("\n")
                temprow.append(sum)  
            matres.append(temprow)

        return matres


    # GET matrices for multiplication
    def getData_mul(self):
        try : 
            self.matrices = []
            self.putData(div=True)
            self.putData(div=True)
            mainMul = self.matrixMul(self.matrices[0],self.matrices[1])

            return mainMul
        
        except:
            print("wrong order of matrix or more than 2 matrix are store")
            print(self.dispData())
            self.getData_mul()
            
    # GET Transpose of matrix
    def transpose(self):
        inp = int(input("\nIndex of Matrix : "))
        mat = self.matrices[inp-1]
        for i in range(self.row):
            for j in range(i+1):
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
        return mat


