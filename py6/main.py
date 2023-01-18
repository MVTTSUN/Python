from random import randint

#1 list
list_random = [randint(1, 10) for _ in range(0, 10)]

def countElements(list_random):
  print(list_random)
  list_random.sort()
  res = {}
  count = 1
  for i in range(0, len(list_random)):
    if i != len(list_random) - 1 and list_random[i] == list_random[i + 1]:
      count += 1
    else:
      res[list_random[i]] = count
      count = 1
  print(res)

countElements(list_random)

#2 dict
def fill_fruits():
  length_dict = int(input('Введите длину словаря: '))
  res = {}
  for _ in range(0, length_dict):
    fruit = input('Введите название фрукта: ')
    count = int(input(f'Введите количество фруктов ({fruit}): '))
    res[fruit] = count
  print(res)

# fill_fruits()

def get_little_friends():
  length_dict = int(input('Введите длину словаря: '))
  friends = {}
  min_age = 100
  for _ in range(0, length_dict):
    friend = input('Введите имя друга: ')
    age = int(input(f'Введите сколько лет другу ({friend}): '))
    friends[friend] = age
    if min_age > age:
      min_age = age
  
  little_friends_list = []
  for name, age in friends.items():
    if age == min_age:
      little_friends_list.append(name)
  print(*little_friends_list, sep=', ')

# get_little_friends()

def get_middle_age_and_big_name_friends():
  length_dict = int(input('Введите длину словаря: '))
  friends = {}
  big_name = ''
  sum_age = 0
  for i in range(0, length_dict):
    friend = input('Введите имя друга: ')
    age = int(input(f'Введите сколько лет другу ({friend}): '))
    friends[friend] = age
    sum_age += age
    if len(big_name) < len(friend):
      big_name = friend
    if i == length_dict - 1:
      print(sum_age / length_dict)
      print(big_name)

# get_middle_age_and_big_name_friends()

def create_english_dict():
  length_dict = int(input('Введите длину словаря: '))
  res = {}
  for _ in range(0, length_dict):
    words = input('Напишите слово и перевод через тире: ')
    words = words.split(' - ')
    res[words[0]] = words[1].split(', ')
  print(res)

create_english_dict()