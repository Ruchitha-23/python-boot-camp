'''h/w print ABC example take XYZ'''


s= "XYZ"
z= ""
for char in s:
    ascii_value = ord(char)
    new_ascii_value = ascii_value - 23
    new_char = chr(new_ascii_value)
    z+= new_char
print(z)