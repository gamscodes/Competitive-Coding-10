class Solution:
    # Approach: Use a monotonic stack to greedily remove digits that make the number larger.
    # TC: O(N), where N is the length of num
    # SC: O(N), for the stack to hold digits
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        # If k still > 0, remove from end
        stack = stack[: len(stack) - k] if k > 0 else stack

        # Join stack into string and remove leading zeros manually
        res = "".join(stack)
        for i in range(len(res)):
            if res[i] != "0":
                res = res[i:]
                break
        else:
            res = ""

        return res if res else "0"


sol = Solution()
print(sol.removeKdigits("1432219", 3))  # Output: "1219"
print(sol.removeKdigits("10200", 1))  # Output: "200"
print(sol.removeKdigits("10", 2))  # Output: "0"
