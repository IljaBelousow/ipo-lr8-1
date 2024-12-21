import json



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
    try:
        idnum = int(input("Введите номер машины: "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный номер машины.")
        return

    qwe = False  
    index = 0  
    for i in i_file:
        if idnum == i['id']:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Фабрика: {i['manufacturer']}, 
            Заправлена: {i['is_petrol']},    
            Объем Бака: {i['tank_volume']}
            Индекс в списке: {index}
            """)
            qwe = True  
            break  
        index += 1
    counter += 1
    if not qwe:
        print("Запись не найдена.")

def add_see():
    global counter 
    try:
        ids = int(input("Введите номер машины: "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный номер машины.")
        return

    errrror = False
    for i in i_file:
        if i['id'] == ids:
            errrror = True
            break
        
    if errrror:
        print("Ошибка: машина с таким номером уже существует.")
    else:
        name = input("Введите имя машины: ")  
        manufacturer = input("Введите завод изготовитель: ")  
        is_petrol = input("Бензин? Введите да/нет: ") 
        tank_volume = input("Введите объем бака машины: ")  

        try:
            tank_volume = float(tank_volume)
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректный объем бака.")
            return

        new_i = {
            'id': ids,
            'name': name,
            'manufacturer': manufacturer,
            'is_petrol': True if is_petrol.lower() == 'да' else False, 
            'tank_volume': tank_volume
        }

        i_file.append(new_i) 
        with open("file.json", 'w', encoding='utf-8') as output_file: 
            json.dump(i_file, output_file, ensure_ascii=False, indent=2)
        print("Машина успешно добавлена.")
        counter += 1
           
def del_kluch_see():
    global counter
    try:
        iddel = int(input("Введите номер машины: "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный номер машины.")
        return

    qwe = False  

    for i in i_file:
        if iddel == i['id']:
            i_file.remove(i)  
            qwe = True  
            break 

    if not qwe:
        print("Запись не найдена.")
    else:
        with open("file.json", 'w', encoding='utf-8') as output_file:
            json.dump(i_file, output_file, ensure_ascii=False, indent=2)
        print("Машина успешно удалена.")
        counter += 1

def end_see():
    global brik_close
    print(f"Программа завершена. ОНА МУЧИЛАСЬ РОВНО {counter} РАЗ !!!!!!!!!")
    brik_close = 1  # Устанавливаем флаг завершения программы

def main():
    with open("file.json", 'r', encoding='utf-8') as file:
        i_file = json.load(file)

    counter = 0
    brik_close = 0
    
    while brik_close != 1:
        menu()
        try:
            user_input = int(input("Введите действие какое хотите выполнить: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите число от 1 до 5.")
            continue

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
