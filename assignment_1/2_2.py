x = 1
for i in range(0, 9):
        if i<5 :
                for j in range(0,i+1):
                        print('* ', end='')
        else :
                for k in range(0,i-x):
                        print('* ', end='')
                x = x+2
        print()