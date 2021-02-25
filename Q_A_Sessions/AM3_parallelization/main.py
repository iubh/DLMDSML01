# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:22:31 2019

@author: Markus Pak 
"""

import time

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'
 
    
def main():
    
    starttime = time.time()
    for i in range(0,10):
        y = i*i
        time.sleep(2)
        print('{} squared results is a/an {} number'.format(i, basic_func(y)))
        
    print('That took {} seconds'.format(time.time() - starttime))
    
if __name__ == '__main__':
    main()