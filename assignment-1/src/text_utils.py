def char_to_num(char):
    if char == ' ':
        return 26
    return ord(char) - ord('a')

def num_to_char(num):
    if num == 26:
        return ' '
    return chr(num + ord('a'))

def text_to_numbers(text):
    text = text.lower()

    text = text.replace('lj', 'l j')
    text = text.replace('nj', 'n j')
    text = text.replace('dž', 'd z')

    cleaned_text = ''
    for char in text:
        if 'a' <= char <= 'z' or char == ' ':
            cleaned_text += char

    numbers = []
    for char in cleaned_text:
        numbers.append(char_to_num(char))

    return numbers

def numbers_to_text(numbers):
    text = ''
    for num in numbers:
        text += num_to_char(num)
    return text

def prepare_text_blocks(numbers, block_size=4):
    while len(numbers) % block_size != 0:
        numbers.append(26)

    blocks = []
    for i in range(0, len(numbers), block_size):
        block = []
        for j in range(block_size):
            block.append([numbers[i + j]])
        blocks.append(block)

    return blocks

def blocks_to_numbers(blocks):
    numbers = []
    for block in blocks:
        for row in block:
            numbers.append(row[0])
    return numbers
