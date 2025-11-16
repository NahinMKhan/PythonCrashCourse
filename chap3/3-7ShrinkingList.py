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

print("\n Sadly, something came up and now I can only invite two people for dinner. \n")

list_removed = []

while len(list) > 2:
    removed_guest = list.pop()
    list_removed.append(removed_guest)
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

print(f'\nDear {list[0]}, you are still invited do not worry!')
print(f'Dear {list[1]}, you are still invited do not worry!')

del list[0]
del list[0]
print(list)