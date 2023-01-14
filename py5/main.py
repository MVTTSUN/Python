#1
def returnNoChooseWord(text, word):
  my_list = text.split();
  res = list(filter(lambda el: -1 == el.find(word), my_list))
  print(*res, sep=' ')

returnNoChooseWord('пабв апрол прабв про но менко', 'абв');

#2
def compressionRleAlgorithm(text):
  res = ''
  cnt = 0
  for i in range(0, len(text)):
    if(i == len(text) - 1):
      res += str(cnt + 1) + text[i]
    elif(text[i] == text[i + 1]):
      cnt += 1
    else:
      res += str(cnt + 1) + text[i]
      cnt = 0
  print(res)

compressionRleAlgorithm('aabbbcccdddddejghrgrrrrre')

#3
def uncompressionRleAlgorithm(text):
  tmp_text = text[0]
  res = ''
  for i in range(0, len(text)):
    if(i == len(text) - 1):
      res += int(tmp_text) * text[i]
    elif(tmp_text.isdigit() and text[i + 1].isdigit()):
      tmp_text += text[i + 1]
    else:
      res += int(tmp_text) * text[i + 1]
      tmp_text = '0'
  print(res)

uncompressionRleAlgorithm('11a4g5h1s3d')