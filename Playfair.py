
def key_matrix(key):
    mat=[[0 for i in range(5)]for j in range(5)]
    alpha=['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    key=key.upper()
    k=''
    for i in key:
        if i==' ':
            continue
        k=k+i
    play=[]
    for i in k:
        if i not in play:
            if i=='J':
                play.append('I')
                continue
            play.append(i)
    is_I="I" in play
    for i in alpha:
        if i not in play:
            if i=='J'and not is_I:
                play.append("I")
                is_I=True
            elif i=="I" or i=="J" and is_I:
                pass
            else:
                play.append(i)
    index=0
    for i in range(5):
        for j in range(5):
            mat[i][j]=play[index]
            index+=1
    return mat

def convert_to_diagraphs(plaintext):
    plaintext=plaintext.upper()
    list1=[]
    for i in range(0,len(plaintext)+1,2):
        if i<len(plaintext)-1:
            if plaintext[i]==plaintext[i+1]:
                plaintext=plaintext[:i+1]+"X"+plaintext[i+1:]
    if len(plaintext)%2 !=0:
        plaintext=plaintext[:]+'X'
    for i in range(0,len(plaintext),2):
        list1.append(plaintext[i]+plaintext[i+1])
    return list1

def search(mat,element):
    for i in range(5):
        for j in range(5):
            if mat[i][j]==element:
                return i,j
def encrypt_columnrule(mat,e1r,e1c,e2r,e2c):
    c1=''
    if e1r==4:
        c1=mat[0][e1c]
    else:
        c1=mat[e1r+1][e1c]
    c2=''
    if e2r==4:
        c2=mat[0][e2c]
    else:
        c2=mat[e2r+1][e2c]
    return c1,c2 
def decrypt_columnrule(mat,e1r,e1c,e2r,e2c):
    c1=''
    if e1r==0:
        c1=mat[4][e1c]
    else:
        c1=mat[e1r-1][e1c]
    c2=''
    if e2r==0:
        c2=mat[0][e2c]
    else:
        c2=mat[e2r-1][e2c]
    return c1,c2 
def encrypt_rowrule(mat,e1r,e1c,e2r,e2c):
    c1=''
    if e1c==4:
        c1=mat[e1r][0]
    else:
        c1=mat[e1r][e1c+1]
    c2=''
    if e2c==4:
        c2=mat[e2r][0]
    else:
        c2=mat[e2r][e2c+1]
    return c1,c2 
def decrypt_row(mat,e1r,e1c,e2r,e2c):
    c1=''
    if e1c==0:
        c1=mat[e1r][4]
    else:
        c1=mat[e1r][e1c-1]
    c2=''
    if e2c==0:
        c2=mat[e2r][4]
    else:
        c2=mat[e2r][e2c-1]
    return c1,c2
def encrypt_square(mat,e1r,e1c,e2r,e2c):
    c1 = ''
    c1 = mat[e1r][e2c]
    c2 = ''
    c2 = mat[e2r][e1c]
    return c1,c2

def encrypt_plaintext(mat,plaintext):
    ciphertext=[]
    for i in range(0,len(plaintext)):
        c1=0
        c2=0
        el1x,el1y=search(mat,plaintext[i][0])
        el2x,el2y=search(mat,plaintext[i][1])
        if el1x==el2x:
            c1,c2=encrypt_rowrule(mat,el1x,el1y,el2x,el2y)
        elif el1y==el2y:
            c1,c2=encrypt_columnrule(mat,el1x,el1y,el2x,el2y)
        else:
            c1,c2=encrypt_square(mat,el1x,el1y,el2x,el2y)
        ciper=c1+c2
        ciphertext.append(ciper)
    return ciphertext
    
def decrypt(mat,data):
    plain=[]
    pt=''
    message=convert_to_diagraphs(data)
    for i in range(0,len(message)):
        c1=0
        c2=0
        el1x,el1y=search(mat,message[i][0])
        el2x,el2y=search(mat,message[i][1])
        if el1x==el2x:
            c1,c2=decrypt_row(mat,el1x,el1y,el2x,el2y)
        elif el1y==el2y:
            c1,c2=decrypt_columnrule(mat,el1x,el1y,el2x,el2y)
        else:
            c1,c2=encrypt_square(mat,el1x,el1y,el2x,el2y)
        pt=c1+c2
        plain.append(pt)
    return plain
text="pallaviisagoodgirl"
plain=convert_to_diagraphs(text)
print("the given plain text :",text)
key=key_matrix("jump up")
ciper=encrypt_plaintext(key,plain)
ciphertext=""
for i in ciper:
    ciphertext=ciphertext+i
print("cipertext:",ciphertext)
print("after decryption:")
pt=decrypt(key,ciphertext)
plaintext=''
for i in pt:
    plaintext=plaintext+i
plaintext_without_fillers=''
for i in plaintext:
    if i=="X":
        continue
    plaintext_without_fillers=plaintext_without_fillers+i
print("plaintext:",plaintext_without_fillers)
