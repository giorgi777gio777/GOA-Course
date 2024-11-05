# Create a list of numbers from 1 to 20. Use a `for` loop to print only the even numbers from the list.
numbers = []
for i in range(1,20):
    numbers.append(i)
   
for num in numbers:
   if num % 2==0:
       print(num)


