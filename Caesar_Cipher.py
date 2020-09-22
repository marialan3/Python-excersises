def code(arg, jump):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    code_word = ""
    for x in arg:
        initial_position = alphabet.index(x)   # know the position of ATTACK in the alphabet
        jump_position = initial_position + jump   
        code_letter = alphabet[jump_position]
        code_word = code_word + code_letter    # add letter to the variable
    return code_word   

code("ATTACK", 3)  # jump = 3


def decode(arg, jump):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    decode_word = ""
    for x in arg:
        initial_position = alphabet.index(x)   
        jump_position = initial_position - jump    
        decode_letter = alphabet[jump_position]
        decode_word = decode_word + decode_letter    
    return decode_word   

decode("DWWDFN", 3)
