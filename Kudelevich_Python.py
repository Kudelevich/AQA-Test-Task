# If the entered number is greater than 7, then print “Hello”
number = int(input("Enter a number: "))
if number > 7:
    print("Hello")

# If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
name = input("Enter a name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

# There is a numeric array at the input, it is necessary to output array elements that are multiples of 3
array = list(map(int, input("Enter numbers separated by space: ").split()))
print("Elements that are multiples of 3:")
for num in array:
    if num % 3 == 0:
        print(num)
