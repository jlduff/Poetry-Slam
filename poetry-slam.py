from random import choice 

def get_file_lines(filename): 
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines 

print(get_file_lines("poem.txt"))

def lines_printed_backwards(lines_list): 
    lines_list.reverse()
    lines_length = len (lines_list)
    for i in range (lines_length): 
        line = lines_list[i]
        line_num = lines_length - i 
        print(f"{line_num}{line}")

# The above function will print the lines of the poem.txt file in 
# backwards order

def lines_printed_random(lines_list):
    for lines in lines_list:
        print(choice(lines_list))

# The lines_printed_random function creates a random-ordered print
# out of the same lines list 

def lines_printed_custom(lines_list):
    lines_length = len(lines_list)

    for i in range(len(lines_list)):
        if i % 10 == 0:
            print(lines_list[i])

# The above function prints every tenth line of the poem.txt file 

