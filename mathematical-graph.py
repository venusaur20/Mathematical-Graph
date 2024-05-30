import matplotlib.pyplot as plt, numpy as np, math


x_start = -10 #int(input("Start of x-axis: "))
x_finish = 10 #int(input("End of x-axis: "))
accuracy = 0.1 #int(input("Update Interval: "))
x = np.arange(x_start, x_finish, accuracy)

function = ()

while True:
    opperation = input("Opperation: ")
    if opperation == ("e"):
        break
    number = input("Number: ")

#Check if the "number" is a variable or number
    if number == ("x"):
        number = (x)
        print(number)
    else:
        number = np.arange()

#Opperations
    if opperation == "+":
        function = (function + number)
    elif opperation == "-":
        function = (function - number)
    elif opperation == "**":
        function = (function**number)
    elif opperation == "/":
        function = (function/number)
    elif opperation == "//":
        function = (function**(1/number))

    print(opperation)
    print(number)

plt.plot(x, function, 'r--')
plt.show()
