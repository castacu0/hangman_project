def binary_search(sequence, item):
    begin_i = 0
    end_i = len(sequence) - 1 #12-1

    while begin_i <= end_i:
        midpoint = begin_i + (end_i - begin_i) // 2

        midpoint_valueX = sequence[midpoint]
        if midpoint_valueX == item:
            return midpoint

        elif item < midpoint_valueX:
            end_i = midpoint - 1

        else:
            begin_i = midpoint + 1

    return f"I don't have that number."

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
num = 10

result = binary_search(sequence_a, num)
print(f"Your numbers is in the index position: {result}")