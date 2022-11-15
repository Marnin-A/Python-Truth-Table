# INSTRUCTIONS

# Design and implement a function that creates all possible combinations of truth values for a given set of propositional variables eg,
# Given a list of propositional variables ['P','Q'], you would generate [[True, True], [True, False],[False, True], [False, False]],
# the boolean values should be in canonical order.
# In addition write a 150 word summary explaining the process you designed to a team member in a different field. 
# 1. Cal the max number of Rows needed in the truth table n variable => 2^n
# 2. Run a for Loop from zero to the number of rows
# 3. Create a binary number for the current row, pad the leading zeros
# 4. Convert all the 1's in the binary numbers to true strings and zeros to false strings
# 5. Append the true and false values to a list


# Create variable list
variable_list =['P','Q','R','S']

# Calculate number of rows
number_of_rows = 2**len(variable_list)

# Create a for-loop to convert all decimal integers from 0 to the number
# of rows to binary
# Set the for loop to iterate backwards
for i in range(number_of_rows)[::-1]:
    # Determine the length of the longest binary number
    widest_num_in_table= len((bin(number_of_rows-1)[2:]))

    #  Remove the first two characters, and add padding
    #  to the remaining value
    current_binary = (bin(i)[2:].zfill(widest_num_in_table))
    
    #  Convert the binary to arrays of 0's and 1's
    result = [int(x) for x in str(current_binary)]
    
    #  Convert the 0's and 1's to True and False strings
    result = [bool(y) for y in result]

    print((str(result)))
    
