import json
brik = 0
index = 0
with open("file.json", "r", encoding="utf-8") as a:
    file = json.load(a)

def all_see():
    global counter
    for i in file:
            print(f"""
            ID: {i["id"]}, 
            Имя: {i["name"]},                       
            Facture: {i["manufacturer"]}, 
            Benzin: {i["is_petrol"]},    
            v3: {i["tank_volume"]}
            """)

def kluch_see():
    global counter
    found = False
    id_input = input("Введите ключ: ")
    for i in file:
        if id_input == i["id"]:  
            print(f"""
            ID: {i["id"]}, 
            Имя: {i["name"]},                       
            Facture: {i["manufacturer"]}, 
            Benzin: {i["is_petrol"]},    
            v3: {i["tank_volume"]}
            """)
            found = True
            break
        if not found:
            print("Такой записи нет :(")
def add_see():
    global counter
    add_input = input("Введите ключ для добавления: ")
    found_2 = False
    for i in file:
        if i["id"] == add_input:
            found_2 = True
            print("Такой ключ уже есть")
            break
        else:
            add_name_input = input("Введите название машины: ")
            add_creator_input = input("Введите название производителя: ")
            add_bool_input = input("Заправляется ли машина бензином (да/нет): ")
            add_cub_input = input("Введите объём бака в литрах: ")

            repository = {
                "id": add_input,
                "name": add_name_input,
                "manufacturer": add_creator_input,
                "is_petrol": True if add_bool_input == "да" else False,
                "tank_volume": add_cub_input,   
            }
            file.append(repository)
            with open("file.json", "w", encoding="utf-8") as b:
                json.dump(file, b)  

def del_kluch_see():
    global counter
    del_input = int(input("Введите ключ для удаления: "))
    found_3 = False
    try:
        for i in file:
            if del_input == i["id"]:
                file.remove(i)
        with open("file.json", "w", encoding="utf-8") as b:
            json.dump(file, b)
    except StopIteration:
        print("Такой записи нет")

def end_see():
    global brik
    print("Вы закрыли программу, ПОЗДРАВЛЯЮ ХЫЦКЖСФЮЪКСЪ")
    brik += 1

def not_end():
    print("ТЫ ЧОТ ПОПУТАЛ ПОХОДУ")

def menu():
    print("""==================================
1 - Вывести все записи
2 - Вывести запись по ключу
3 - Добавить запись
4 - Удалить запись по ключу
5 - Выйти из программы
==================================""")

def main():
    while brik != 1:
        menu()
        user_input = int(input("Введите действие: "))
        if user_input == 1:
            all_see()
        elif user_input == 2:
            kluch_see()
        elif user_input == 3:
            add_see()
        elif user_input == 4:
            del_kluch_see()
        elif user_input == 5:
            end_see()
        else:
            not_end()

main()