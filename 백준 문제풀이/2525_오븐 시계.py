hour = input()
rhour = hour.split(maxsplit = 2)
rhour[0], rhour[1] = int(rhour[0]), int(rhour[1])
min = int(input())

rhour[1] += min

while rhour[1] >= 60:
    rhour[1] -= 60
    rhour[0] += 1

if rhour[0] >= 24:
    rhour[0] -= 24

print(rhour[0], rhour[1])