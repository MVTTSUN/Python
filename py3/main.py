#1
def sum_no_odd_position(my_list):
  sum = 0
  for i in range(1, len(my_list), 2):
    sum += my_list[i]
  print(sum)

sum_no_odd_position([2, 3, 5, 9, 3])

#2
def mult_pairs(my_list):
  mult_list = []
  for i in range(len(my_list) // 2):
    mult_list.append(my_list[i] * my_list[-(i + 1)])
  if len(my_list) % 2 == 1:
    mult_list.append(my_list[len(my_list) // 2] ** 2)
  print(mult_list)

mult_pairs([2, 3, 4, 5, 6])

#3
def diff_float(my_list):
  for i in range(len(my_list)):
    my_list[i] = (my_list[i] * 1000 - my_list[i] // 1 * 1000) / 1000
  max_number = my_list[0]
  min_number = my_list[0]
  for i in range(len(my_list)):
    if my_list[i] != 0:
      if max_number < my_list[i]:
        max_number = my_list[i]
      if min_number > my_list[i]:
        min_number = my_list[i]
  print(max_number - min_number)

diff_float([1.1, 1.2, 3.1, 5, 10.01])

#4
my_list = []
def dec_to_bin(number):
  if number == 1:
    my_list.append(1)
    my_list.reverse()
    print(*my_list, sep='')
  elif number == 0:
    my_list.append(0)
    my_list.reverse()
    print(*my_list, sep='')
  else:
    my_list.append(number % 2)
    dec_to_bin(number // 2)

dec_to_bin(45)