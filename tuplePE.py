# ordered, immutable, allows duplicate elements
mt = (1,2,3,4,'max')  # tuple is not mutable and it is good practice to use first brackets to intialize a tuple
print(mt)

mt1 = tuple([1,2,3,4]) # tuple() to create a tuple

print(mt[0])

for x in mt: # checking if the element is in the tuple
    print(str(x)+" is in the tuple")
if 'max' in mt:
    print("Yes")
else:
    print("No")

mt2 = ('a','b','c','a')
print(len(mt2))
print(mt2.count('b')) # counting a value occurence
print(mt2.index('b')) # checking the index of the value

ml = list(mt2) # converting a tuple to a list
print(ml)

mt2 = tuple(ml) # converting a list to a tuple
print(mt2)

pt1 = mt2[:3] # slicing the tuple from element 0 to 2
print(pt1)
r = pt1[::-1] # reverse a tuple
print(r)