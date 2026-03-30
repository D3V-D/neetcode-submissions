class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "#️⃣" 
        res = ""
        for i, s in enumerate(strs):
            res += s
            if  i != len(strs) - 1:
                res += "🎬"
        return res
    def decode(self, s: str) -> List[str]:
        if s == "#️⃣":
            return []
        return s.split("🎬")
