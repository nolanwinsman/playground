import matplotlib.pyplot as plt
 
# data to be plotted
data = {'Ezekiel Steadywater': 450, 'Kimmo': 15, 'Darius': 434, 'Trunks': 388}
data = {k:int(v) for k,v in data.items()}

 
# creating the bar plot
plt.bar(data.keys(), data.values())
 
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantity')
 
plt.show()