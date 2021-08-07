import pyfiglet
logo = pyfiglet.figlet_format("CAESAR CIPHER")
print(logo)
print('''
version : 0.0.2
Developed by Nassim.L
github : https://github.com/Nassim-L
''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text , shift_amount):
    cipher_txt = ''
    for letter in plain_text:
        if letter in alphabet:
            
            position = alphabet.index(letter)
            newposition = position + shift_amount
        
            if newposition >=25:
                newpositionV2 = newposition%25 -1
                newletter = alphabet[newpositionV2]
                cipher_txt += newletter
            
            else:
                newletter = alphabet[newposition]
                cipher_txt += newletter 
                
        else:
            newletter = letter
            cipher_txt += newletter 
            
    print(f'Your message : {plain_text}')
    print(f'Your encrypted message :{cipher_txt}')
    
     
def decrypt(plain_text , shift_amount):
    cipher_txt = ''
    for letter in plain_text:
        if letter in alphabet:
            
            position = alphabet.index(letter)
            newposition = position - shift_amount
        
            if newposition >=25:
                newpositionV2 = newposition%25 +1
                newletter = alphabet[newpositionV2]
                cipher_txt += newletter
            
            else:
                newletter = alphabet[newposition]
                cipher_txt += newletter 
                
        else:
            newletter = letter
            cipher_txt += newletter  
            
        
    print(f'Your crypted message : {plain_text}')
    print(f'Your decrypted message : {cipher_txt}')
    
def ceaser(text,shift, direction):
    
    
        
    if direction == "encode":
        encrypt(text,shift)
    
    
    if direction =='decode':
        decrypt(text,shift)
        
statu = True  
while statu :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction) 
    answar = input("Write 'Yes' to Contirnue and 'No'to stop ")
    if answar.lower() == 'no'  :
        statu = False
        
        
    if answar.lower() == 'yes' :
        statu = True
        
        
        
    
    
    


            






