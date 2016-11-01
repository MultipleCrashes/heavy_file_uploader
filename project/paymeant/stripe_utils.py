import stripe 
stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

class StripeClass:
	
    def __init__(self):
        self.transaction_token = ''
        pass

    ''' Steps 
        1. Generate Token
        2. Charge Card 
    '''
    
    def generate_token(self,):
        self.transaction_token = stripe.Token.create(
                card={"number":"4242424242424242",
                      "exp_month":12,
                      "exp_year":2016,
                      "cvc":"123"},
                )
	print "token generated ->",self.transaction_token

    def charge_card(self):
        token = self.transaction_token
	try:
	    charge = stripe.Charge.create(
		        amount =10000,
			currency='INR',
			source=token,
			description='Test Charge'
		    )
	    print "charge response - > ",charge 
	except stripe.error.CardError as e:
	    print str(e) 


if __name__=='__main__':
	obj = StripeClass()
	obj.generate_token()
	obj.charge_card()
