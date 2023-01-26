#1
ingredients = [4, 4, 0]
def choose_coffee (*args):
  for coffee in args:
    if coffee == 'Эспрессо' and ingredients[0] >= 1:
      ingredients[0] -= 1
      return 'Эспрессо'
    elif coffee == 'Капучино' and ingredients[0] >= 1 and ingredients[1] >= 3:
      ingredients[0] -= 1
      ingredients[1] -= 3
      return 'Капучино'
    elif coffee == 'Маккиато' and ingredients[0] >= 2 and ingredients[1] >= 1:
      ingredients[0] -= 2
      ingredients[1] -= 1
      return 'Маккиато'
    elif coffee == 'Кофе по-венски' and ingredients[0] >= 1 and ingredients[2] >= 2:
      ingredients[0] -= 1
      ingredients[2] -= 2
      return 'Кофе по-венски'
    elif coffee == 'Латте Маккиато' and ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
      ingredients[0] -= 1
      ingredients[1] -= 2
      ingredients[2] -= 1
      return 'Латте Маккиато'
    elif coffee == 'Кон Панна' and ingredients[0] >= 1 and ingredients[2] >= 1:
      ingredients[0] -= 1
      ingredients[2] -= 1
      return 'Кон Панна'
  return 'К сожалению, не можем предложить Вам напиток'

print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))
print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))
print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))

#2
def encrypt_caesar(msg, shift):
  res = ''
  for sym in msg:
    if 1040 <= ord(sym) <= 1103:
      if ord(sym) > 1071 and ord(sym) + shift > 1103:
        res += chr(1072 + (ord(sym) + shift - 1103) - 1)
      elif ord(sym) <= 1071 and ord(sym) + shift > 1071:
        res += chr(1040 + (ord(sym) + shift - 1071) - 1)
      else:
        res += chr(ord(sym) + shift)
    else:
      res += sym
  print(res)

def decrypt_caesar(msg, shift):
  res = ''
  for sym in msg:
    if 1040 <= ord(sym) <= 1103:
      if ord(sym) >= 1072 and ord(sym) - shift < 1072:
        res += chr(1103 - (1072 - (ord(sym) - shift) - 1))
      elif ord(sym) >= 1040 and ord(sym) - shift < 1040:
        res += chr(1071 - (1040 - (ord(sym) - shift) - 1))
      else:
        res += chr(ord(sym) - shift)
    else:
      res += sym
  print(res)

encrypt_caesar('Да здравсвует Цезарь, проверка пограничных значений ЭЮЯ', 5)
decrypt_caesar('Йе мйхезцзшкч Ыкмехб, фхузкхпе фуихетньтаъ мтеьктно ВГД', 5)