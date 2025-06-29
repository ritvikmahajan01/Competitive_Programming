# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_by_line = [""]*numRows


        pos = 0
        down = True
        for i in range(len(s)):
            # print(pos)

            s_by_line[pos] += s[i]

            if pos < numRows-1 and down:
                pos += 1
            
            elif pos == numRows - 1 and down:
                pos -=1
                down = False

            elif pos > 0 and not down:
                pos -= 1

            elif pos == 0 and not down:
                pos += 1
                down = True

        ans = ""
        for i in range(numRows):
            ans += s_by_line[i]

        # print(ans)
        return ans



    

# sol = Solution()

# sol.convert("A", 1)