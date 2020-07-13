# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(num):
    print(num % 2 == 0)
even = input("Check if number is even")
even = int(even)
is_even(even)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("EVEN")
else:
    print("odd")