def read_file(file_path, file_name, file_ext):    path = file_path + file_name + '.' + file_ext    try:        file = open(path, 'rb')    except:        print('Cannot open {}'.format(path))    file_data = file.read()    file.close()    return file_data