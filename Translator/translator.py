def encode_binary_string(s, encoding='UTF-8'):
    return ' '.join(format(ord(x), 'b') for x in s)
    

def BinaryToDecimal(binary):    
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)

def decode_binary_string(s):
    string = s.replace(' ','')
    print(string)
    str_data =''
    for i in range(0, len(string), 7): 
        temp_data = int(string[i:i + 7]) 
        decimal_data = BinaryToDecimal(temp_data) 
        str_data = str_data + chr(decimal_data)
    return(str_data)




