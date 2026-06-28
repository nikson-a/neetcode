class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for _str in strs:
            i = "".join(sorted(_str))
            data.setdefault(i, [])
            data[i].append(_str)
        return(list(data.values()))
        