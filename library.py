import argparse
import json
import os.path

class database:

    def __init__(self):
        if not os.path.exists(self.filename):
            self.__writeData({'books': []})

    def add(self, title, author, year):
        data = self.__readData()
        data['books'].append({
            'title': title,
            'autor': author,
            'year': year,
            'status': 'в наличии'
            })
        self.__writeData(data)
        print('Книга добавлена!')
    
    def remove(self, id):
        data = self.__readData()
        try:
            del data['books'][id]
        except:
            print("Нет такой книги!")
        self.__writeData(data)
        print('Книга удалена!')
    
    def search(self, field, value):
        data = self.__readData()

        isFound = False
        
        try:
            for i in range(0, len(data['books'])):
                if data['books'][i][field] == value:
                    print('id = ', i)
                    print('Название книги: ', data['books'][i]['title'])
                    print('Автор книги: ', data['books'][i]['autor'])
                    print('Год издания: ', data['books'][i]['year'])
                    print('Статус книги: ', data['books'][i]['status'])
                    isFound = True
                    break
            if not isFound:
                print('Книга не найдена!')
        except:
            print('Нет такого поля!')


    def show(self):
        data = self.__readData()
        for i in range(0, len(data['books'])):
            print(i, ', ', data['books'][i]['title'], ', ', data['books'][i]['autor'], ', ', data['books'][i]['year'], ', ', data['books'][i]['status'])
    
    def change(self, id): 
        data = self.__readData()
        if data['books'][id]['status'] == 'в наличии':
            data['books'][id]['status'] = 'выдана'
            print('Статус книги изменён на выдана!')
        else:
            data['books'][id]['status'] = 'в наличии'
            print('Статус книги изменён на в наличии!')
        self.__writeData(data)
    
    def __writeData(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    
    def __readData(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    filename = 'database.json'

def main():

    parser = argparse.ArgumentParser(
        prog='library',
        description='Консольное приложение для управления библиотекой книг.',
    )

    parser.add_argument('-a','--add', nargs=3, type=str, help='Добавить книгу. \nПринимает три аргумента: название книги, автора и год издания.')
    parser.add_argument('-r', '--remove', nargs=1, type=int, help='Удалить книгу. \n Принимает один аргумент: id книги.')
    parser.add_argument('-s', '--search', nargs=2, type=str, help='Найти книгу.\n Принимает два аргумента: заголовок таблицы и его значение.')
    parser.add_argument('-l', '--list', nargs='?', const='1', help='Вывести список всех книг')
    parser.add_argument('-c', '--change', nargs=1, type=int, help='Меняет статус книги.')

    args = parser.parse_args()

    db = database()

    if args.list:
        db.show()
    if args.add:
        db.add(args.add[0], args.add[1], args.add[2])
    if args.remove:
        db.remove(args.remove[0])
    if args.search:
        db.search(args.search[0], args.search[1])
    if args.change:
        db.change(args.change[0])



if __name__ == '__main__':
    main()