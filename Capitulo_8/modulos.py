# Módulos internos
import math
import random
import statistics
import keyword

print(math.pow(2,3))
print(random.randint(0,100))

# media
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# mediana
print(statistics.median(nums))

# moda
print(statistics.mode(nums))

print(keyword.iskeyword('for'))
print(keyword.iskeyword('football'))