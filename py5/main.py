#1
def returnNoChooseWord(word):
  with open('py5/text1in.txt', 'r', encoding='UTF-8') as file:
    my_list = file.read().split();

  res = list(filter(lambda el: -1 == el.find(word), my_list))
  
  with open('py5/text2out.txt', 'w', encoding='UTF-8') as file:
    print(*res, file=file)

returnNoChooseWord('абв');

#4
def compressionRleAlgorithm():
  with open('py5/text-compression4in.txt', 'r', encoding='UTF-8') as file:
    text = file.read();

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

  with open('py5/text-compression4out.txt', 'w', encoding='UTF-8') as file:
    file.writelines(res)

compressionRleAlgorithm()

def uncompressionRleAlgorithm():
  with open('py5/text-uncompression4in.txt', 'r', encoding='UTF-8') as file:
    text = file.read();
  
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
  
  with open('py5/text-uncompression4out.txt', 'w', encoding='UTF-8') as file:
    file.writelines(res)

uncompressionRleAlgorithm()