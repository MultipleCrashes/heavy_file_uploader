import random, scrypt 

class AuthClass:

    def rand_str(length):
        return ''.join(chr(random.randint(0,255)) for i in range(length))

    def hash_password(password, maxtime=0.5, datalength=64):
        return scrypt.encrypt(randstr(datalength), password, maxtime=maxtime)

    def verify_password(saved_password_hash, entered_password_hash, maxtime=0.5)
        try:
            scrypt.decrypt(saved_password_hash, entered_password_hash, maxtime)
            retun True 
        except scrypt.error:
            return False 


if __name__=='__main__':
    user_pass = 'harishpass'
    user_salt = randstr(2)
    pw_salt = user
