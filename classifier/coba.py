import numpy as np
from statistics import mean

lst1 = [1,2,3]
lst2 = [2,3,4]
lst3 = [3,4,5]
lst_ave = []
for i in range(len(lst1)):
    lst_ave.append(mean([lst1[i],lst2[i],lst3[i]]))
print(lst_ave)