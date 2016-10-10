stripe_secret_key = 'sk_test_YWpFhaSbJp7nolsdKx5iHY9r'
import request

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


if __name__=='__main__':
	obj = StripeClass()
	obj._charge_card()
