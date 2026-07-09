class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol_stk = []
        val_stk = []
        for tok in tokens:
            if tok.isdigit() or (tok[0] == '-' and tok[1:].isdigit()):
                val_stk.append(int(tok))
            else:
                b, a = val_stk.pop(), val_stk.pop()
                if tok == '+':
                    val_stk.append(a+b)
                elif tok == '-':
                    val_stk.append(a-b)
                if tok == '*':
                    val_stk.append(a*b)
                if tok == '/':
                    if b != 0:
                        val_stk.append(int(float(a)/b))
        return val_stk[-1]
                