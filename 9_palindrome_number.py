class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_list = list(str(x))
        if x < 0:
            return False
        elif len(input_list) % 2 == 0:
            part1_input_list = input_list[: len(input_list) // 2]
            part2_input_list = input_list[len(input_list) // 2 :]
            part2_input_list_reverse = part2_input_list[::-1]
            if part1_input_list != part2_input_list_reverse:
                return False
            else:
                return True
        else:
            for i, v in enumerate(input_list[int(len(input_list) / 2 - 1.5)]):
                if v != input_list[len(input_list) - i - 1]:
                    return False
            return True
