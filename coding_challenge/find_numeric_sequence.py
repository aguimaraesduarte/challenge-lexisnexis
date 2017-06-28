Write a program that has as input a string that can be of any size. The program should look for sequences of *at least* four numerical character in a row and return the starting and ending position of each occurrence. The output data format/structure decision is up to you.
i.e: 
Input = "xx0ab1234567c6709b245"
Output = [(5,11),(13,16)] (5 is the position of the character '1', 11 is the position of the character '7' which is the last character of the first numerical sequence).
Same thing applies for 13 and 16 which are the first and last position of the beginning and end of the second numerical sequence.

"""
Find and return sequences of at least 4 numerical characters in a row from the input string.
@input: in_string is a string of characters
@output: list of tuples in the form (begin, end) with the positions of start and end of the numerical characters
"""
def find_numeric_sequence(in_string):
    # return blank list if in_string is not a string or empty string
    if ((not isinstance(in_string, basestring)) or (len(in_string) == 0)):
        return []
    else:
        # create return list
        output = []
        numericals = []
        # create all substrings from in_string
        sub_strings = [in_string[i:] for i in range(len(in_string))]
        # iterate through all the substrings and find the ones that start with a numerical character
        # append these indices to numericals
        for idx, sub in enumerate(sub_strings):
            if sub[0].isdigit():
                numericals.append(idx)
        # at this point, numericals has a list of all indices that contain digits
        # we now need to filter to ranges that are greater than four consecutive numbers, and keep
        # only the start and end positions as tuples
        ## 1. get the break points of numericals (the positions at which the sequence ends)
        breaks = [pos1+1 for pos1, pos2 in zip(numericals, numericals[1:]) if pos2-pos1 != 1]
        # the above won't catch the last element if it's numerical, so we add it back if it's a number
        if str(numericals[-1]).isdigit():
            breaks.append(len(in_string))
        ## 2. trim and store to output list
        # starting index
        k = 0
        for b in breaks:
            # get sub-list for at each break-point
            test_output = [n for n in numericals[k:] if n<b]
            # only save it if it has at least 4 characters
            if len(test_output) >= 4:
                output.append((test_output[0], test_output[-1]))
            # increase the starting index by however many characters were in the previous test_output list
            k += len(test_output)
        return output