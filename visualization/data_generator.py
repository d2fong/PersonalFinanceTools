import json

# p = PRINCIPAL
# a = ACCUMULATED VALUE
# t = INVESTMENT TERM (in years)
# m = PERIODS PER YEAR
# jm = (INTEREST RATE, COMPOUNDING_SCHEME)
# i = jm / m


# simple script that generates data for the visualization prototype
def accumulation_timeline_generation(p, t, m, jm):
	num_compounding_periods = m * t
	i = jm[0] / jm[1]

	data = {}
	data['principle'] = p
	data['num_compounding_periods'] = m * t
	data['num_investment_years'] = t
	data['accumulated_value'] = p * pow((1 + i), num_compounding_periods)
	data['timeline'] = []


	curr_data_point = {}
	for index in range(0, num_compounding_periods):
		curr_data_point['acc_value'] = p * pow((1+i), index)
		curr_data_point['interest_earned'] = curr_data_point['acc_value'] - p
		data['timeline'].append(curr_data_point)

	json_data = json.dumps(data)
	print json_data

accumulation_timeline_generation(100000, 1, 12, (0.07, 12))