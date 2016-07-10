from user.models import *

class AuthenticateUser:
    def authenticate_user(self, user_id, password):
        try:
            User.objects.get(user_id=user_id)
        except Exception,e:
            print "Exception found during authentication",e
            pass 



