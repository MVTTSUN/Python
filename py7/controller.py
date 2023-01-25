from view import get_import_file, get_mode, get_tool
from model import tmp_data, modificate_data

def telephone_dir():
  mode = get_mode()

  if mode == '1':
    path = get_import_file()
    extend = path.split('.')[1]
    data = tmp_data(path, extend)
    tool = get_tool()
    modificate_data(tool)

  if mode == '2':
    tool = get_tool()
    modificate_data(tool)