d = {'phone':0,'laptop':122,'airpod':33}
empty = {}
for i in d:
    if d[i] > 0:
        empty[i] = d[i] 

print(empty)