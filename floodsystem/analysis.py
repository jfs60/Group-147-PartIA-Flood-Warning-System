import matplotlib
import numpy as np
import matplotlib.dates as dates

#Task2F
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x1= x[0]
    x = x-x1
    p_coeff = np.polyfit(x, levels, p)
    poly = np.poly1d(p_coeff)
    return poly,x1
    
