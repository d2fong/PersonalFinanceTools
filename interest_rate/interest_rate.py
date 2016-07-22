from decimal import Decimal, getcontext

# Currently, this class only supports compounding rates, TODO: implement some sort
# of class for simple interest
class InterestRate(object):

	DEFAULT_PRECISION = 8

	def __init__(self, percent_rate, compounding_period):
		
		# Set a default precision for now, potentially allow one to specify precision 
		# sometime in the future
		getcontext().prec = InterestRate.DEFAULT_PRECISION

		self.percent_rate = Decimal(percent_rate)
		self.compounding_period = compounding_period
		self.periodic_interest_rate = self.percent_rate / self.compounding_period

	def periodic_interest_rate(self):
		return self.periodic_interest_rate


# Given an interest rate and a different compounding_period
# convert an equivalent rate for the given
def convert_interest_rate(new_comp_period, interest_rate):
	getcontext().prec = InterestRate.DEFAULT_PRECISION

	old_rate = 1 + interest_rate.periodic_interest_rate
	e = Decimal(interest_rate.compounding_period / new_comp_period)

	return getcontext().power(old_rate, e) - 1
