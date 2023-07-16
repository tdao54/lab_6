
def password_encode(password):
    encode_pass = ""
    for i in password: #for each char in password str 
        i = int(i) + 3  #convert to int and add 3 
        if i >= 10: #if i is over 10 goes back to 0 and adds remainder
            i = i - 10
        encode_pass += str(i)
    return encode_pass 

def password_decode(password):
    decode_pass = ""
    for i in password:  # for each char in password str
        i = int(i) - 3  # convert to int and add 3
        if i < 0:  # if i is 0 or less, i adds 10
            i = i + 10
        decode_pass += str(i)
    return decode_pass

if __name__ =='__main__':
    while True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1: #encode option
            password = input('Please enter your password to encode: ')
            encoded_password = (password_encode(password))
            print('Your password has been encoded and stored!\n')
        elif option == 2: #decode option
            try:
                decoded_password = (password_decode(encoded_password))
                print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')
            except NameError:
                print("You did not enter a password to encode!")
        elif option == 3:
            break 
