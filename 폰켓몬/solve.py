def solution(nums):
    types = [] # different kinds of ponkemons in nums

    for mon in nums:
        if mon not in types:
            types.append(mon)

    if len(types) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(types)