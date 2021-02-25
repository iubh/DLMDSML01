# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:30:49 2019

@author: Markus Pak 
"""

import time
import multiprocessing

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(L,x):
    y = x*x
    time.sleep(2)
    L.append(y)
    print('{} squared results is a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    v = [];

    with multiprocessing.Manager() as manager:
        L = manager.list()
        for i in range(0,100):
            p = multiprocessing.Process(target=multiprocessing_func, args=(L,i))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()
        print(L)

    # print('The vector is...:')
    # print(L)
    print('That took {} seconds'.format(time.time() - starttime))
