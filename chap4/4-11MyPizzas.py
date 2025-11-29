pizzas = ['New York', 'Deep Dish', 'Pepperoni']
friend_pizzas = pizzas[:]  # Make a copy of the list

pizzas.append('Super Pizza')
friend_pizzas.append('Chicken Pizza')

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print('I really love pizza!')

for pizza in friend_pizzas:
    print(f'My friend likes {pizza} pizza')
print("My friend really loves pizza too!")