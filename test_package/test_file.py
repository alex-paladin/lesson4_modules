def reverse_name(name1):
    list1 = list(name1)
    list1.reverse()
    print(" ".join(list1))

def diff_letters(name1):
    set1 = set(name1)
    return len(set1)



print('Enter your name:')
a = input()
print("Enter your friend's name:")
b = input()

print('Your reversed name is:',reverse_name(a))
print('Your name contains',diff_letters(a),' different letters')



