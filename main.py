import json
with open("file.json", 'r', encoding='utf-8') as file:
    i_file = json.load(file)

counter = 0
brik_close = 0
dizel = True

def menu():
    print("""
        1 - Вывести все записи 
        2 - Вывести запись по полю 
        3 - Добавить запись 
        4 - Удалить запись по полю 
        5 - Выйти из программы
        """)

def all_see():
    global counter 
    for i in i_file:
        print(f"""
        Код: {i['id']}, 
        Имя: {i['name']},                       
        Производитель: {i['manufacturer']}, 
        Бензин: {i['is_petrol']},    
        Объем v3 : {i['tank_volume']} 
        """)
    counter += 1

def kluch_see():
    global counter
    idnum = int(input("Введите номер машины: "))
    for i in i_file:
        if idnum == i['id']:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Производитель: {i['manufacturer']}, 
            Бензин: {i['is_petrol']},    
            Объем v3: {i['tank_volume']}
            """)
            counter += 1
            return
    print("Машина не найдена")
    counter += 1

def add_see():
    global counter 
    brik = False
    ids = int(input("Введите номер машины: "))
    
    for i in i_file:
        if i['id'] == ids:
            brik = True
        break
    
    if brik:
        print("Машина с таким номером уже существует.")
        counter += 1
    else:
        name = input("Введите имя машины: ")  
        manufacturer = input("Введите завод изготовитель: ")  
        is_petrol = input("бензин ? введите да/нет: ")  
        tank_volume = float(input("Введите объем v3 машины: "))  

        new_i = {
            'id': ids,
            'name': name,
            'manufacturer': manufacturer,
            'is_petrol': True if is_petrol == 'да' else dizel == False, 
            'tank_volume': tank_volume
        }

        i_file.append(new_i) 
        with open("file.json", 'w', encoding='utf-8') as output_file: 
            json.dump(i_file, output_file)
        print("Машина успешно добавлена.")
        counter += 1
           

def del_kluch_see():
    iddel = int(input("Введите номер машины: "))
    for i in i_file:
        if iddel == i['id']:
            i_file.remove(i)
            with open("file.json", 'w', encoding='utf-8') as output_file:
                json.dump(i_file, output_file)
            print("Машина успешно удалена.")
            counter += 1
            return
    print("Запись не найдена.")
    counter += 1

def end_see():
    global brik_close
    print(f"!!!!!!!!!!!! Программа завершена !!!!!!!!!! Она мучилась ровно {counter} раз !!!!!!!!!!!")
    brik_close += 1 

def main():
    while brik_close != 1:
        menu()
        user_input = int(input("Введите действие какое хотите выполнить: "))

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
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")

main()
