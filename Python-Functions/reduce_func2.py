import functools # This code find min ele in given list
print(functools.reduce(lambda x,y:x if x < y else y,[23,4,66]))