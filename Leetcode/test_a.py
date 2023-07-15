"""
*** Условие:
Написать функцию, которая принимает аргумент типа словарь (dict). Словарь может быть вложенным.
Функция должна печатать все ключи и значения у этого словаря на всех уровнях вложенности.
Функция должна отображать уровень вложенности пробельными символами.

Примечание: возможно при копировании поехало форматирование

*** Пример:
d = {'a': 'b', 'c': {'d': {'e': 'g'}}, 'f': [[1,2],, 2, 3]}

dict_printer(d)

- a: b
- c:
    - d:
       - e: g
- f: [1, 2, 3]

"""

def dict_printer(d,x):
    x = " "  + x
    for i,v in d.items():
        if isinstance(v,dict):
            print(x, i, ": ")
            dict_printer(v,x)
        else:
            print(x, i, ": ", v)


# def dict_printer(d):
#     for i in d.items():
#         x = _dict_printer(i[1])
#         print("- ", i[0], ": ", x )
#     return 0

d = {'a': 'b', 'c': {'d': {'e': 'g'}}, 'f': [1, 2, 3]}
dict_printer(d,"-")