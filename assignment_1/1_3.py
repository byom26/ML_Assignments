li = list(map(str, input("Enter your name: ").rstrip().split(' ')))
print(' '.join([str(i[::-1]) for i in li]))