def best_score(a_dictionary):
    if a_dictionary:
        # Find the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None

# Test cases
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
