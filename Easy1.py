def length_of_last_word(s):
    s = s.rstrip()
    length = 0

    for char in reversed(s):
    
        if char == ' ':
            break
        
        else:
            length += 1

    return length


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))  
print(length_of_last_word("luffy is still joyboy"))  
