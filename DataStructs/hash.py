"""
collisons:
when hash function assigns same index for 2 keys --> collision


to solve, solutions:

1. linear probing: assigned next available index. Why not good, it will just start a chain reaction aka CLUSTERING
makes everything o(n)

2. Seperate chaning: hash table is array of pointers to linked list. o(n/k) --> big good in real world (k is size of hash table)

"""
