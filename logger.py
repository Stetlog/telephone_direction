# Возвращение списков к изначальному состоянию
def test_data_for_first_variant():
    with open("test_first_variant.csv", "r", encoding="utf-8") as file:
        test1_first_variant1 = [line for line in file]
    with open("data_first_variant.csv", "w", encoding="utf-8") as file:
        file.writelines(test1_first_variant1)
def test_data_for_second_variant():
    with open("test_second_variant.csv", "r", encoding="utf-8") as file:
        test1_second_variant1 = [line for line in file]
    with open("data_second_variant.csv", "w", encoding="utf-8") as file:
        file.writelines(test1_second_variant1)
##########################

# Со вторым списком не удается. Код в фуекции Def rename_data()

from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")

def rename_data():
    name2 = input("Введите имя, которое хотите изменить: ")
    surname2 = input("Введите фамилию, которую хотите изменить: ")
    name1 = name2 + str("\n")
    surname1 = surname2 + str("\n")
    
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        list1 = [line for line in file]
    if name1 in list1 and surname1 in list1:
        new_name2 = input("Введите новое имя: ")
        new_surname2 = input("Введите новую фамилию: ")
        list1[list1.index(name1)] = new_name2 + str('\n')
        list1[list1.index(surname1)] = new_surname2 + str('\n')
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            file.writelines(list1)
    

    ####   Со вторым списком что-то не удается #####


    # with open("data_second_variant.csv", "r", encoding="utf-8") as file:
    #     list1 = [line for line in file]
    # for line in list1:
    #     if name2 in line and surname2 in line:
    #         list1[list1.index(line[list1.index(name2)])] = new_name2
    #         list1[list1.index(line[list1.index(surname2)])] = new_surname2
    #         with open("data_second_variant.csv", "w", encoding="utf-8") as file:
    #             file.writelines(list1)

        # name2 = "name2"
    # surname2 = "surname2"
    # with open("data_second_variant.csv", "r", encoding="utf-8") as file:
    #     list1 = [line for line in file]
    #     print(list1)
    # for line in list1:
    #     if name2 in line and surname2 in line:
    #         print(list1[list1.index(line)][list1.index(name2)])



def delete_data():
    name = input("Введите имя, которое хотите удалить: ") + str("\n")
    surname = input("Введите фамилию, которую хотите удалить: ") + str("\n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        list1 = [line for line in file]
    if name in list1 and surname in list1:
        del list1[list1.index(name): list1.index(name) + 5]
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            file.writelines(list1)


