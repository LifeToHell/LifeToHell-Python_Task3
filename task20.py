print('В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.') 
elementsarray = input(('Введите слово или слова через пробел :')).upper()
eng_points = { 1: 'AEIOULNSTR' , 2: 'DG', 3: 'BCMP', 4: 'FHVWYP', 5: 'K ', 8: 'JX', 10: 'QZ' }
rus_points = { 1: 'АВЕИНОРСТ' , 2: 'ДКЛМПУ', 3: ' БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ' }
eng = 'AEIOULNSTRDGBCMPFHVWYPKJXQZ'
rus = 'АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ'


if elementsarray[0] in eng:
    summa = 0
    for i in elementsarray:
        for key, value in eng_points.items():
            if i in value:
                summa += key
    print(f'Слово {elementsarray} набрало  = {summa} баллов')
else:
    if elementsarray[0] in rus:
        summa = 0
        for i in elementsarray:
            for key, value in rus_points.items():
                if i in value:
                    summa += key
        print(f'Слово {elementsarray} набрало  = {summa} баллов')
