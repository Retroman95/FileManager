import os

#------------------------------/ Блок Функций /---------------------------------------------------------
def new_file():
    file_1 = str(input('Введите имя нового файла: '))
    os.mkdir(file_1)
    print('Файл ', file_1, ' создан!')

def rename_file():
    name_1 = str(input('Введи имя файла: '))
    name_2 = str(input('Введи новое имя файла: '))
    os.rename(name_1, name_2)
    print('Файл ', name_1, ' переимонован на ', name_2)


def delete_file():
    del_1 = str(input('Введи имя файла для удаления: '))
    os.rmdir(del_1)
    print('Файл ', del_1, ' удален!')

def current_file():
    print("Текущая деректория:", os.getcwd())

#------------------------------/ Блок программы /---------------------------------------------------------
print("""Это программа по работе с файлами
1. Создание папки/файла
2. Переименование папки/файла
3. Удаление папки/файла
4. Идентификация текущего рабочего каталога
5. Завершить работу
""")
while True:
    answer = int(input("Выберите действие: "))
    if answer == 1:
        new_file()
    elif answer == 2:
        rename_file()
    elif answer == 3:
        delete_file()
    elif answer == 4:
        current_file()
    elif answer == 5:
        break
    else:
        print('Ошибка ввода!')
