import matplotlib.pyplot as plt

data = {'milk': 60, 'water': 10}
names = list(data.keys())
values = list(data.values())

plt.bar(range(len(data)), values, tick_label=names)
plt.show()