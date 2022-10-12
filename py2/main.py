import re

#1
def list_fact(n):
  list = []
  cnt = 1
  for i in range(1, n + 1):
    cnt *= i
    list.append(cnt)
  print(list)

list_fact(4)

#2
def table_true(rows):
  print(f'X Y Z ¬(X∧Y)∨Z')
  for i in range(0, rows):
    one_column = round(int(bin(i)[2:len(bin(i))]) / 100)
    two_column = round(int(bin(i)[2:len(bin(i))]) / 10 % 10)
    three_column = int(bin(i)[2:len(bin(i))]) % 10
    four_column = (not(one_column and two_column)) or three_column
    print(f'{one_column} {two_column} {three_column} {bool(four_column)}')

table_true(8)

#3
def count_match(one_string, two_string):
  for i in range(0, len(one_string)):
    print(f'{one_string[i]} - {len(re.findall(one_string[i], two_string))}', end = ' ')
  print()

count_match('one', 'onetwonine')

#4
def shift_position(n):
  list = []
  for i in range(-n, n + 1):
    list.append(i)
  #list = list[n:n+1]
  list.insert(0, list[len(list) - 1])
  list.insert(0, list[len(list) - 2])
  print(list[:len(list) - 2])

shift_position(3)