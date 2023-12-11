def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return length, first_char

# Test case
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))