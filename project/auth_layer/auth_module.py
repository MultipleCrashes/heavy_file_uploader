import random, scrypt 

class AuthClass:

    def rand_str(length):
        return ''.join(chr(random.randint(0,255)) for i in range(length))

    def hash_password(password, maxtime=0.5, datalength=64):
        return scrypt.encrypt(randstr(datalength), password, maxtime=maxtime)

    def verify_password(saved_password_hash, entered_password_hash, maxtime=0.5):
        try:
            scrypt.decrypt(saved_password_hash, entered_password_hash, maxtime)
            retun True 
        except scrypt.error:
            return False 


if __name__== '__main__':
    user_pass = 'harishpass'
    user_salt = randstr(5)  # also store salt as plain text
    pw_salt = user_pass + user_salt 
    hashed_pw = hash_password(pw_salt)
    # get plain salt from db and password entered by the user ,
    # hash the combination and match with what is stored in the db 
    verify_password(hash_password,pw_salt)   # returns True
