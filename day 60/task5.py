# Create a list of numbers from 1 to 10. Use a `for` loop to create a new list containing the squares of each number. Print the new list.
numbers = [1,2,3,4,5,6,7,8,9]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number*number)
print (squared_numbers)