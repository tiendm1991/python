# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:08:24 2019

@author: TienDM
"""
def DivisionPossible(array, division):
    s = sum(array)
    if s % division != 0:
        return False
    avg = s/division
    sub = [0] * division
    array = sorted(array)
    visited = [False] * len(array)
    return help(array, sub, visited, avg,  0)
    return True
def help(array, sub, visited, avg, idx):
    #print(visited)
    #print(sub)
    d = len(sub)
    n = len(array)
    if idx == d:
        return True
    checked = False
    for i in range(n):
        if visited[i]:
            continue
        sub[idx] += array[i]
        visited[i] = True
        if sub[idx] == avg:
            checked = help(array, sub, visited, avg, idx+1)
        elif sub[idx] < avg:
            checked = help(array, sub, visited, avg, idx)
        if checked:
            return True
        sub[idx] -= array[i]
        visited[i] = False
    return False
