def get_mode():
  mode = input('1 - Импорт справочника\n2 - Создание справочника\n')
  return mode

def get_tool():
  tool = input('1 - Добавление данных\n2 - Редактирование данных\n3 - Удаление данных\n4 - Экспорт справочника\n')
  return tool

def get_import_file():
  path = input('Укажите путь к импортируемому файлу: ')
  return path

def get_export_file():
  name_file = input('Укажите название файла с расширением: ')
  return name_file

def get_add_data():
  name = input('Укажите ФИО: ')
  tel = input('Укажите номер телефона: ')
  return [name, tel]

def get_remove_data():
  name = input('Укажите ФИО: ')
  return name

def get_edit_data():
  name_edit = input('Укажите ФИО, у которого необходимо изменить информацию: ')
  tel = input('Укажите номер телефона: ')
  return [name_edit, tel]

def export_file(name_file, data):
  string_data = ''
  if name_file.split('.')[1] == 'xml':
    string_data += '<xml>\n'
    for name in data:
      string_data += f'<name>{name}</name>\n'
      string_data += f'<tel>{data[name]}</tel>\n'
    string_data += '</xml>'
    with open(f'py7/export/{name_file}', 'w', encoding='utf8') as file:
      file.write(string_data)
  if name_file.split('.')[1] == 'csv':
    for name in data:
      string_data += f'{name};{data[name]}\n'
    with open(f'py7/export/{name_file}', 'w', encoding='cp1251') as file:
      file.write(string_data)