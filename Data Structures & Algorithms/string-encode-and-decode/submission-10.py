class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(len(strs)) + "<#>" + "<#>".join(strs)

    def decode(self, s: str) -> List[str]:
        s = s.split("<#>")
        if s[0] == "0":
            return []
        return s[1:]
