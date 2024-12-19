import numpy as np
from scipy import stats

data = np.loadtxt('dataset.txt', delimiter=' ', dtype=int)

# print('Mean is: ', np.mean(data))
#
# print('Median is: ', np.median(data))
#
# print('Mode is: ', int(stats.mode(data)[0]))
#
# print('StDev is: ', np.std(data))

my2dMatrix = data.reshape(2500,100)
print('fourth element of a 2d matrix: \n')
print(my2dMatrix[4:5], '\n')

my3dMatrix = data.reshape(2500,10,10)
print('fourth element of a 3d matrix: \n')
print(my3dMatrix[4:5,2], '\n')

slicedMatrix = my2dMatrix[::10,2:6]
print('first five elements of sliced matrix: \n')
print(slicedMatrix[0:5])

