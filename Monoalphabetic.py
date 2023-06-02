import random
class Monoalphabetic:
    def __init__(self,s):
        self.s=s
        self.alpha=['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.key=self.alpha.copy()
        random.shuffle(self.key)
    def encrypt(self):
        us=self.s.upper()
        en=""
        for i in us:
            if i ==' ':
                continue
            s=self.alpha.index(i)
            en=en+self.key[s]
        return en
        
    def decrypt(self,msg):
        de=""
        for i in msg:
            if i ==' ':
                continue
            s=self.key.index(i)
            de=de+self.alpha[s]
        return de

c=Monoalphabetic("hi everyone")
encrypted_msg=c.encrypt()
decrypted_msg=c.decrypt(encrypted_msg)
print("message=",c.s,",key = ",c.key)
print("Encrypted message = ",encrypted_msg)
print("Decrypted message = ",decrypted_msg)