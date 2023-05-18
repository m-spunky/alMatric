class alMatric():
    def __init__(self):
        self.matrices = []
        self.row = 0
        self.col = 0
        self.notsizedef = True
        self.n = 0
        
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
    def putData(self):
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
   
    # Method for Subtraction
    def matrixSub(self):
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


            


