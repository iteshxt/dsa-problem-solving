class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)  # handle multi-digit numbers
            elif c == "[":
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif c == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += c
        
        return curr_str
