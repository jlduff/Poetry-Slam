from random import choice 

def get_file_lines(filename): 
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines 

def lines_printed_backwards(lines_list): 
    lines_list.reverse()
    lines_length = len (lines_list)
    for i in range (lines_length): 
        line = lines_list[i]
        line_num = lines_length - i 
        print(f"{line_num}{line}")


