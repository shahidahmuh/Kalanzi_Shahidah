#BAR CHARTS

#simple bar chart
import matplotlib.pyplot as plt
w = ['John','Peter','Ruth','Simon']
z = [10, 20, 30, 40]

plt.bar(w, z)
plt.title("Simple Bar Chart")
plt.xlabel("Names of Students")
plt.ylabel("Age of the Students")

plt.show()