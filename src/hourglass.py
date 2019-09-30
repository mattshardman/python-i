def line_sum(a, i):
    return sum(a[i:i + 3])

def hourglassSum(arr):

    totals = []

    for (line_i, line) in enumerate(arr):
        if line_i <= 3:
            for (item_i, item) in enumerate(line):
                if item_i < len(line) - 3:
                    one = line_sum(line, item_i)
                    two = arr[line_i + 1][item_i + 1]
                    three = line_sum(arr[line_i + 2], item_i)
                    totals.append(sum([one,two,three]))

    return sorted(totals, reverse=True)[0]

arr = [
    [1,1,1,0,0,0],
    [0,1,9,0,0,0],
    [1,9,9,0,0,0],
    [1,9,9,0,0,0],
    [1,9,9,0,0,0],
    [1,9,9,0,0,0]
]

result = hourglassSum(arr)
print(result)