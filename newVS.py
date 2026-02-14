"""A simple chaotic function demonstration
This function takes a number between 0 and 1 and applies the logistic map
    repeatedly to demonstrate chaotic behavior.
    """

def main():
    print("Lets do a chaotic function")
    x = .25
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
    
main()

"""
A simple chaotic function demonstration
This function takes a number between 0 and 1 and applies the logistic map
    repeatedly to demonstrate chaotic behavior.

    I need something to do. I need to make money now, problem solved. I will make a program that demonstrates a chaotic function, then I will calculate the area of a circle, and then I will do some for loops.

"""

print("  ")
print("That was a choatic function demonstration but now I need to do something else.")
print("  ")
print("Now on to the area of a circle.")
pi = 3.14159
radius = 2.2
area = pi*(radius ** 2)
circumference = 2 * pi * radius
print("The radius is ", radius)
print("The circumference is ", circumference)
print("The area of the circle is:", area)
print("  ")
print("Now some for loops!")

looper = [12,2,34,564,346]
testString = "This is a test string"
print(looper)
print(*looper)
print(*looper, sep = ', ')
print(testString)
