import matplotlib.pyplot as plt
import numpy as np

############################################################
##                initial condition                       ##
############################################################

def dydx(x,y):
    return y

H=0.1
Y0=1
X0=0
Xf=1

euler = True
r_k = True
graphs = False

############################################################
##                        Backend                         ##
############################################################

def eulerMethod(showplot=True):
    outy = []
    outx = []
    trueouty = []

    h = H
    y0 = Y0
    x0 = X0
    xf = Xf

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
    print()

    
    if (showplot):
        fig, ax = plt.subplots()
        ax.plot(outx, outy, color="red")
        ax.plot(outx, trueouty, color="blue")
        plt.show()

def rungekutta(showplot=True):
    outy = []
    outx = []
    trueouty = []

    h = H
    y0 = Y0
    x0 = X0
    xf = Xf

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
    print()

    if (showplot):
        fig, ax = plt.subplots()
        ax.plot(outx, outy, color="red")
        ax.plot(outx, trueouty, color="blue")
        plt.show()

if __name__ == "__main__":
    if euler:
        eulerMethod(graphs) 
    if r_k:
        rungekutta(graphs)