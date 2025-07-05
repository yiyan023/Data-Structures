def fewerThanTargetDistinct(arr: list[int], target: int) -> bool:
    return len(set(arr)) < target

print(fewerThanTargetDistinct([1,2,2,3,3], 3) == False)
print(fewerThanTargetDistinct([1,2,2,3,4], 3) == False)
print(fewerThanTargetDistinct([1,1,2,2,2], 3) == True)
print(fewerThanTargetDistinct([9], 1) == False)
print(fewerThanTargetDistinct([9], 2) == True)
print(fewerThanTargetDistinct([8,8,8], 1) == False)
print(fewerThanTargetDistinct([8,8,8], 2) == True)
print(fewerThanTargetDistinct([8,8,8], 3) == True)
print(fewerThanTargetDistinct([6,7,8,9], 1) == False)
print(fewerThanTargetDistinct([6,7,8,9], 2) == False)
print(fewerThanTargetDistinct([6,7,8,9], 3) == False)
print(fewerThanTargetDistinct([6,7,8,9], 4) == False)
print(fewerThanTargetDistinct([6,7,8,9], 5) == True)
