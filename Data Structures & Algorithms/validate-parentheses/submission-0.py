class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in "([{":
                st.append(c)
                
            elif c in ")]}":
                if not st:
                    return False

                top = st[-1]

                if ((c == ')' and top != '(') or
                    (c == '}' and top != '{') or
                    (c == ']' and top != '[')):
                    return False

                st.pop()

        return not st