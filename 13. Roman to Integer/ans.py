# def create_special_roman_int_map(roman_int_map: dict[str, int]) -> dict[str, int]:
#     key_list = list(roman_int_map.keys())
#     special_roman_int_map = {}
#     for index, roman in enumerate(key_list):
#         if len(key_list) - 3 < index:
#             break

#         next_roman = key_list[index + 1]
#         two_next_roman = key_list[index + 2]

#         value = roman_int_map[roman]
#         next_value = roman_int_map[next_roman]
#         two_next_value = roman_int_map[two_next_roman]

#         special_roman_int_map[f"{roman}{next_roman}"] = next_value - value
#         special_roman_int_map[f"{roman}{two_next_roman}"] = two_next_value - value

#     return special_roman_int_map


class Solution:
    def __init__(self):
        self.roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        self.special_roman_int_map = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

    def romanToInt(self, s: str) -> int:
        _sum = 0
        while len(s) > 0:
            sub_int = self.check_sub(s)
            if sub_int != 0:
                _sum += sub_int
                s = s[2:]
            else:
                target_s = s[0]
                _sum += self.roman_int_map[target_s]
                s = s[1:]
        return _sum

    def check_sub(self, s: str) -> int:
        if len(s) < 2:
            return 0

        target_s = s[:2]
        return self.special_roman_int_map.get(target_s, 0)


print(Solution().romanToInt("MCDLXXVI"))
