import os
import msvcrt

def updateUI():
  global field
  os.system('cls')
  for i in range(len(field)):
    for j in range(len(field[i])):
        print(field[i][j], end=' ')
    print()

x = 20
y = 20
field = [[0]*x for i in range(y)]
for i in range(len(field)):
  for j in range(len(field[i])):
      if i==0 or i==x-1:
        field[i][j] = '@'
      elif j==0 or j==y-1:
        field[i][j] = '@'
      else:
        field[i][j] = '·'

head_x = 1
head_y = 1
tail = (0,1)
dirrection = 'left'
        
updateUI()
while True:
  key = ord(msvcrt.getch()) #читаем нажатую клавишу
  field[head_x][head_y] = 'o'
  if key == 72:#up
    head_x -=1
  elif key == 80:#down
    head_x +=1
  elif key == 75: #left
    head_y -=1
  elif key == 77: #right
    head_y +=1
  field[head_x][head_y] = 'O'
  updateUI()

  if head_x == 0 or head_x==x-1 or head_y == 0 or head_y==y-1:
    print('лох')
    break

    

