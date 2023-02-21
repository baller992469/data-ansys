import matplotlib.pyplot as plt

# read data from the two txt files
with open('dandiaolan1#18out2.txt', 'r') as f1:
    data1 = [float(line.strip()) for line in f1]
    
with open('dandiaolan2#18.txt', 'r') as f2:
    data2 = [float(line.strip()) for line in f2]

# create a line chart
plt.plot(data1, label='File 1')
plt.plot(data2, label='File 2')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Line Chart')
plt.legend()
plt.show()
