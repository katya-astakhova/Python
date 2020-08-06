import sys

def salary(hours, rate, reward):
    sal = (hours * rate) + reward
    print(sal)


h = int(sys.argv[1])
r = int(sys.argv[2])
rew = int(sys.argv[3])
salary(h, r, rew)
