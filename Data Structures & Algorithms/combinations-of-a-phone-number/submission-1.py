class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        letter_digit = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def compute(i, cur_str):
            if len(cur_str) == len(digits):
                ans.append(cur_str)
                return
            for c in letter_digit[digits[i]]:
                compute(i + 1, cur_str + c)
        if digits:
            compute(0, "")
        return ans