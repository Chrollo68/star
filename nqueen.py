n=int(input(“Enter the number of queens”))

def displayBoard(board):
   for i in range(n):
      for j in range(n):
         print(board[i][j],end=" ")
      print()

def solveQueen(board,col):
   if(col == n):
      displayBoard(board)
      return True
   for i in range(n):
      if(isSafe(board,i,col)):
         board[i][col] = "🜲"
         if(solveQueen(board,col + 1)):
            return True
         board[i][col]="0"
   return False

def isSafe(board,row,col):
   for x in range(col):
      if(board[row][x]=="🜲"):
         return False
   for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
      if(board[x][y]=="🜲"):
         return False
   for x,y in zip(range(row,n,1),range(col,-1,-1)):
      if(board[x][y]=="🜲"):
         return False
   return True

board=list()
a=list()
board = []
k=0
for i in range(n):
   for j in range(n):
      a.append(0)
   board.append(a)
   a=[]
solveQueen(board,0)
