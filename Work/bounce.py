# bounce.py
#
# Exercise 1.5
bounce = 100
for i in range(10):
    bounce *= 3 / 5
    print(i + 1, round(bounce, 4))