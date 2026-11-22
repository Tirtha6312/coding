class Solution:
    def checkString(self, s: str) -> bool:
        bseen = False
        for c in s:
            if c == 'a':
                if bseen:
                    return False
            else:
                bseen = True
        return True