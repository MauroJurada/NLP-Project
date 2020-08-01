import csv
import numpy
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import interpolate

file1 = "Chen, Kang, Lin (2018)"
file2 = "Liu, Feng, Chen, Wei, Deo (2019)"

coords = numpy.load('fingerprints/' + file1 + '.npy')
coords2 = numpy.load('fingerprints/' + file2 + '.npy')

print(coords)
x, y = numpy.split(coords, [-1], axis=1)
x = numpy.ravel(x)
y = numpy.ravel(y)

x2, y2 = numpy.split(coords2, [-1], axis=1)
x2 = numpy.ravel(x2)
y2 = numpy.ravel(y2)

plt.xlim([-11, 11])

plt.plot(x, y, lw=14, color='lightsteelblue', solid_capstyle='round', alpha=0.6)
plt.plot(x2, y2, lw=14, color='linen', solid_capstyle='round', alpha=0.6)

plt.plot([-5, -5], [0, 5.2], color='cornflowerblue', linewidth=0.6)
plt.plot([5, 5], [0, 5.4], color='cornflowerblue', linewidth=0.6)

plt.plot(x, y, color='tab:blue', marker=',', linestyle='solid', linewidth=2, solid_capstyle='round', alpha=0.7)
plt.plot(x2, y2, color='tab:orange', marker=',', linestyle='solid', linewidth=2, solid_capstyle='round', alpha=0.7)

plt.text(10, -0.2, 'v0.1', fontsize=6)

plt.text(-10.5, 5.5, file1, fontsize=8, color="tab:blue")
plt.text(-10.5, 5.3, file2, fontsize=8, color="tab:orange")
plt.axis('off')
plt.savefig('fingerprints/' + file1 + ' -- ' + file2 + '.png', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches='tight', pad_inches=0.1,
            metadata=None)
plt.show()
