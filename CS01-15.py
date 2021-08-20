def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","orange"]
my_function(fruits)

Superlist = [5,10,15,20,25,50,20]
for i in range(len(Superlist)):
    print(i)
    if (Superlist[i] == 20):
        Superlist[i] = 200
print(Superlist)