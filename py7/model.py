from view import get_add_data, get_edit_data, get_remove_data, get_export_file, export_file
from logger import logger

tmp_dir = {}

def tmp_data(path, extend):

  with open(f'py7/import/{path}', encoding='utf8') as file:
      lines = file.read().splitlines()

  if extend == 'csv':
    for i in range(0, len(lines)):
      line = lines[i].split(';')
      tmp_dir[line[0]] = line[1]
  elif extend == 'xml':
    for i in range(0, len(lines)):
      if 'name' in lines[i]:
        name = lines[i].replace('>', '<').split('<')[2]
      elif 'tel' in lines[i]:
        tel = lines[i].replace('>', '<').split('<')[2]
        tmp_dir[name] = tel

  return tmp_dir

def modificate_data(tool):
  if tool == '1':
    data_list = get_add_data()
    tmp_dir[data_list[0]] = data_list[1]
    print(tmp_dir)
    logger(data_list[0], data_list[1])
  elif tool == '2':
    data_list = get_edit_data()
    if tmp_dir.get(data_list[0]):
      tmp_dir[data_list[0]] = data_list[1]
      print(tmp_dir)
  elif tool == '3':
    data_list = get_remove_data()
    if tmp_dir.get(data_list):
      tmp_dir.pop(data_list)
      print(tmp_dir)
  elif tool == '4':
    name_file = get_export_file()
    export_file(name_file, tmp_dir)