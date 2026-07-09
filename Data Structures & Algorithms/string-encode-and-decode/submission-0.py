class Solution:

    def encode(self, strs: List[str]) -> str:
        ward = "<endword>"
        s = ""
        for st in strs:
            s = s+st+ward
        return s

    def decode(self, s: str) -> List[str]:
        return s.strip().split("<endword>")[:-1]