"""
 ___ ____ __
|_ _|_ _/ __|
 | | | | (__
 |_||___\___|
 ___  _    __
|_ _|/_\ / __|
 | |/ _ \ (__
 |_/_/  \_\___|
 ___ ___ ___
|_ _| _ | __|
 | |||_|| _|
 |_||___|___|
"""
#FIVE DIFFERENT BOTS AND TWO-PLAYER MODE!
import random
class square:
  def __init__(self, x, y):
    self.x=x
    self.y=y
    self.shape='-'
    self.occupied=False
sq1=square(0,0)
sq2=square(1,0)
sq3=square(2,0)
sq4=square(0,1)
sq5=square(1,1)
sq6=square(2,1)
sq7=square(0,2)
sq8=square(1,2)
sq9=square(2,2)
sqList=[sq5, sq1, sq3, sq7, sq9, sq2, sq4, sq6, sq8]
board=[[sq1, sq2, sq3],[sq4, sq5, sq6],[sq7, sq8, sq9]]
win_possibilities=[[sq1, sq2, sq3],[sq4, sq5, sq6],[sq7, sq8, sq9],[sq1, sq4, sq7],[sq2, sq5, sq8],[sq3, sq6, sq9],[sq1, sq5, sq9],[sq3, sq5, sq7]]
#fundamental functions to print board, occupy square, map player input to square, etc.
def print_board():
  for i in board:
    print(f"{i[0].shape}|{i[1].shape}|{i[2].shape}")
    print("-----")
def check_win(multiplayer, p1_shape):
  for i in win_possibilities:
    if i[0].shape==i[1].shape and i[1].shape==i[2].shape:
      if i[0].shape==p1_shape:
        if multiplayer=='y':
          print("Player 1 wins!")
        else:
          print("You win!")
      else:
        if multiplayer=='y':
          print("Player 2 wins!")
        else:
          print("Bot wins!")
      return True
  return False
def check_tie():
  for sq in sqList:
    if not sq.occupied:
      return False
  if not check_win():
    print("It's a tie!")
    return True
def occupy(square, shape):
  square.shape=shape
  square.occupied=True
def input2square(input):
  if input=='1':
    move_sq=sq1
  elif input=='2':
    move_sq=sq2
  elif input=='3':
    move_sq=sq3
  elif input=='4':
    move_sq=sq4
  elif input=='5':
    move_sq=sq5
  elif input=='6':
    move_sq=sq6
  elif input=='7':
    move_sq=sq7
  elif input=='8':
    move_sq=sq8
  elif input=='9':
    move_sq=sq9
  else:
    move_sq=""
  return move_sq
def update_sqList():
  global sqList
  sqList[0]=sq5
  sqList[1]=sq1
  sqList[2]=sq3
  sqList[3]=sq7
  sqList[4]=sq9
  sqList[5]=sq2
  sqList[6]=sq4
  sqList[7]=sq6
  sqList[8]=sq8
def update_square(move_sq):
  global sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9
  if move_sq.x==0:
    if move_sq.y==0:
      sq1=move_sq
    elif move_sq.y==1:
      sq4=move_sq
    else:
      sq7=move_sq
  elif move_sq.x==1:
    if move_sq.y==0:
      sq2=move_sq
    elif move_sq.y==1:
      sq5=move_sq
    else:
      sq8=move_sq
  else:
    if move_sq.y==0:
      sq3=move_sq
    elif move_sq.y==1:
      sq6=move_sq
    else:
      sq9=move_sq
  update_sqList()
#functions for different bot strats
def random_move(bot_shape):
  rand_sqs=sqList
  for i in len(rand_sqs):
    sq=rand_sqs[random.randint(0, len(rand_sqs)-1)]
    rand_sqs.remove(sq)
    if not sq.occupied:
      occupy(sq, bot_shape)
      return
def find_good_square(bot_shape):
  for sq in sqList:
    if not sq.occupied:
      occupy(sq, bot_shape)
def find_threat(p_shape):
  for i in win_possibilites:
    cond_1=(i[0].shape==i[1].shape and i[0]==p_shape)
def claim_win(bot_shape):
  for i in win_possibilities:
    cond_1=(i[0].shape==i[1].shape and i[0].shape==bot_shape)
#This is the game
def player_move(p_shape):
  p_move=input("Player 1: enter the square number for your move: ")
  move_sq=input2square(p_move)
  while move_sq not in sqList:
    p_move=input("Please enter a valid square number: ")
    move_sq=input2square(p_move)
  while move_sq.occupied:
    p_move=input("That square is occupied. Try another square.")
    move_sq=input2square(p_move)
    while move_sq not in sqList:
      p_move=input("Please enter a valid square number: ")
      move_sq=input2square(p_move)
  occupy(move_sq, p_shape)
  update_square(move_sq)
def game():
  global sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9
  player_shape=input("Do you want to play as 'X' or 'O'? ")
  two_p=input("""Are you playing a two-player game?('y')
  Otherwise, you will play a bot.""")
  if player_shape=='X' or player_shape=='x':
    player_shape='X'
    otherP_shape='O'
  else:
    player_shape='O'
    otherP_shape='X'
  if two_p!='y':
    bot_lvl=input("""Select the level of the bot (1/2/3/4/5):
    1. Dummy.1: Just chooses random squares. SUPER EASY.
    2. Dummy.2: Tries to choose squares that are considered 'better'(centers or corners). SUPER EASY.
    3. Logical: Chooses moves that make sense, but can fall for traps. MEDIUM.
    4. Defensive: Won't let you win. HARD.
    5. Boss: Will beat you up if you make the slightest mistake. IMPOSSIBLE.\n""")
    while bot_lvl not in ['1', '2', '3', '4', '5']:
      bot_lvl=input("Please enter a valid level number (1/2/3/4/5):\n")
  move_num=1
  while not check_win(two_p, player_shape):
    print("Current board:")
    print_board()
    if move_num%2==1:
      print("Player 1:")
      player_move(player_shape)
    else:
      if two_p=='y':
        print("Player 2:")
        player_move(otherP_shape)
      else:
        if bot_lvl='1':
          random_move(otherP_shape)
        elif bot_lvl='2':
          find_good_square(otherP_shape)
        elif bot_lvl='3':
          
print("""1|2|3
-----
4|5|6
-----
7|8|9""")
print("""Instructions:
Enter the corresponding number on the board above
to place your piece on that square.""")
