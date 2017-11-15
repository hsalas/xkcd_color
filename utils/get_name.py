'''Gives the XKCD color survey name for a given sets of hex-code
'''

from .read_rgb import read_data, make_dict

xkcd_rgb_table = read_data()
xkcd_rgb = make_dict(xkcd_rgb_table)


def get_xkcd_color_name(code):

	'''Returns color-name from the hex-code.
	Inputs:
		code (str or list):	String or list of strings containing the hex-code of the color.
	Return:
		name (str or list):	String or list of strings containing name of the colors.
	'''
	if type(code) == str:
		try:
			name = reverse_xkcd_rgb[color]
		except KeyError as e:
			print('Color-name not in xkcd color survey')
	elif type(code) == list:
		name = []
		color_not_found = []
		for key in code:
			try:
				name.append(reverse_xkcd_rgb[key])
			except KeyError as e:
				color_not_found.append(key)
		if color_not_found != []:
			print('Following colors hex-codes are not in the xkcd color survey')
			print(color_not_found)
	else:
		raise TypeError('Invalid input.')
	return(name)
