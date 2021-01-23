# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:17:43 2020

@author: samson
"""
import random

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B'],
    'B' : ['C', 'D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

frontier = ['A']
goalState = ['E']
visited = [] 


def loop():
    if not frontier:
        return
    l=frontier.pop(random.randint(0,len(frontier)-1))
    if l == goalState:
        return
    visited.append(l)
    for neighbour in graph[l]:
        if neighbour not in frontier and neighbour not in visited:    
            frontier.append(neighbour)
    loop()

frontier1 = ['A']
goalState1 = ['E']
visited1 = [] 

def dfs():
    if not frontier1:
        return
    l=frontier1.pop()
    if l == goalState1:
        return
    visited1.append(l)
    for neighbour in graph[l]:
        if neighbour not in frontier1 and neighbour not in visited1:    
            frontier1.append(neighbour)
    dfs()
    
frontier2 = ['A']
goalState2 = ['E']
visited2 = [] 

def bfs():
    if not frontier2:
        return
    l=frontier2.pop(0)
    if l == goalState2:
        return
    visited2.append(l)
    for neighbour in graph[l]:
        if neighbour not in frontier2 and neighbour not in visited2:    
            frontier2.append(neighbour)
    bfs()
    
loop()
print("LOOP SEQUENCE: ",visited)
dfs()
print("DFS SEQUENCE: ",visited1)
bfs()
print("BFS SEQUENCE: ",visited2)