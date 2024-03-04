def encode_message(code, message):
    message = message.upper()
    code = code.upper()
    encoded_message = ""
    alphabet = []
    hashset = []
    #vytvorí list so všetkými pismenami abecedy a pridá code do šifry
    for i in range(0, 26):
        alphabet.append(chr(i+65)) 
        if (i)<(len(code)):
            hashset.append(code[i]) 

    #doplní chybajúce pismená do konca abecedy do šifry
    for i in range(ord(code[len(code)-1])+1, 91):
        if code.find(chr(i))==-1:
            hashset.append(chr(i))   

    #doplní chybajúce pismená z abecedy do šifry
    for i in range(len(hashset), 26):
        for a in range(65, 91):
            if chr(a) not in hashset:
                hashset.append(chr(a))  

    #zašifruje správu 
    for a in message:
        encoded_message =  encoded_message + hashset[alphabet.index(a.upper())]

    """
    Encode a message by shifted substitution table
    :param str code: code word to create shifted substitution table
    :param message: message to be encoded
    :rtype: str
    :return: encoded message
          print(ord(code[len(code)-1]))
            hashset.append(chr((i+ord(code[len(code)-1]))))
    """
    ...

    return encoded_message


if __name__ == "__main__":
    code = "ALGORITMUS"
    message = "hello"
    encoded_message = encode_message(code, message)
    print(encoded_message)
