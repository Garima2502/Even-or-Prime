# -*- coding: utf-8 -*-
"""Ques1-whether even or prime

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qAn1ipg0eVYO598C7jKBy1fS9PiAi8na
"""

import numpy as np

random_numbers = list(np.random.randint(low=13,high=789,size=100))

even = list()

prime = list()

for num in random_numbers:

  if num %2 == 0 :
    even.append(num)
  else:
    for divisor in range(2,num):
      if num % divisor == 0:
        break
if divisor == (num-1):
        prime.append(num)

print(even)

print(prime)

