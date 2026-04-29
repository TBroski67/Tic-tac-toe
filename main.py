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
    if i[0].shape==i[1].shape and i[1].shape==i[2].shape and i[0].occupied:
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
def check_tie(two_p, p1_shape):
  for sq in sqList:
    if not sq.occupied:
      return False
  if not check_win(two_p, p1_shape):
    print("It's a tie!")
    return True
def occupy(square, shape):
  square.shape=shape
  square.occupied=True
def input2square(user_input):
    mapping = {'1': sq1, '2': sq2, '3': sq3, '4': sq4, '5': sq5, '6': sq6, '7': sq7, '8': sq8, '9': sq9}
    return mapping.get(user_input, "")
#functions for different bot strats
def random_move(bot_shape):
  rand_sqs=[sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]
  for i in range(len(rand_sqs)):
    sq=rand_sqs[random.randint(0, len(rand_sqs)-1)]
    rand_sqs.remove(sq)
    if not sq.occupied:
      occupy(sq, bot_shape)
      return
def find_good_square(bot_shape):
  for sq in sqList:
    if not sq.occupied:
      occupy(sq, bot_shape)
      return
def claim_win(bot_shape):
  for i in win_possibilities:
    cond_1=(i[0].shape==i[1].shape and i[0].shape==bot_shape and not i[2].occupied)
    cond_2=(i[0].shape==i[2].shape and i[0].shape==bot_shape and not i[1].occupied)
    cond_3=(i[1].shape==i[2].shape and i[1].shape==bot_shape and not i[0].occupied)
    if cond_1:
      occupy(i[2], bot_shape)
      return True
    elif cond_2:
      occupy(i[1], bot_shape)
      return True
    elif cond_3:
      occupy(i[0], bot_shape)
      return True
  return False
def find_threat(p_shape, bot_shape):
  for i in win_possibilities:
    cond_1=(i[0].shape==i[1].shape and i[0].shape==p_shape and not i[2].occupied)
    cond_2=(i[0].shape==i[2].shape and i[0].shape==p_shape and not i[1].occupied)
    cond_3=(i[1].shape==i[2].shape and i[1].shape==p_shape and not i[0].occupied)
    if cond_1:
      occupy(i[2], bot_shape)
      return True
    elif cond_2:
      occupy(i[1], bot_shape)
      return True
    elif cond_3:
      occupy(i[0], bot_shape)
      return True
  return False
#This is the game
def player_move(p_shape):
  p_move=input("Enter the square number for your move: ")
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
  while not (check_win(two_p, player_shape) or check_tie(two_p, player_shape)):
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
        if bot_lvl=='1':
          random_move(otherP_shape)
        elif bot_lvl=='2':
          find_good_square(otherP_shape)
        elif bot_lvl=='3':
          if not claim_win(otherP_shape):
            if not find_threat(player_shape, otherP_shape):
              find_good_square(otherP_shape)
    move_num+=1
print("""1|2|3
-----
4|5|6
-----
7|8|9""")
print("""Instructions:
Enter the corresponding number on the board above
to place your piece on that square.""")
game()
