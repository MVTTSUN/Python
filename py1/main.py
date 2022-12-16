import math

# 1
def is_holiday(number):
  print(f'{number} - это выходной день?')
  if number >= 6 and number <= 7:
    print('да')
  elif number >= 1 and number <= 5:
    print('нет')
  else:
    print('введите число от 1 до 7')

is_holiday(7)

# 2
def is_truth(rows):
  print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
  for i in range(rows):
    x = round(int(bin(i)[2:len(bin(i))]) / 100)
    y = round(int(bin(i)[2:len(bin(i))]) / 10 % 10)
    z = int(bin(i)[2:len(bin(i))]) % 10
    result = not (x or y or z) == (not x and not y and not z)
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} | {result}')
    
is_truth(8)

# 3
def get_term(x, y):
  print(f'Координаты x = {x}, y = {y}. Где на координатной плоскости расположена точка?')
  if x > 0 and y > 0:
    print('1 четверть')
  elif x < 0 and y > 0:
    print('2 четверть')
  elif x < 0 and y < 0:
    print('3 четверть')
  elif x > 0 and y < 0:
    print('4 четверть')
  elif x == 0 and y != 0:
    print('лежит на оси x')
  elif x != 0 and y == 0:
    print('лежит на оси y')
  else:
    print('лежит на пересечении оси x и y')

get_term(34, -30)

# 4
def get_coordinates(number):
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

get_coordinates(3)

# 5
def find_2d_distance(a, b):
  print(f'Точка А ({a[0], a[1]}), точка B ({b[0], b[1]}). Расстояние между точками А и В:')
  print(math.sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2)))

find_2d_distance([7, -5], [1, -1])