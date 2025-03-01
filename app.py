import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_rates = {
        'meters': {'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084},
        'kilometers': {'meters': 1000, 'miles': 0.621371, 'feet': 3280.84},
        'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'feet': 5280},
        'feet': {'meters': 0.3048, 'kilometers': 0.0003048, 'miles': 0.000189394}
    }

    if from_unit == to_unit:
        return value
    try:
        return value * conversion_rates[from_unit][to_unit]
    except KeyError:
        st.error(f"Conversion from {from_unit} to {to_unit} not supported")
        return None

st.title('Unit Converter')

units = ['meters', 'kilometers', 'miles', 'feet']

value = st.number_input('Enter value:', min_value=0.0, format='%f')
from_unit = st.selectbox('From:', units)
to_unit = st.selectbox('To:', units)

if st.button('Convert'):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f'{value} {from_unit} is equal to {result} {to_unit}')
