'''Some code to make use of the colors from XKCD color with their name when plotting

xkcd_rgb: dictionary with color_name:color_code
reverse_xkcd_rgb: dictionary with color_code:color_name
xkce_color_list: lis of all color names.

Functions:
	get_xkcd_color_name
	get_xkcd_color_code
	xkce_color_name_list
	xkcd_color_code_list

Author Hector Salas O.
'''

from utils.read_rgb import *
from utils.get_name import *
from utils.get_code import *
from utils.get_code_list import *
from utils.get_name_list import *

xkcd_rgb_table = read_data()
xkcd_rgb =  make_dict(xkcd_rgb_table)
reverse_xkcd_rgb = dict(zip(xkcd_rgb.values(), xkcd_rgb.keys()))

xkce_color_list = list(xkcd_rgb_table['color-name'])
