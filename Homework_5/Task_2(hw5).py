# 2 Создайте программу для игры в ""Крестики-нолики"".

print("Let's play Tic-tac-toe")


field = [1,2,3,4,5,6,7,8,9]
def print_field (list):
      print(field[0], ' ', field [1], ' ', field[2])
      #print (' ')
      print(field[3], ' ', field[4], ' ', field[5])
      #print(' ')
      print(field[6], ' ', field[7], ' ', field[8])
      #print(' ')

print_field(field)

count = 1

for k in range(1,9):
      if (field[0]==field[1]==field[2]) \
            or (field[3]==field[4]==field[5])\
            or (field[6]==field[7]==field[8])\
            or (field[0]==field[3]==field[6])\
            or (field[1]==field[4]==field[7])\
            or (field[2]==field[5]==field[8])\
            or (field[0]==field[4]==field[8])\
            or (field[2]==field[4]==field[6]):
            print ('The game is over.')
            print(' ')
            print_field(field)
            break

      elif count%2==True:
            print('Please enter the number to replace with the 0.')
            l = int(input('Number for 0: '))
            if l in field:
                  i = field.index(l)
                  field[i] = '0'
                  count +=1
                  print('Move: ', count)
                  print_field(field)
            else:
                  print('The place is taken. Please choose another one')


      else:
            print('Please enter the number to replace with the X.')
            l = int(input('Number for X: '))
            if l in field:
                  i = field.index(l)
                  field[i] = 'X'
                  count += 1
                  print('Move: ', count)
                  print_field(field)
            else:
                  print('The place is taken. Please choose another one')
