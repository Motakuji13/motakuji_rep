d = dict ([(23, 34), (56, 87)])
print (d)

s = dict.fromkeys (['a', 'b'], 1)
print (s)

r = {a : a ** 2 for a in range(7)}
print (r)

person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 'adress': ['г. Андрюшки', 'ул. Ваасильковская д. 23б', 'кв.12'], 'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-565-345-23-65', 'mobile_phone_2': 'Нет'}}
print (person['name']['first_name'])


print (person.keys ())

name = input("")