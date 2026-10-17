class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wi = ai = 0
        digi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        wn = len(word)
        an = len(abbr)
        while ai < an and wi < wn:
            if abbr[ai] not in digi:
                if word[wi] == abbr[ai]:
                    wi += 1
                    ai += 1
                else:
                    return False
            else:
                comp = ''
                while ai < an and abbr[ai] in digi:
                    comp += abbr[ai]
                    ai += 1
                    if len(comp) == 1 and comp == '0':
                        return False
                comp = int(comp)
                wi += comp
                if wi > wn:
                    return False

        if ai == an and wi == wn:
            return True
        return False
