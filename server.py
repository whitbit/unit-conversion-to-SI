from flask import Flask
from math import pi

app = Flask(__name__)

SI_CONVERSTIONS = {
    'minute': (60, 's'),
    'min': (60, 's'),
    'hour': (3600, 's'),
    'h': (3600, 's'),
    'day': (86400, 's'),
    'd': (86400, 's'),
    'degree': ((pi/180), 'rad'),
    'º': ((pi/180), 'rad'),
    '\'': (pi/180, 'rad'),
    'second': ((pi/648000), 'rad'),
    '\"': ((pi/648000), 'rad'),
    'hectare': (10000, 'm²'),
    'ha': (10000, 'm²'),
    'litre': (0.001, 'm³'),
    'L': (0.001, 'm³'),
    'tonne': (10**3, 'kg'),
    't': (10**3, 'kg')
}


@app.route('/units/si?units=<units>', methods=['GET'])
def convert_to_SI(units):
    
    pass

def parse_units_input(units):

    # for case of no math input
    if ('/' not in units
        and '*' not in units
        and '(' not in units
        and ')' not in units):
        return SI_CONVERSTIONS[units]

def to_json(converted_units):

    name, multiplication_factor = converted_units[0], converted_units[1]
    multiplication_factor = format(multiplication_factor, '.14f')

    return { 'unit_name': name,
             'multiplication_factor': multiplication_factor}



if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)