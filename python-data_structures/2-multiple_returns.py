def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return length, first_char

# Test cases
sentence1 = "At Holberton school, I learnt C!"
length1, first1 = multiple_returns(sentence1)
print("Length: {:d} - First character: {}".format(length1, first1))

sentence2 = "Hello"
length2, first2 = multiple_returns(sentence2)
print("Length: {:d} - First character: {}".format(length2, first2))

sentence3 = "H"
length3, first3 = multiple_returns(sentence3)
print("Length: {:d} - First character: {}".format(length3, first3))

sentence4 = ""
length4, first4 = multiple_returns(sentence4)
print("Length: {:d} - First character: {}".format(length4, first4))
