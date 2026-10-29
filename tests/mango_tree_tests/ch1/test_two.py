import pytest 
from typing import List 

# Leetcode 15. 3Sum 
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = set()
    n = len(nums) 
    
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            triplet_sum = nums[i] + nums[l] + nums[r]
            if triplet_sum == 0:
                result.add((nums[i], nums[l], nums[r]))
                l+=1
                r-=1
            elif triplet_sum > 0:
                r-=1
            else:
                l+=1

    ans = []
    for r in result:
        r = list(r)
        ans.append(r)
    ans.sort()

    return ans

@pytest.mark.parametrize("nums, expected", [
    ([-1, -1, 3, -1, 2, 0], [[-1, -1, 2]]), 
    ([-1,0,1, 2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([], []),
    ([0,1,1], [])])
def test_threeSum(nums, expected):
    for e in expected:
        e.sort()
    expected.sort()
    assert threeSum(nums) == expected

