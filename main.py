def create_dict():
    School = {'1а': '25', '1б': '25', '2г': '20', '8б': '15', '12у': '10'}
    print(School)
    return School


def print_from_dict(diction, i):
    print(diction[i])


def input_class():
    while True:
        a = str(input("Введите класс: "))
        if a in {'1а', '1б', '2г', '8б', '12у'}:
            return a
        else:
            print("Такого класса на существует")


def remake_dict(School):
    n=0
    while n <3:
        y = input_class()
        x = str(input("Введите новое количество учеников: "))
        School[y] = x
        n+=1


def main():
    School = create_dict()
    needed_class = input_class()
    print_from_dict(School, needed_class)
    print('изменения происходят...')
    remake_dict(School)
    print(School)
    print('добавляем два новых класса')
    School['2a'] = '20'
    School['2б'] = '25'
    print(School)
    del School['12у']
    print('после удаления одного класса (12у)\n', School)


if __name__ == "__main__":
    main()
