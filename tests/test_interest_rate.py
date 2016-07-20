from interest_rate.interest_rate import convert_interest_rate, InterestRate
from decimal import Decimal, getcontext

import unittest

class InterestRateTest(unittest.TestCase):

	def setUp(self):
		getcontext().prec = 8
	
	def test_interest_rate_construction(self):
		val = 0.07
		compoundingPeriod = 365

		result = InterestRate(val, compoundingPeriod)

		self.assertEqual(result.periodic_interest_rate, Decimal(val) / Decimal(compoundingPeriod))

	def test_interest_rate_conversion(self):
		val = 0.07
		compoundingPeriod = 4
		ir = InterestRate(val, compoundingPeriod)
		newCompoundingPeriod = 2

		result = convert_interest_rate(2, ir)

		self.assertEqual(result, Decimal(0.0353062) / 1)

	def test_handle_negative_interest_rate(self):
		val = -0.124
		compoundingPeriod = 12

		result = InterestRate(val, compoundingPeriod)

		self.assertEqual(result.periodic_interest_rate, Decimal(val) / Decimal(compoundingPeriod))

if __name__ == '__main__':
	unittest.main()