from collections import Counter
def rearrange_by_frequency(nums: list[int]) -> list[int]:
    chastota=Counter(nums)

    result=sorted(nums,key=lambda x:(-chastota[x],[x]))
    return result
           
print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))

