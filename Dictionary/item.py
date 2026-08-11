dist = {'delhi': 1000, 'Mumbai': 2000}

result = {}

for key, value in dist.items():
    result[key] = value * 0.62

print(result)