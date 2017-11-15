'''Generates a list with hex-codes from the XKCD color survey.
Author Hector Salas O.
'''
from .read_rgb import read_data, make_dict

xkcd_rgb_table = read_data()
xkcd_rgb = make_dict(xkcd_rgb_table)


def xkcd_color_code_list(banned=[], only_=[], exclude_=[]):
	'''Generates a list with the hex-codes for colors in the xkcd survey.
	Inputs:
		banned:	list optional.
				List of strings with color-names to be excluded.
		exclude_:	list optional.
					Color-names that include the strings from the list will be
					excluded. View frequent strings in color-names.
		only_:	list optional.
				Only color-names that include strings from the list will be
				added to the list. View frequent strings in color-names.

	Frequent strings in color-names:

	'green' (206), blue (137), 'light' (87), --'ish' (76),  'dark' (72),
	'pink' (67), 'purple' (64),  'brown' (60), 'yellow' (58), 'red' (50),
	'grey' (47), 'orange' (34), 'pale' (31), 'bright' (24), 'deep' (17),
	'sea' (16), 'teal' (16), 'lime' (15), 'olive' (12), 'aqua' (12),
	'violet' (11), 'sky' (11), 'tan' (10), 'dust' (10), 'baby' (10),
	'rose' (10), 'gold' (10), 'dull' (9), 'pastel' (9), 'lavender' (9),
	'turquoise' (9), 'foam' (8), 'poo' (8), 'sand' (8), 'dirt' (8), 'neon' (7),
	'magenta' (7), 'navy' (7), 'medium' (6)  'ugly' (6), 'cyan' (6),
	'rust' (6), 'burnt' (6), 'mustard' (6), 'dusk' (6),'warm' (5), 'shit' (5),
	'hot' (5), 'royal' (5), 'blood' (4), 'off ' (4)

	Returns:
		List with color hex-codes (list)
	'''
	hex_list = []
	for key in xkcd_rgb:
		if key not in banned:
			if exclude_ == [] and only_ == []:
				hex_list.append(xkcd_rgb[key])
			elif exclude_ != [] and only_ == []:
				for name in exclude_:
					if name not in key:
						hex_list.append(xkcd_rgb[key])
			elif exclude_ == [] and only_ != []:
				for name in only_:
					if name in key:
						hex_list.append(xkcd_rgb[key])
			else:
				for only_name in only_:
					aux = True
					for exclude_name in exclude_:
						if exclude_name in key:
							aux = False
					if aux:
						if only_name in key:
							hex_list.append(xkcd_rgb[key])

	return(hex_list)
