def majority_element(nums: list[int]) -> int:
    
    """
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """

    ele = cnt = 0

    for i in nums:
        if cnt == 0:
            ele = i
        if ele == i:
            cnt += 1
        else:
            cnt -= 1

    return ele


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
