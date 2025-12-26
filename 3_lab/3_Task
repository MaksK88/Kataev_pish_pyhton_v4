block_size = 3
result = []
for i in range(0, len(array), block_size):
    block = array[i:i + block_size]
    if len(block) == block_size:
        result.extend(block[::-1])
    else:
        result.extend(block)
print(result)