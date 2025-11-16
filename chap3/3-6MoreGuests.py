list = ['Kobe', 'Zyzz', 'Messi', 'Chico']

print(f'Unfortunately, {list[2]} cannot make it to the dinner.')

list[2] = 'Neymar'

for name in list:
    print(f'Dear {name}, you are invited to dinner at my mega mansion. Hope to see you soon!')

print("\n I have great news! I found a bigger dinner table, so now more guests can come! \n")

list.insert(0, 'Jordan')
list.insert(2, 'Ronaldo')
list.append('Jordan Barrett')

for name in list:
    print(f'Dear {name}, you are invited to dinner at my mega mansion. Hope to see you soon!')