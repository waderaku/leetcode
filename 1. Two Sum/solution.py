# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 各数とその個数の辞書作成
        nums_dict = {}
        [nums_dict.update({num: nums_dict.get(num, 0) + 1}) for num in nums]

        for index, num in enumerate(nums):
            match_num = target - num

            # 辞書の中から今回のnumを一つ取り出す（数を減らす）
            nums_dict.update({num: nums_dict.get(num, 0) - 1})

            # 合計がtargetになるような片割れの値があった辞書内にあった場合、成功
            if nums_dict.get(match_num, 0) != 0:
                return [index, nums.index(match_num, index + 1)]
