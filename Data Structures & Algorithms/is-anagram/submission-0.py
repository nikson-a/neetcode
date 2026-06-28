class Solution:

    def find_letter_count(self, dt):
        data = {}
        for i in dt:
            data.setdefault(i, 0)
            data[i] += 1
        return data
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.find_letter_count(s) == self.find_letter_count(t)
        
