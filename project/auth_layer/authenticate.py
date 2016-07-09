from user.models import *


class AuthenticateUser:
    def authenticate_user(self, user_name, password):
        try:
            User.objects.get(user_name = user_name)
        except User.DoestNotExist:
            pass 
        except Exception,e:
            pass 



