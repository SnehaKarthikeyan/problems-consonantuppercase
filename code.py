Coding:

first = input()

second = ""

vowels = ['a','e','i','o','u']

for i in first:

 if i in vowels:
  second = second+i
 
 else :

  second = second+i.upper()

print(second)
