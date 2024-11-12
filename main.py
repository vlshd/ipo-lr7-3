import json 

with open("star.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 

count = 0 

while True:
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

    number = int(input("Введите номер действия: "))

    if number == 1:
        for star in data:
            print(f"""
            Номер записи: {star['id']}, 
            Общее название: {star['name']},                       
            Название созвездия: {star['constellation']}, 
            Видно без телескопа: {star['is_visible']},    
            Радиус: {star['radius']} 
            """)
        count += 1

    elif number == 2:
        id = int(input("Введите номер звезды: "))
        find = False    
        for star in data:
            if id == star['id']:
                print(f"""
                Номер записи: {star['id']}, 
                Общее название: {star['name']},                       
                Название созвездия: {star['constellation']}, 
                Видно без телескопа: {star['is_visible']},    
                Радиус: {star['radius']} 
                """)
                find = True  
                break  
        count += 1
        if not find:
            print("Запись не найдена.")
 
    elif number == 3:
        id = int(input("Введите номер звезды: "))
        
        exists = False
        for star in data:
            if star['id'] == id:
                exists = True
                break
        
        if exists:
            print("Такой номер уже существует.")
        else:
            name = input("Введите название: ")  
            latin_name = input("Введите название созвездия: ")  
            is_visible = input("Введите, видно ли звезду без телескопа (да/нет): ")  
            radius = float(input("Введите радиус: "))  

            new_star = {
                'id': id,
                'name': name,
                'latin_name': latin_name,
                'is_visible': True if is_visible.lower() == 'да' else False, 
                'radius': radius
            }

            data.append(new_star) 
            with open("star.json", 'w', encoding='utf-8') as out_file: 
                json.dump(data, out_file)
            print("Звезда успешно добавлена.")
        count += 1

    elif number == 4:
        id = int(input("Введите номер звезды: "))
        find = False  

        for star in data:
            if id == star['id']:
                data.remove(star)  
                find = True  
                break 

        if not find:
            print("Запись не найдена.")
        else:
            with open("star.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно удалена.")
        count += 1

    elif number == 5:
        print(f"""Программа завершена.
               Кол-во операций: {count}""") 
        break
    else:
        print("Такого номера нет.")
    