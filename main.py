import json

with open("file.json", 'r', encoding='utf-8') as file:
    i_file = json.load(file)


close = 0
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
    for i in i_file:
        print(f"""
        Код: {i['id']}, 
        Имя: {i['name']},                       
        Производитель: {i['manufacturer']}, 
        Бензин: {i['is_petrol']},    
        Объем бакa: {i['tank_volume']} 
        """)

def kluch_see():
    idnum = int(input("Введите номер машины: "))
    for i in i_file:
        if idnum == i['id']:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Производитель: {i['manufacturer']}, 
            Бензин: {i['is_petrol']},    
            Объем бака: {i['tank_volume']}
            """)
            return
    print("Машина не найдена")

def add_see():
    brik = False
    ids = int(input("Введите номер машины: "))
    
    for i in i_file:
        if i['id'] == ids:
            brik = True
        break
    
    if brik:
        print("Машина с таким номером уже существует.")
    else:
        name = input("Введите имя машины: ")  
        manufacturer = input("Введите завод изготовитель: ")  
        is_petrol = input("бензин ? введите да/нет: ")  
        tank_volume = float(input("Введите объем бака машины: "))  

        new_i = {
            'id': ids,
            'name': name,
            'manufacturer': manufacturer,
            'is_petrol': True if is_petrol == 'да' else dizel == False, 
            'tank_volume': tank_volume
        }

        i_file.append(new_i) 
        with open("file.json", 'w', encoding='utf-8') as output_file: 
            json.dump(i_file, output_file, ensure_ascii=False, indent=2)
        print("Машина успешно добавлена.")
           

def del_kluch_see():
    iddel = int(input("Введите номер машины: "))
    for i in i_file:
        if iddel == i['id']:
            i_file.remove(i)
            with open("file.json", 'w', encoding='utf-8') as output_file:
                json.dump(i_file, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно удалена.")
            return
    print("Запись не найдена.")

def end_see():
    global close
    print(f"!!!!!!!!!!!! Программа завершена !!!!!!!!!! ")
    close += 1 

def main():
    while close != 1:
        menu()
        point = int(input("Введите номер действия, которое хотите выполнить: "))

        if point == 1:
            all_see()
        elif point == 2:
            kluch_see()
        elif point == 3:
            add_see()
        elif point == 4:
            del_kluch_see()
        elif point == 5:
            end_see()
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")

main()
