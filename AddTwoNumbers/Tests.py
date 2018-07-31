import time

start = time.clock()
x = 0
for i in range(10000000):
    x = i / 1
end = time.clock()

print '/=',end-start

start = time.clock()
x = 0
for i in range(10000000):
    x -= -1
end = time.clock()

print '-=',end-start