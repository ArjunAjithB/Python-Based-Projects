a = ["Potato","Carrot","Cauliflower"]
b = [2,4,6,8,10]
c = ["Purple","Peach","Green","Blue"]
d = [1,2,3,4,5]
e = ["Japan","Turkey","Holland","Bhutan","Mexico"]
f = [i for i in range(0,31) if i%3 == 0]
g = ["Forrest Gump","Infinity War","The Martian"]
h = [i for i in range (0,100) if i%2 != 0][:5]
print("Three of my favorite vegetables")
print(a)
print("The first 5 even numbers")
print(b)
print("Four different colors you like")
print(c)
print("The square of numbers from 1 to 5")
print([i**2 for i in d])
print("Names of 5 countries you want to visit")
print(e)
print("The multiples of 3 up to 30")
print(f)
print("Three of your favorite movies")
print(g)
print("The first 6 odd numbers")
print(h)
#trying to square with numpy
import numpy as np
x = np.array([1,2,3,4,5])
y=np.square(x)
list(y)
print(y)
print("Exercise 2")
z=15-30
print(z)
u=7*6
print(u)
v=25%4
print(v)
w=9**2
print(w)
i=100+200+300
print(i)
j=144/12
print(j)
k=3.5*2
print(k)
l=15.9-8.4
print(l)
print("Exercise 3")
m=[5,10,15,20]
print("Calculate the sum of all elements")
print(sum(m))
print("Multiply each element by 3 and print the new list")
print([num * 3 for num in m])
n=[3,6,9,12,15]
print("Calculate the average of the numbers in the list")
print(sum(n)/len(n))
print("Find the largest and smallest numbers in the list")
print(max(n),min(n))
list1=[1,2,3,4,5]
list2=[10,20,30,40,50]
print("Add corresponding elements of both lists (e.g., 1 + 10, 2 + 20) and store the results in a new list")
print([x+y for x,y in zip(list1,list2)])
#Second Attempt
print([list1[i] + list2[i] for i in range(len(list1))])
list3=[2,4,6,8,10]
print("Find the product of all the elements in the list")
print(np.prod(list3))
print("Divide each element by 2 and print the resulting list")
print([num/2 for num in list3])
