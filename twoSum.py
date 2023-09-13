#----------Solution 1-------#
nums = [2,7,11,15]
target = 9
nums_dict = {}
for i,j in enumerate(nums):
    remainder = target - j
    if remainder in nums_dict:
        print (nums_dict[remainder], i)
    nums_dict[j] = i
# --------Solution 2---------#
# seen = [2,7,11,15]
# ans = []
# for i in range(len(nums)):
#     # target-nums[i]
#     # 9-nums[0] -> 9-2=7
#     if target-nums[i] in seen:
#         ans.append([i, nums.index(target-nums[i])])
# print(ans[0])