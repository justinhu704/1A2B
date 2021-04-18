import random
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
answer=''
a_count=0 # initial A count
b_count=0 # initial B count
c = 0
for i in range(4):
    answer+=str(items[i])
while(True):
    c+=1
    number=input('Please enter the number: ')
    if not number.isdigit():  #cheak all input is digit
        pass
    else:
        if number==answer:
            print('You guess the correct number')
            if c < 2:
                print('You use', c, 'time.')
            else:
                print('You use', c, 'times.')
            break
        for i in range(4):
            for j in range(4):
                if i==j and number[i]==answer[j]:
                    a_count+=1
                elif number[i]==answer[j]:
                    b_count+=1
        print('{0}A{1}B.format(a_count, b_count')
        a_count=0
        b_count=0
    if c < 2:
        print('You use', c, 'time.')
    else:
        print('You use', c, 'times.')

