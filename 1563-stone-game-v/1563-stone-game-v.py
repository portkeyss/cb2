class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0]
        for x in stoneValue:
            prefix.append(prefix[-1]+x)
        
        @lru_cache(None)
        def f(i,j):#returns (reward, maxLeft, maxRight, mid1,mid2),where mid1 is the max k1 for [i,k1] to ensure smaller(or equal) left interval, mid2 is the min k2 for [k2,j] to ensure smaller(or equal) right interval. In fact mid1+1==mid2 always holds for interval length>=2, this redundancy is for the convenience of coding only
            if i==j:
                return (0,0,0,i-1,j+1)
            _, maxLeft, _,mid1,_ = f(i,j-1)
            _, _,maxRight,_,mid2 = f(i+1,j)
            mid1 += 1
            while mid1<j and prefix[mid1]-prefix[i-1]<=prefix[j]-prefix[mid1]:
                maxLeft = max(maxLeft,prefix[mid1]-prefix[i-1]+f(i,mid1)[0])
                mid1 += 1
            mid1 -= 1
            mid2 -= 1
            while mid2>i and prefix[j]-prefix[mid2-1]<=prefix[mid2-1]-prefix[i-1]:
                maxRight = max(maxRight,prefix[j]-prefix[mid2-1]+f(mid2,j)[0])
                mid2 -= 1
            mid2 += 1
            reward = max(maxLeft, maxRight)
            return reward,maxLeft,maxRight, mid1,mid2
        
        return f(1,len(prefix)-1)[0]