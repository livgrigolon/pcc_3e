my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f'Eu gosto de:')
for food in my_foods:
    print(f'{food.title()}')

print(f'Meu amigo gosta de:')
for food in friend_foods:
    print(f'{food.title()}')