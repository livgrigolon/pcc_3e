color = 'blue'
print(color == 'blue')
print(color != 'blue')

name = 'Livia'
print(name.lower() == 'livia')

age = 18
print(age == 18)

age = 21
print(age < 21)

age = 21
print(age > 21)

age = 60
print(age <= 60)

age = 60
print(age >= 59)

age_1 = 17
age_2 = 21
print(age_1 >= 18 and age_2 <= 18)

age_1 = 17
age_2 = 21
print(age_1 >= 18 or age_2 >= 18)

names = ['Livia', 'Maria', 'Gabriel', 'Lucas']
print('Livia' in names)

name = 'Joao'
if not 'Joao' in names:
    print(f'{name} is not in the list')
