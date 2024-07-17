import time

n, m, k = map(int, input().split())
numArr = [int(x) for x in input().split()]
numArr.sort()
output = 0
count = 1

start_time = time.time()
for i in range(m):
    if count <= k:
        output += numArr[-1]
        count += 1
    elif count > k:
        output += numArr[-2]
        count = 1

print(output)
end_time = time.time()

elapsed_time = end_time - start_time
print("걸린 시간: {:.5f}초".format(elapsed_time))