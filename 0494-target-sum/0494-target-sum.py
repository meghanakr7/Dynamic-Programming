class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if(abs(target) > sum(nums)):
            return 0
        targetSum = (target + sum(nums)) // 2
        if((target + sum(nums))%2):
            return 0
        table = [[0 for i in range(targetSum+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(targetSum+1):
                if(j == 0):
                    table[i][j] = 1
                elif(i == 0):
                    table[i][j] = 0
        for i in range(1, n+1):
            for j in range(targetSum+1):
                if(nums[i-1] <= j):
                    table[i][j] = table[i-1][j - nums[i-1]] + table[i-1][j]
                else:
                    table[i][j] = table[i-1][j]
        return table[n][targetSum]

