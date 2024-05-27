def reverse_strings (s):
    if len(s) <= 1:
        return s
    else:
        last_word = s[len(s)-1:]
        remaining_word = s[:len(s) - 1]
        return last_word + reverse_strings(remaining_word)
    
print (reverse_strings("hello"))
print (reverse_strings("python"))
