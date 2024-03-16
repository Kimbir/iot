import np as np
import matplotlib.pyplot as plt
q = 4
w = 1
c = 20
x = np.linspace(-3*np.pi, 3*np.pi, 250)
s = np.random.normal(1, 4, 250)/20
y = np.sin(x)+ s,
plt.figure(figsize=(10, 5)),
plt.scatter(x, y,
 s=300,
 marker='s',
 lw=2,
 edgecolor='black',
 c='violet',
 hatch='**'
),
plt.title(label='$sin(x)$ with random noise',
 fontsize=20
),
plt.xlabel('x range', fontsize=18),
plt.ylabel('y range', fontsize=18),
plt.tick_params(labelsize=16),
plt.xticks(ticks=np.arange(-10, 11, 2))
plt.yticks(ticks=np.arange(-1.5, 2,0.5),
 labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1]
),
plt.show()
