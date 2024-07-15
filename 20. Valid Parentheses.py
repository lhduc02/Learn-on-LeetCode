class Solution:
    def isValid(self, s: str) -> bool:
        while(1):
            if "()" in s or "[]" in s or "{}" in s:
                s = s.replace("()", "")
                s = s.replace("[]", "")
                s = s.replace("{}", "")
            else:
                print(s)
                if len(s) == 0:
                    return True
                return False
