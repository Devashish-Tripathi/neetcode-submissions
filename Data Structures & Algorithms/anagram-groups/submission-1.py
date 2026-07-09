class Solution:
    def isAnagram(self, str1, str2):
        if len(str1) ==  len(str2):
            if sorted([x for x in str1]) == sorted([x for x in str2]):
                return True
        return False
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDone = set()
        ans = []
        n = len(strs)
        for i in range(n):
            s1 = strs[i]
            if s1 in strDone: continue
            strans = [s1]
            for j in range(i+1, n):
                s2 = strs[j]
                if self.isAnagram(s1, s2):
                    strans.append(s2)
                    strDone.add(s2)
            ans.append(strans)
        
        return ans