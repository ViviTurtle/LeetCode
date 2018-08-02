import time

start = time.clock()
max_number = -1

for i in range(10000000):
    if i > max_number:
        max_number = i

end = time.clock()
print max_number
print 'If Max: ',end-start

max_number = -1

start = time.clock()
for i in range(10000000):
    max_number = max(i, max_number)
end = time.clock()
print max_number
print 'Max Number: ',end-start

max_number = -1
start = time.clock()
max_number = max([i for i in range(10000000)])
print max_number
end = time.clock()

print 'Max List: ',end-start

max_number = -1
listx = [i for i in range(10000000)]
start = time.clock()
max_number = max(listx)
print max_number
end = time.clock()

print 'Max List-Already-Made: ',end-start