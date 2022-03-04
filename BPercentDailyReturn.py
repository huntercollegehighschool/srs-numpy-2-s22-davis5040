""" 
Percent Daily Return Exercise

In this exercise, you are given the stock values for several consecutive days for acme corporation. Your job is to calculate the "percent daily return" for each day. The percent daily return is the percentage that the stock changes each compared to the day before.

Note: the percent daily return = 100 * (current day - previous day)/previous day

Below you are given the stock prices (there are only 4 days in this example). First convert to a numpy array. Then use slicing and numeric operations to calculate the percent daily return (no for loops!).
"""
import numpy as np

acme = [10, 11.5, 11, 10, 12]
acme = np.array(acme)
print(100*(acme[1] - acme[0])/acme[0])
print(100*(acme[2] - acme[1])/acme[1])
print(100*(acme[3] - acme[2])/acme[2])
print(100*(acme[4] - acme[3])/acme[3])