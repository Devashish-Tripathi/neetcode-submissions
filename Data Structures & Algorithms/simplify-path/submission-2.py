class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path = path.split('/')
        for pt in path:
            if pt == '..':
                if stk:
                    stk.pop()
            elif pt != '' and pt != '.':
                stk.append(pt)
        
        return '/' + '/'.join(stk) 