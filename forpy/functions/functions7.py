def has33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

print(has33([1, 3, 3]))
print(has33([1, 3, 1]))