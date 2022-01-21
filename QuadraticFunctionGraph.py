'''
Quadratic function calculator
'''

import matplotlib.pyplot as plt

#Assume values of X
#x_values = [-1,1,2,3,4,5]
x_values = list(range(50))
y_values = []
for x in x_values:
    #Calculate the value of the quadratic function
    y = x**2 + 2*x + 1
    print('x={0} y={1}'.format(x,y))
    y_values.append(y)

plt.plot(x_values,y_values)
plt.xlabel('X Axes')
plt.ylabel('Y Axes')
plt.title('Quadratic Function')
plt.show()
    
