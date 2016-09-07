import numpy as np
from datetime import datetime, date
from decimal import *
# pricing_utils

# def calculate_payout(optionContract, underlyingPrice):
# 	if optionContract.option_type == OptionContract.CALL:
# 		return calculate_call_payout(optionContract, underlyingPrice)
# 	elif optionContract.option_type == OptionContract.PUT:
# 		return calculate_put_payout(optionContract, underlyingPrice)

# def calculate_call_payout(optionContract, underlyingPrice):
# 	return 0

# def calculate_put_payout(optionContract, underlyingPrice):
# 	return 0

expiry_date_string = '9/16/16'
expiry_date = datetime.strptime(expiry_date_string, '%m/%d/%y')
today = date.today()

days_left = expiry_date.date() - today

S0 = 2184.5 #initial level
K = 2185.0 #strike
T = (float(days_left.days)/252) #time to maturity
r = .0040 #riskless rate
sigma = .0496 #vol
# sigma = .0796 #vol

I = 10000 #number of simulations

z = np.random.standard_normal(I) #pseudorandom numbers
# z = np.random.lognormal(I) #pseudorandom numbers
ST = S0 * np.exp((r - .5 * sigma ** 2) * T + sigma * np.sqrt(T) * z) #index vals at maturity
hT = np.maximum(ST - K, 0) #inner values at maturity
C0 = np.exp(-r * T) * np.sum(hT) / I #monte carlo estimator

print "value of european call options %5.8f" % C0
	