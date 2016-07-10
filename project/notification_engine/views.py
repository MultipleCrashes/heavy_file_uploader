from django.shortcuts import render
<<<<<<< HEAD
from otpauth import OtpAuth

# Create your views here.
# A method for generating and validating the OTP
# in this we are going to use time based OTP
class otp:
	def __init__(self):
		auth=OtpAuth('secret')

	def Generate_OTP(request):
		#secret is any string that we can use for generating otp
		random_otp_string=auth.totp()
		print verify_OTP(random_otp_string)

	def verify_OTP(random_otp_string):
		return auth.valid_totp(random_otp_string)

=======

# Create your views here.
>>>>>>> 6e2bc3eb4ba58b44c07d0ea44eef71fbb650a940
