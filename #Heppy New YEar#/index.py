import time
from turtle import*

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy New Year!')

bgcolor('black')
tracer(100)
c = ['red', 'orange', 'blue', 'green', 'blue', 'white']
for i in range(700):
    color(c[i%6])
    fd(7)
    lt(88)
    fd(i*3)
    circle(10)
    lt(59)
done()