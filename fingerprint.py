import csv
import numpy
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import interpolate

with open('Paper-features-formated.csv', newline='', encoding="utf8") as csvfile:
    data = list(csv.reader(csvfile))

number_of_collumns = len(data[0])
number_of_rows = len(data)

print("collumns: " + str(number_of_collumns))
print(number_of_rows)

# print(data[number_of_rows-1][number_of_collumns-1])

# for i in range(number_of_collumns):
#   if i < 3:
#       normalised_data.append(float('nan'))
#       continue
#   sum = float(0)
#   for j in range(1, number_of_rows):
#       sum += float(data[j][i])
#   normalised_data.append(sum / (number_of_rows-1))


temp = []

# todo: see how csv is formatted
normalised_data_mean = [float('nan'), float('nan'), float('nan')]
normalised_data_std = [float('nan'), float('nan'), float('nan')]
normalised_data_min = [float('nan'), float('nan'), float('nan')]
normalised_data_max = [float('nan'), float('nan'), float('nan')]
finalData = []

# todo: see how csv is formatted
for j in range(3, number_of_collumns):
    temp = []
    sum = 0
    for i in range(1, number_of_rows):
        print("aa" + data[i][j])
        temp.append(float(data[i][j]))
    temp = numpy.array(temp)
    normalised_data_mean.append(temp.mean(dtype=numpy.float64))
    normalised_data_min.append(temp.min())
    normalised_data_max.append(temp.max())
    normalised_data_std.append(temp.std(dtype=numpy.float64))

for j in range(1, number_of_rows):
    finalData = []
    for i in range(3, number_of_collumns):
        temp = float(data[j][i]) - normalised_data_mean[i]
        if temp > 0:
            if (normalised_data_max[i] - normalised_data_mean[i]) == 0:
                temp = 0
            else:
                temp = (temp / (normalised_data_max[i] - normalised_data_mean[i])) * 5  # times 5 since teh dot will be +-5
        else:
            if (normalised_data_mean[i] - normalised_data_min[i]) == 0:
                temp = 0
            else:
                temp = (temp / (normalised_data_mean[i] - normalised_data_min[i])) * 5
        finalData.append(temp)

    # print("finalData:")
    # print(finalData)
    #
    # print("mean:")
    # print(normalised_data_mean)
    # print("min:")
    # print(normalised_data_min)
    # print("max")
    # print(normalised_data_max)
    # print("std:")
    # print(normalised_data_std)

    coords = []
    #print(len(finalData) // 2)
    for i in range(len(finalData) // 2):
        coords.append([finalData[i] - 5, i])

    for i in range(len(finalData) // 2, len(finalData)):
        coords.append([finalData[i] + 5, 11 - i])

    f = open('fingerprints/' + data[j][1] + '.txt', 'w')
    for coord in coords:
        f.write(str(coord) + '\n')
    f.close()

    print(coords)
    x, y = numpy.split(coords, [-1], axis=1)
    x = numpy.ravel(x)
    y = numpy.ravel(y)
    print(x)
    # plt.scatter(x,y)

    plt.xlim([-11, 11])

    plt.plot(x, y, lw=50, color='aliceblue', solid_capstyle='round', marker="o", markersize=53)
    plt.plot(x, y, lw=20, color='#cfcfcf', solid_capstyle='round')

    plt.plot([-5, -5], [0, 5.4], color='cornflowerblue', linewidth=0.6)
    plt.plot([5, 5], [0, 5.4], color='cornflowerblue', linewidth=0.6)

    plt.plot(x, y, lw=10, color='tab:grey', solid_capstyle='round')
    x *= 0.95
    y *= 0.99
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 0.95
    y *= 0.99
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 0.95
    y *= 0.99
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 0.95
    y *= 0.99
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 0.88
    y *= 0.99
    plt.plot(x, y, color='gainsboro', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 0.88
    y *= 0.99
    plt.plot(x, y, color='gainsboro', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')

    x, y = numpy.split(coords, [-1], axis=1)
    x = numpy.ravel(x)
    y = numpy.ravel(y)

    x *= 1.05
    y *= 1.01
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 1.05
    y *= 1.01
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 1.05
    y *= 1.01
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 1.05
    y *= 1.01
    plt.plot(x, y, color='#4f4f4f', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 1.07
    y *= 1.01
    plt.plot(x, y, color='gainsboro', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')
    x *= 1.07
    y *= 1.01
    plt.plot(x, y, color='gainsboro', marker='', linestyle='solid', linewidth=1, solid_capstyle='round')

    x, y = numpy.split(coords, [-1], axis=1)
    x = numpy.ravel(x)
    y = numpy.ravel(y)
    plt.plot(x, y, color='k', marker=',', linestyle='solid', linewidth=2, solid_capstyle='round')
    plt.text(10, -0.2, 'v0.1', fontsize=6)
    plt.axis('off')
    plt.savefig('fingerprints/' + data[j][1] + '.png', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches='tight', pad_inches=0.1,
            metadata=None)
    plt.show()
