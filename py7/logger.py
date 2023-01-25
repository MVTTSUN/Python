from datetime import datetime as dt

def logger(name, tel):
  time = dt.now().strftime('%H:%M:%S')
  with open('py7/log/log.csv', 'a') as file:
    file.write(f'{time};{name};{tel}')