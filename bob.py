# print the number of times bob appears in a string

# s is once again lowercase

def sub_string(src, target):
    current_index = src.find(target) 
    count = 0
    while True: 
        if current_index == -1:
            break
        count += 1
        current_index = src.find(target, current_index + 1)
    return count
