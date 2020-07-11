result = -1
starting = '10:00 14:00 10:00 15:00 10:00 13:00'
leaving = '17:00 22:00 14:00 21:00 17:00 22:00'

starting = starting.split(' ')
leaving = leaving.split(' ')
a = [(int(starting[i][:starting[i].index(':')]), int(leaving[i][:leaving[i].index(':')])) for i in range(len(starting))]
h = {i: set() for i in range(24)}
for hour in range(24):
    for i, t in enumerate(a):
        if t[0] <= hour < t[1]:
            h[hour].add(i)
x = set()
_max = 0
for hour in range(24):
    if len(h[hour]) > _max:
        _max = len(h[hour])
        x = {hour}
    elif len(h[hour]) == _max:
        x.add(hour)
result = len(x)
print(result)
