#2. lets you add names to your array
studentname = []
print('List is empty : ('))
option = str(input('You want to add the element in the list (yes/no)? : '))
if option == 'yes':
    num = int(input('How much element do you want : '))
    for i in range (1, num+1):
        print('Enter the', i, 'student name: ')
        n = str(input())
        studentname.append(n)
else:
    print('Thank you for using sharecodepoint services !!')
    print('\n', studentname)