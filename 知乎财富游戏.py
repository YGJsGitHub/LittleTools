# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# author:ygj time:2020/10/10


import matplotlib.pyplot as plt
import numpy as np
import random
import time

round = 2000000
interval = 1000
index = list(range(0, 100))
wealth = np.zeros(100, dtype=float) + 100
wealthchange = [1, 1, 1, -1, -1, -1]


plt.ion()
plt.figure(1)
for i in range(round):
    changelist = random.sample(index, 6)
    wealth[changelist] = wealth[changelist] + wealthchange
    if i % interval == 0:
        plt.clf()
        print('Epoch:', i)
        plt.bar(index, np.sort(wealth))
        plt.draw()
        plt.pause(0.1)