class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        def findMax(k,row=True):
            mx = -inf
            idx = None
            if row:
                for i in range(m):
                    if mat[i][k] > mx:
                        mx = mat[i][k]
                        idx = i
            else:
                for j in range(n):
                    if mat[k][j] > mx:
                        mx = mat[k][j]
                        idx = j
            return mx,idx
        if m<n:
            l,r = 0,n-1
            while l<=r:
                mid = (l+r)//2
                lMx, lIdx = findMax(mid-1,True) if mid>0 else (-1,-1)
                mMx, mIdx = findMax(mid,True)
                rMx, rIdx = findMax(mid+1,True) if mid<n-1 else (-1,-1)
                if mMx>=lMx and mMx>=rMx:
                    return (mIdx,mid)
                elif mMx<lMx:
                    r = mid-1
                else:
                    l = mid+1
        else:
            l,r = 0,m-1
            while l<=r:
                mid = (l+r)//2
                lMx, lIdx = findMax(mid-1,False) if mid>0 else (-1,-1)
                mMx, mIdx = findMax(mid,False)
                rMx, rIdx = findMax(mid+1,False) if mid<m-1 else (-1,-1)
                if mMx>=lMx and mMx>=rMx: 
                    return (mid, mIdx)
                elif mMx<lMx:
                    r = mid-1
                else:
                    l = mid+1