class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetSum = 0
        n = len(nums)
        if(sum(nums) %2 == 1):
            return False
        else:
            targetSum = sum(nums)//2
        table = [[-1 for j in range(targetSum+1)] for i in range(n+1)]
        for i in range(n+1):
            for j in range(targetSum+1):
                if(i == 0):
                    if(j == 0):
                        table[i][j] = True
                    else:
                        table[i][j] = False
                if(j == 0):
                    if(i == 0):
                        table[i][j] = True
                    else:
                        table[i][j] = False
        def bottomUp(nums, n, targetSum):
            for i in range(1,n+1):
                for j in range(1,targetSum+1):
                    if(j >= nums[i-1]):
                        table[i][j] = table[i-1][j-nums[i-1]] or table[i-1][j]
                    else:
                        table[i][j] = table[i-1][j]
        bottomUp(nums, n, targetSum)
        return table[n][targetSum]