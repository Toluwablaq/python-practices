def generator():
    import random
    import string
    
    pass_input=input('enter the password to generate:  ')
    lent=len(pass_input)
    if(lent<=2):
        character=list(string.ascii_letters+string.digits)
        random.shuffle(character)
        passwd=[]
        for _ in range(5):
            passwd.append(random.choice(character))
            generate="".join(passwd)
        pass_app=generate + pass_input
        print("""""")
        print('password generated successful: ' +pass_app)
    #random.shuffle(pass_app)
    else:
        print('sorry only two charater is needed')
 
generator()


