'''
1) The keywords are specific words or reserved words whose meaning and tasks are predefined by the developer .
2) Meaning and task's are could not be changed .
3) The keywords are also called as universal standard words because these keywords are acting same across all the programming languages .
4) True False and None are called special keywords because we can use the special keywords as a value of the variable .
'''
import keyword
print(keyword.kwlist)  # print keywords

print(keyword.iskeyword('hello'))  # check keyword