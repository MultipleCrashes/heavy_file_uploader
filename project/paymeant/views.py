from django.shortcuts import render

# Create your views here.
class StripeClass:
	
	def __init__(self):
		pass

	def charge_card(self):

		token = request.POST['stripeToken']
		try:
			charge = stripe.Charge.create(
				amount =1,
				currency='INR',
				source=token,
				description='Test Charge'
				)
		except stripe.error.CardError as e:
			pass 
