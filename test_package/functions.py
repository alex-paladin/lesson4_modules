def common_letters(name1,name2):
    set1 = set(name1)
    set2 = set(name2)
    return len(set1.intersection(set2))

def len_comparison(name1,name2):
    set1 = set(name1)
    set2 = set(name2)
    if len(set1) > len(set2):
                             print(name1,'has more letters than',name2)
    elif len(set1) < len(set2):
                               print(name2,'has more letters than',name1)
    elif len(set1) == len(set2):
                               print(name2,'and',name1,'have equal length')

print('Enter your name:')
a = input()
print("Enter your friend's name:")
b = input()

print("Your and your friend's name contain",common_letters(a,b),'common letters')
len_comparison(a,b)



