class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        paths = path.split('/')
        for path in paths:
            if path == '.' or path == "":
                continue
            elif path == '..':
                if stk: stk.pop()
            else:
                stk.append(path)
        return '/'+'/'.join(stk)