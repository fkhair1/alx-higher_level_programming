#!/usr/bin/python3
def weight_average(my_list=[]):
    print(sum([a[0]*a[1] for a in my_list])/sum([a[1] for a in my_list]))
