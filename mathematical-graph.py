import matplotlib.pyplot as plt, numpy as np, math


x_values = np.linspace(-100, 100, 2000)

def plot():
    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values, '-', color='green')
    plt.show()
    plt.close()


def function_generator():
    function = (np.linspace(-100, 100, 2000) * 0)
    while True:
        opperation = input("Opperation: ")
        if opperation == ("e"):
            break
        
        number = input("Number: ")
        if number == "x":
            number = x_values
        else:
            number = int(number)

#Opperations
        if opperation == "+":
            function = (function + number)
        elif opperation == "-":
            function = (function - number)
        elif opperation == "*":
            function = (function*number)
        elif opperation == "**":
            function = (function**number)
        elif opperation == "/":
            function = (function/number)
        elif opperation == "//":
            function = (function**(1/number))

    return(function)
    

y_values = function_generator()
plot()
