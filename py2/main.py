import random

# 1
def get_sum_nums_of_num(num):
  result = 0
  if type(num) == int or float:
    num = str(num)
    num = num.replace('.', '')
    num = num.replace(',', '')
  for i in num:
    result += int(i)
  print(result)

get_sum_nums_of_num(67.82)

#2
def get_sub_fact(n):
  count = 1
  for i in range(n):
    count = count * (i + 1)
    print(count, end = ' ')
  print()

get_sub_fact(4)

#3
def get_sub_form(n):
  my_list = []
  sum = 0
  for i in range(n):
    my_list.append((1 + 1/(i + 1))**(i + 1))
    sum += (1 + 1/(i + 1))**(i + 1)
  print(my_list, sum)

get_sub_form(4)

#4
def shuffle_list(my_list):
  random.shuffle(my_list)
  print(my_list)

shuffle_list([1, 3, 98])