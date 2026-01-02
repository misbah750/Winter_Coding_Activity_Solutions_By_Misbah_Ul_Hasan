import math 

def cal_impact(contributions):
    impact = []
    for i in range(len(contributions)):
        right = math.prod(contributions[i + 1 :])
        left = math.prod(contributions[: i])
        impact.append(left * right)
    return impact

print(cal_impact([1, 2, 3, 4]))
print(cal_impact([-1, 1, 0, -3, 3]))