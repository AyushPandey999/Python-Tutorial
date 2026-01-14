'''
Variables are the name of memory blocks where the values are stored .

The variables are the container which is used to store some values .

Syntax :- Variable_Name = Value

There are two types of spaces :
1) Variable / Stack Space .
2) Value / Heap Space

x = 10

x -> Stack Space -> 0 * 17
10 -> Heap Space -> 0 * 17

Memory Address :
 id(var/value)
'''

x=10
y=20
print('x : ',id(x))
print('y : ',id(y))