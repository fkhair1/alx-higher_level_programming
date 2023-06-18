#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum([a[0]*a[1] for a in my_list])/sum([a[1] for a in my_list])
     else
        return 0
