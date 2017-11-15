'''Gives the XKCD color survey hex-code for a given sets of color-names
'''
from .read_rgb import read_data, make_dict

xkcd_rgb_table = read_data()
xkcd_rgb = make_dict(xkcd_rgb_table)


def get_xkcd_color_code(name):
	'''returns the hex-code for the color name.
	Inputs:
		name:	str or list of strins.
				Name of the colors.
	Return:
		code:	str or list of strings.
				hex-code of the colors.
	'''
	if type(name) == str:
		if name not in xkcd_rgb.keys():
			raise KeyError('Color-name not in xkcd color survey')
		code = xkcd_rgb[name]
	elif type(name) == list:
		code = []
		color_not_found = []
		for key in name:
			try:
				code.append(xkcd_rgb[key])
			except KeyError as e:
				color_not_found.append(key)
		if color_not_found != []:
			print('Following colors-names are not in the xkcd color survey')
			print(color_not_found)
	else:
		raise TypeError('Invalid input.')
	return(code)
