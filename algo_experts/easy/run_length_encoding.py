def runLengthEncoding(string):
    # Write your code here.
    
    counter = 1
    encoded = []
    current_char = string[0]
    for i in range(len(string)):

        if i == len(string) - 1:
            encoded.append("{}{}".format(counter, current_char))

        elif string[i+1] != current_char or counter == 9:
            encoded.append("{}{}".format(counter, current_char))
            counter = 1
            current_char = string[i + 1]
        else:
            counter += 1
    
    return "".join(encoded)
        