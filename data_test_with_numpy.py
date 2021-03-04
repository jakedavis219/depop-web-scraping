import numpy as np


# 0 = always on film
# 1 = LOAF Cameras
# 2 = LensFayre Cameras
# 3 = TOOP SHOOT
# 4 = Film Camera Store
# 5 = Retro Camera Shop
# 6 = DTH Cameras
test = np.genfromtxt('shop_sales.csv', delimiter=",")
nan_array = np.isnan(test)
not_nan_array = ~ nan_array
array2 = test[not_nan_array]

print(array2)

listArray = list(array2)

for x in len(listArray):
    print(listArray[0,7])