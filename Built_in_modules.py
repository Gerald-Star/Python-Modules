
# Math module

import math 

print(math.pi)

math.sqrt(16)

root = math.sqrt(16)
print(root)


# Random module

import random

print(random.randint(0, 100))

print(random.random())

print(random.randrange(0, 101, 2))

print(random.choice([1, 2, 3, 4, 5]))

print(random.choices([1, 2, 3, 4, 5], k=2))

print(random.sample([1, 2, 3, 4, 5], k=3))


# Datetime module

import datetime

x = datetime.datetime.now()

print(x)

print(x.year) # 2024

print(x.strftime("%A")) # Friday

print(x.strftime("%B")) # April

print(x.strftime("%c")) # Fri Apr 12 14:59:00 2024

print(x.strftime("%x")) # 04/12/24

print(x.strftime("%X")) # 14:59:00


print()
# OS module

import os

print(os.getcwd())

os.mkdir("new_dir")

os.chdir("new_dir")

print(os.getcwd())

os.chdir("..")

os.rmdir("new_dir")

print(os.getcwd())



print()
# Sys module

import sys

print(sys.path)

print(sys.version)


print()

import platform

x = platform.system()
print(x)


x = platform.python_version()

print(x)

x = dir(platform)
print(x)


