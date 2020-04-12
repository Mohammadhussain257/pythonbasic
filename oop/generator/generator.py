#  Memory Error will occurred
# l = [x*x for x in range(100000000000000000000000000000)]
# print(l)

# for the memory utilization generator concept is available

g = (x*x for x in range(10000000000000000000000000000000000))
while True:
    print(next(g))