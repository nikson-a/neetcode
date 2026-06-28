class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for n in nums:
            data.setdefault(n, 0)
            data[n] += 1
        
        # Sort elements by their frequency in descending order
        sorted_elements = sorted(data.keys(), key=lambda x: data[x], reverse=True)
        
        # Return the first k elements
        return sorted_elements[:k]