import binascii, base64;

def hex2base64(hex_string):
    newbyte = str.encode(hex_string);
    newhex = binascii.unhexlify(newbyte);
    base64string = base64.b64encode(newhex).decode('ascii');
    return base64string;

hexstring = input("Please enter a hex string \n");
base64string = hex2base64(hexstring);
print("The base 64 encoded string is ", base64string);

