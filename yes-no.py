import random 

choice = ['yes', 'no']

yes = 0
no = 0

for i in range(5):
    result = random.choice(choice)
    if result == 'yes':
        yes += 1
    else:
        no += 1

print('Yes ', yes)
print('No ', no)

if yes > no:
    print('--------')
    print('Yes Win')
else:
    print('--------')
    print('No win')
