
alpha={'A':0,"B":1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
class Caesar:
    def __init__(self,s,k):
        self.s=s
        self.k=k
        self.alpha=['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def encrypt(self):
        us=self.s.upper()
        en=""
        for i in us:
            if i ==' ':
                en=en+'s'
                continue
            else:
                s=self.alpha.index(i)
                en=en+self.alpha[(s+self.k)%26]
        return en
        
    def decrypt(self,msg):
        de=""
        for i in msg:
            if i =='s':
                de=de+' '
            else:

                s=self.alpha.index(i)
                de=de+self.alpha[(s-self.k)%26]
        return de
     

c=Caesar("hi everyone",2)
encrypted_msg=c.encrypt()
decrypted_msg=c.decrypt(encrypted_msg)
print("message=",c.s,",key = ",c.k)
print("Encrypted message = ",encrypted_msg)
print("Decrypted message = ",decrypted_msg)


