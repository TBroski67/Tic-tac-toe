# Tic-tac-toe
class square:
  def __init__(self, x, y):
    self.x=x
    self.y=y
    self.shape='-'
    if x==1 and y==1:
      self.position='center'
    elif (x==1 and y!=1) or (x!=1 and y==1):
      self.position='edge'
    else:
      self.position='corner'
sq1=square(0,0)
sq2=square(1,0)
sq3=square(2,0)
sq4=square(0,1)
sq5=square(1,1)
sq6=square(2,1)
sq7=square(0,2)
sq8=square(1,2)
sq9=square(2,2)
board=[[sq1, sq2, sq3],[sq4, sq5, sq6],[sq7, sq8, sq9]]
def print_board():
  for i in board:
    print(f"{i[0].shape}|{i[1].shape}|{i[2].shape}")
    print("-----")
print("""1|2|3
-----
4|5|6
-----
7|8|9""")
print("""Instructions:
Enter the corresponding number on the board above
to place your piece on that square.""")
player_shape=input("Do you want to play as 'X' or 'O'? ")
if player_shape=='X' or player_shape=='x':
  player_shape='X'
  bot_shape='O'
else:
  player_shape='O'
  bot_shape='X'
print_board()
