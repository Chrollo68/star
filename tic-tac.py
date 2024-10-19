board=['' for _ in range(9)]

def print_board(board):
     for row in [board[i*3:(i+1)*3]for i in range(3)]:
          print('|'.join(row))
          print('-'*5)

def check_win(board,player):
     win_conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
     for condition in win_conditions:
          if board[condition[0]]==board[condition[1]]==board[condition[2]]==player:
               return True
     return False

def minimax(board,depth,is_maximizing):
     if check_win(board,'X'):
          return 1
     elif check_win(board,'O'):
          return -1
     elif '' not in board:
          return 0
     if is_maximizing:
          best_score=-float('inf')
          for i in range(9):
               if board[i]=='':
                    board[i]='X'
                    score=minimax(board,depth+1,False)
                    board[i]=''
                    best_score=max(score,best_score)
          return best_score
     else:
          best_score=float('inf')
          for i in range(9):
               if board[i]=='':
                    board[i]='O'
                    score=minimax(board,depth+1,True)
                    board[i]=''
                    best_score=min(score,best_score)
          return best_score
     
def ai_move(board):
     best_score=-float('inf')
     move=0
     for i in range(9):
          if board[i]=='':
               board[i]='X'
               score=minimax(board,0,False)
               board[i]=''
               if score>best_score:
                    best_score=score
                    move=i
     board[move]='X'

def play_game():
     while True:
          print_board(board)
          if check_win(board,'X'):
               print("X wins!")
               break
          elif check_win(board,'O'):
               print("O wins!")
               break
          elif '' not in board:
               print("Its a tie!")
               break
          move = int (input("Enter your move(1-9)"))-1
          if board[move]=='':
               board[move]='O'
          else:
               print("Invalid move try again.")
               continue
          ai_move(board)

play_game()

