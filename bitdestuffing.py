def bit_destuffing(data):
    result = ""
    count = 0
    i = 0

    while i < len(data):
        if data[i] == '1':
            count += 1
            result += data[i]
            if count == 5:
                i += 1  # skip the stuffed 0
                count = 0
        else:
            result += data[i]
            count = 0
        i += 1

    return result

data = "0111110101"
print(bit_destuffing(data))
