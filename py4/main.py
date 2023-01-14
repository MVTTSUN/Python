import math
import random

#1
def get_round_pi(d):
  if 10 ** -10 <= d <= 10 ** -1:
    print(round(math.pi, int(f'{d:e}'.split('-')[1])))

get_round_pi(10 ** -10)

#2
def get_mult_simple_list(number):
  my_list = []
  for i in range(2, number + 1):
    if number % i == 0:
      my_list.append(i)
  print(my_list)

get_mult_simple_list(15)

#3
def remove_repeat_numbers(my_list):
  unic_numbers = []
  for i in range(len(my_list)):
    if my_list.count(my_list[i]) == 1:
      unic_numbers.append(my_list[i])
  print(unic_numbers)

remove_repeat_numbers([1, 2, 4, 2, 5, 1, 6, 7])

#4
def get_k(k):
  my_list = []
  for i in range(k, 1, -1):
    my_list.append(str(random.randrange(101)) + f'x^{i}+')
  my_list.append(str(random.randrange(101)) + f'x+')
  my_list.append(str(random.randrange(101)))
  with open('py4/k.txt', 'w') as file:
    file.writelines(my_list)

get_k(3)