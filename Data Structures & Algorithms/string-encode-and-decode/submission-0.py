class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(strs)

    def decode(self, s: str) -> List[str]:
        import ast
        return ast.literal_eval(s)
