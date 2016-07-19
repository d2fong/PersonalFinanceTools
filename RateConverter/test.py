import unittest


class RateConverterTest(unittest.TestCase):
	
	def test_convert_rate(self):
		r1 = 7.0
		fr1 = 4
		fr2 = 365

		output = 0.000741417

		result = convert_rate(r1, fr1, fr2)
		

		self.assertEqual(result, output)


if __name__ == '__main__':
	unittest.main()