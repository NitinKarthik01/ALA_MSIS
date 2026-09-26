
class Matrix :
    def __init__(self,rows):
        self.rows = [list(row) for row in rows]
        self.num_rows = len(rows)
        if self.num_rows>0 :
            self.num_col = len(self.rows[0])

            for x in self.rows:
                if len(x) != self.num_col:
                    raise ValueError("All rows must have the same number of columns") 
        # print(self.rows,self.num_rows,self.num_col)


    def __add__(self,other):
        if self.num_col != other.num_col or self.num_rows != other.num_rows :
            raise ValueError("Matrices must have the same dimensions")

        result = []
        for i in range(self.num_rows) :
            row = []
            for j in range(other.num_col):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.append(row)

        return Matrix(result)


    def __iadd__(self,other):
        if self.num_col != other.num_col or self.num_rows != other.num_rows :
            raise ValueError("Matrices must have the same dimensions")

        result = []
        for i in range(self.num_rows) :
            row = []
            for j in range(other.num_col):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.append(row)

        return Matrix(result)


    def __sub__(self,other):
        if self.num_col != other.num_col or self.num_rows != other.num_rows :
            raise ValueError("Matrices must have the same dimensions")

        result = []
        for i in range(self.num_rows) :
            row = []
            for j in range(other.num_col):
                row.append(self.rows[i][j] - other.rows[i][j])
            result.append(row)

        return Matrix(result)

    
    def __mul__(self,other):
        if self.num_col != other.num_rows :
            raise ValueError("Matrices of this dimension cant be multiplied")
        
        result = []
        for i in range(self.num_rows) :
            row = []
            for j in range(other.num_col):
                sum = 0
                for k in range(other.num_rows):
                    sum += self.rows[i][k] * other.rows[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[1,2,3],[12,23,34]])
print(matrix1)


matrix2 = Matrix([[1,2,5],[4,10,11]])
print(matrix2)


matrix1+=matrix2
print(matrix1)


matrix3 = Matrix([[1,3,5],[7,10,100],[1,7,0]])
print(matrix3)

matrix_add = matrix1+matrix2
matrix_sub = matrix1-matrix2
matrix1*=matrix3
print(matrix1)