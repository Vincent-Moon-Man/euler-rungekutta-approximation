import matplotlib.pyplot as plt
import numpy as np

def dydx(x,y):
    return y

h=0.1

def eulerMethod(showplot=True):
    outy = []
    outx = []
    trueouty = []

    y0=1
    x0=0
    xf=1

    while(True):
        if (x0 < xf-h):
            y0 = y0 + h * dydx(x0,y0)
            x0 = x0 + h
            outy.append(y0)
            outx.append(x0)
            trueouty.append(np.power(np.e, x0))
        else:
            break

    print("EULER METHOD")
    print("Estimated Value:", outy[-1])
    print("True Value:", trueouty[-1])
    print("Error: ", trueouty[-1] - outy[-1])
    print("Amount of Ticks:", (xf - x0) / h)

    
    if (showplot):
        fig, ax = plt.subplots()
        ax.plot(outx, outy, color="red")
        ax.plot(outx, trueouty, color="blue")
        plt.show()

def rungekutta(showplot=True):
    outy = []
    outx = []
    trueouty = []

    y0=1
    x0=0
    xf=1

    while(True):
        if (x0 < xf-h):
            k1 = h * dydx(x0, y0)
            k2 = h * dydx(x0 + h / 2, y0 + k1 / 2)
            k3 = h * dydx(x0 + h / 2, y0 + k2 / 2)
            k4 = h * dydx(x0 + h, y0 + k3)

            y0 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x0 = x0 + h

            outy.append(y0)
            outx.append(x0)
            trueouty.append(np.power(np.e, x0))
        else:
            break

    print("RUNGE KUTTA")
    print("Estimated Value:", outy[-1])
    print("True Value:", trueouty[-1])
    print("Error: ", trueouty[-1] - outy[-1])
    print("Amount of Ticks:", (xf - x0) / h)

    if (showplot):
        fig, ax = plt.subplots()
        ax.plot(outx, outy, color="red")
        ax.plot(outx, trueouty, color="blue")
        plt.show()

if __name__ == "__main__":
    # eulerMethod(False)
    rungekutta(False)