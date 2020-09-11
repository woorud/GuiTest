import numpy as np
import random
data = open('Sudokunums.txt', 'r')
lines = data.read()
nums = []
for line in lines:
    if line != '\n':
        nums.extend(line)
nums = np.array(nums)
nums = nums.reshape(9, 9)

random19 = list(range(1, 10))
random.shuffle(random19)

# print(nums)
print(random19)

for i in range(9):
    for j in range(9):
        tmp = int(nums[i][j]) - 1
        if random.random() < 0.7:
            nums[i][j] = str(random19[int(nums[i][j]) - 1])
        else: # 30% 확률로 공백
            nums[i][j] = ' '
print(nums)