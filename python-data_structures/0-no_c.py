def no_c(my_string):
    new_string = ''
    for i, char in enumerate(my_string):
        # Exclude 'c' and 'C' characters only from the beginning and end
        if char not in ('c', 'C') or (i == 0 and i == len(my_string) - 1):
            new_string += char
    return new_string

# Test cases
print(no_c("Holberton School"))           # Output: Holberton Shool
print(no_c("Chicago"))                     # Output: hiago
print(no_c("C is fun!"))                    # Output:  is fun!

# Additional test cases
print(no_c("Hellooosss"))                  # Output: Hellooosss
print(no_c("HellcCcccooccoscccss"))        # Output: HellcCcccooccoscccss