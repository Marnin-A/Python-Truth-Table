# INSTRUCTIONS

# Design and implement a function that creates all possible combinations of truth values for a gven set of propositional variales eg,
# Given a list of propositional variables ['P','Q'], you would generate [[True, True], [True, False],[False, True], [False, False]],
# the boolean values should be in canonical order.
# In addition write a 150 word summary explaining the process you designed to a team member in a different field. 
# 1. Cal the max number of Rows needed in the truth table n variable => 2^n
# 2. Run a for Loop from zero to the number of rows
# 3. Create a binary number for the current row, pad the leading zeros
# 4. Convert all the 1's in the binary numbers to true strings and zeros to false strings
# 5. Append the true and false values to a list


# Step 1
variable_list =['P','Q','R','S']
number_of_rows = 2**len(variable_list)
print(number_of_rows)


# Step 2
# for i in range(number_of_rows):
#     print(i)

# Step 3
for i in range(number_of_rows):
    #print("The binary number for {} is {}".format(number_of_rows, bin(i) ))
    # current_binary= str(bin(i).[2:])
    # print(current_binary)
    widest_num_in_table= len(str(bin(number_of_rows-1)[2:]))
    print(bin(i)[2:].zfill(widest_num_in_table))
    current_binary = bin(i)[2:].zfill(widest_num_in_table)
    

print(widest_num_in_table)
    