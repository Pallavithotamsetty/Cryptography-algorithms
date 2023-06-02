def encryption(msg):
    msg=msg.upper()
    msg=msg.replace(" ","")
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k=input("Enter the key value:")
    msg=list(msg)
    k1=convert_k(k,len(msg))
    k1=list(k1.upper())
    encrypt=""
    for i in range(len(msg)):
        encrypt+= l[(l.index(msg[i])+l.index(k1[i]))%26]
    print(encrypt)
def decryption(msg):
    msg=msg.upper()
    msg=msg.replace(" ","")
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k=input("Enter the key value:")
    msg=list(msg)
    k1=convert_k(k,len(msg))
    k1=list(k1.upper())
    decrypt=""
    for i in range(len(msg)):
        decrypt+= l[(l.index(msg[i])-l.index(k1[i]))%26]
    print(decrypt)
def convert_k(key,n):
    key = list(key)
    if n == len(key):
        return(key)
    else:
        for i in range(n -len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
if __name__ == "__main__": 
  i=input("enter encryption(e) or decryption(d):")
  string = input("Enter the message: ")
  if i=='e':
    encryption(string) 
  else:
    decryption(string)
