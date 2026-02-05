def bit_stuffing(data):
    result = ""
    count = 0

    for bit in data:
        if bit == '1':
            count += 1
            result += bit
            if count == 5:
                result += '0'
                count = 0
        else:
            result += bit
            count = 0

    return result

data = "011111101"
print(bit_stuffing(data))
