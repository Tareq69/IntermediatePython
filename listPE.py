# ordered, mutable, allows duplicate elements
a = [1,2,3]
print(a)
b = list()
print(b)

mylist = ['banana','cherry','apple']
item = mylist[0]
print(item)
for x in mylist:
    print(x)

if 'lemon' in mylist: # checking if element exists
    print('Yes')
else:
    print("No")

print(len(mylist)) # len() gives the length of the list

mylist.append('lemon')
print(mylist)

mylist.insert(1,'Coconut') # inserting element in specific index
print(mylist)

item = mylist.pop() # removes and returns the last element
print(mylist)
print(item)
#mylist.remove('Coconut') # removes specified value
# item = mylist.clear() # removes all the item of the list
# print(item)


lst = [1,2,3,-5,-2,0]
lst.reverse()   # reverses all the item of the list
# lst.sort() # sorts the whole list but also affects the original list so be careful
new_lst = sorted(lst) # sorts the list passed
print(new_lst)

lst1 = [5] * 5 # will create a list with 5 5's
lst2 = [3] * 3
lst3 = lst1 + lst2 # concatinating 2 list
print(lst3)

lst = [1,2,3,4,5,6,7,8,9]
a = lst[1:5]# slices element from m+1 to n
a = lst[:5]# slices element from start to n
a = lst[1:]# slices element from m+1 to end
print(a)

lst_org = ['banana','cherry','apple']
lst_copy = lst_org.copy() # actually copies the list meaning stores the list in a new memory space. = assignment only doesnt do it.
# also we can use lst = list(lst_org) and we can use lst = lst_org[:], these 3 way we can copy a list
print(lst_copy)

mlst = [1,2,3,4,5]
lst2 = [i for i in mlst] # list comprehension using for in loop
print(mlst)
print(lst2)




