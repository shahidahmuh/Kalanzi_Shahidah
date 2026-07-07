#Matplotlib pyplot - Is a module that is found within matplotlib that provides a MATLAB for making plots
#it simplifies the process of adding plot elements such as filters etc 

#Steps to use pyplot
#1. import matplotlib.pyplot as plt
#2. Create data 
#3. plot data using plt.plot()
#4. customize the plot. Add titles, labels.
#5. Display the plot, use plt.show()

#BASIC LINE GRAPH
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8, 10]
y = [0, 4, 8, 16, 20, 24]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', label="Datapoints")

ax.set_title("Basic Line Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
plt.show()