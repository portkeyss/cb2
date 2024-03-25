class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = Counter(set(nums1))+Counter(set(nums2))+Counter(set(nums3))
        return [x for x,v in counter.items() if v>1]
        