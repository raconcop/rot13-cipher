def encrypt(text):
    text = text.lower()
    encrypted_text = ""
    
    
    for char in text:
        num = ord(char)
        if (num <= 109):
                num += 13
                encrypted_text += chr(num)
        elif (num > 109):
                num -= 13
                encrypted_text += chr(num)
    return(encrypted_text)

msg = "hellothere"
enc = encrypt(msg)
print(enc)
