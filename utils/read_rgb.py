'''Read the file rgb.txt with the data from the XKCD color survey and passes it to a python dictionary

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

from astropy.table import Table, QTable
from astropy.io import ascii

# ------- Functions -------


def read_data(data_file='../rgb.txt'):

    ''' Reads the file containing the rotations curve of a galaxy and pass
    the data to a table.
    input:
        data_file:  str
                    Name of the file with the color data.
    output:
        table: (Table) Table wiht de data.
    '''

    table = ascii.read('rgb.txt', delimiter=':')
    table = Table(table)
    return(table)

def make_dict(table, dict_keys='color-name', dict_values='hex-code'):

    '''Creates a dictionary from two columns of a table
    Inputs:
        table:  Table with the data
        dict_keys:  column with the keys
        dict_values :column with the values
    output:
        table_dict: dictionary
    '''
    table_dict = dict(zip(table[dict_keys], table[dict_values]))
    return(table_dict)
