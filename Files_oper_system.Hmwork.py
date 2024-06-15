import os
from time import strftime


def print_file_info(filename):
    file_path = os.path.join(directory, filename)

    # Получаю информацию о файле
    try:
        file_size = os.path.getsize(file_path)

        # Получаю время последнего изменения файла
        last_modified = os.path.getmtime(file_path)
        last_modified_str = strftime('%Y-%m-%d %H:%M:%S', last_modified)

        parent_dir = os.path.dirname(file_path)

        # Вывожу информацию о файле
        print(f'File Name: {filename}')
        print(f'Size: {file_size} bytes')
        print(f'Last Modified: {last_modified_str}')
        print(f'Parent Directory: {parent_dir}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')


# Указываю путь к каталогу
directory = 'заменяю/на/путь/к/каталогу/который/хочу/обойти'

# Обхожу все файлы и папки в каталоге
for root, dirs, files in os.walk(directory):
    for file in files:
        print_file_info(file)