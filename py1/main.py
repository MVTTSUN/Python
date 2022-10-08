import math

#1
def day_week(number):
  if type(number) == int:
    number = str(number)
  match number:
    case '1':
      print('Понедельник')
    case '2':
      print('Вторник')
    case '3':
      print('Среда')
    case '4':
      print('Четверг')
    case '5':
      print('Пятница')
    case '6':
      print('Суббота')
    case '7':
      print('Воскресенье')
    case _:
      print('Нет такого дня')

day_week(3)

#2
def distance_in_2d(a, b):
  res = math.sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))
  print(res)

distance_in_2d([7, -5], [1, -1])

#3
def term(number):
  if type(number) == int:
    number = str(number)
  match number:
    case '1':
      print('x > 0, y > 0')
    case '2':
      print('x < 0, y > 0')
    case '3':
      print('x < 0, y < 0')
    case '4':
      print('x > 0, y < 0')
    case _:
      print('нет такой четверти')
      
term(4)

#4
def odd_numbers(n):
  for i in range(1, n + 1):
    if i % 2 == 0:
      print(i, end = ' ')

odd_numbers(7)