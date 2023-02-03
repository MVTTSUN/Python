from datetime import datetime as dt

def logger(id, nickname, message):
  time = dt.now().strftime('%H:%M:%S')
  data = dt.now().date()
  with open('log.csv', 'a') as file:
    file.write(f'{data};{time};{id};{nickname};{message}\n')