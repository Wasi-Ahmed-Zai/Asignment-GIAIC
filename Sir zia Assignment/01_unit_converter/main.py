import streamlit as st

# Function to convert units
def convert_units(value, from_units, to_units):
    conversions = {
                                     # Length
        "kilometers_meters": 1000,              "meters_kilometers": 0.001,   
        "kilometers_millimeters": 1000000,      "millimeters_kilometers": 0.000001, 
        "kilometers_centimeters": 100000,       "centimeters_kilometers": 0.00001,    
        "kilometers_miles": 0.621371,           "miles_kilometers": 1.60934,
        "kilometers_feet": 3280.84,             "feet_kilometers": 0.0003048,
        "kilometers_inches": 39370.1,           "inches_kilometers": 0.0000254,
        "kilometers_yards": 1093.61,            "yards_kilometers": 0.0009144,
        "meters_millimeters": 1000,             "millimeters_meters": 0.001,
        "meters_centimeters": 100,              "centimeters_meters": 0.01,       
        "meters_feet": 3.28084,                 "feet_meters": 0.3048,
        "meters_yards": 1.09361,                "yards_meters": 0.9144, 
        "meters_miles": 0.000621371,            "miles_meters": 1609.34,
        "meters_inches": 39.3701,               "inches_meters": 0.0254,
        "millimeters_centimeters": 0.1,         "centimeters_millimeters": 10,
        "millimeters_miles": 6.2137e-7,         "miles_millimeters": 1609340,
        "millimeters_feet": 0.00328084,         "feet_millimeters": 304.8,
        "millimeters_inches": 0.0393701,        "inches_millimeters": 25.4,
        "millimeters_yards": 0.00109361,        "yards_millimeters": 914.4,
        "centimeters_miles": 6.2137e-6,         "miles_centimeters": 160934,
        "centimeters_feet": 0.0328084,          "feet_centimeters": 30.48,
        "centimeters_inches": 0.393701,         "inches_centimeters": 2.54,
        "centimeters_yards": 0.0109361,         "yards_centimeters": 91.44,
        "inches_miles": 1.5783e-5,              "miles_inches": 63360,
        "inches_feet": 0.0833333,               "feet_inches": 12,
        "inches_yards": 0.0277778,              "yards_inches": 36,
        "feet_yards": 0.333333,                 "yards_feet": 3,
        "feet_miles": 0.000189394,              "miles_feet": 5280,
        "yards_miles": 0.000568182,             "miles_yards": 1760,

                                     # Weight
        "tons_kilograms": 1000,                  "kilograms_tons": 0.001,
        "tons_grams": 1_000_000,                 "grams_tons": 1 / 1_000_000,
        "tons_milligrams": 1_000_000_000,        "milligrams_tons": 1 / 1_000_000_000,
        "tons_pounds": 2204.62,                  "pounds_tons": 1 / 2204.62,
        "tons_ounces": 35274,                    "ounces_tons": 1 / 35274,
        "kilograms_grams": 1000,                "grams_kilograms": 0.001, 
        "kilograms_milligrams": 1_000_000,        "milligrams_kilograms": 0.000001,
        "kilograms_pounds": 2.20462,            "pounds_kilograms": 0.453592,  
        "kilograms_ounces": 35.274,              "ounces_kilograms": 0.0283495,
        "grams_pounds": 0.00220462,              "pounds_grams": 453.592,
        "grams_ounces": 0.035274,                "ounces_grams": 28.3495,
        "grams_milligrams": 1000,                "milligrams_grams": 0.001,
        "pounds_milligrams": 453592.37,         "milligrams_pounds": 2.20462e-6,           
        "pounds_ounces": 16,                    "ounces_pounds": 0.0625,
        "milligrams_ounces": 3.5274e-5,         "ounces_milligrams": 28349.5,


                                     # Time
        "seconds_minutes": 1/60,                "minutes_seconds": 60,
        "seconds_hours": 1/3600,                "hours_seconds": 3600,
        "seconds_days": 1/86400,                "days_seconds": 86400,
        "seconds_weeks": 1/604800,              "weeks_seconds": 604800,
        "seconds_months": 1/2629746,            "months_seconds": 2629746,  
        "seconds_years": 1/31536000,            "years_seconds": 31536000,  
        "minutes_hours": 1/60,                  "hours_minutes": 60,
        "minutes_days": 1/1440,                 "days_minutes": 1440,
        "minutes_weeks": 1/10080,               "weeks_minutes": 10080,
        "minutes_months": 1/43829.1,            "months_minutes": 43829.1,   
        "minutes_years": 1/525600,              "years_minutes": 525600, 
        "hours_days": 1/24,                     "days_hours": 24,
        "hours_weeks": 1/168,                   "weeks_hours": 168,
        "hours_months": 1/730.484,              "months_hours": 730.484, 
        "hours_years": 1/8760,                   "years_hours": 8760,   
        "days_weeks": 1/7,                      "weeks_days": 7,
        "days_months": 1/30.44,                 "months_days": 30.44,
        "days_years": 1/365,                    "years_days": 365,
        "months_weeks": 4.348,                  "weeks_months": 1/4.348,
        "months_years": 1/12,                   "years_months": 12,
        "weeks_years": 1/52.1429,               "years_weeks": 52.1429,

                                     # Volume
        "liters_milliliters": 1000,                  "milliliters_liters": 0.001,
        "liters_gallons": 0.264172,                  "gallons_liters": 3.78541, 
        "liters_cups": 4.22675,                      "cups_liters": 0.236588,                  
        "liters_cubic_meters": 0.001,                "cubic_meters_liters": 1000,  
        "liters_fluid_ounces": 33.814,               "fluid_ounces_liters": 0.0295735,
        "milliliters_cups": 0.00422675,              "cups_milliliters": 236.588,
        "milliliters_cubic_meters": 1e-6,            "cubic_meters_milliliters": 1e6,
        "milliliters_gallons": 0.000264172,          "gallons_milliliters": 3785.41, 
        "milliliters_fluid_ounces": 0.033814,        "fluid_ounces_milliliters": 29.5735,  
        "cups_gallons": 0.0625,                       "gallons_cups": 16,
        "cups_cubic_meters": 0.000236588,             "cubic_meters_cups": 4226.75,
        "cups_fluid_ounces": 8,                       "fluid_ounces_cups": 0.125,
        "cubic_meters_gallons": 264.172,              "gallons_cubic_meters": 0.00378541,
        "cubic_meters_fluid_ounces": 33814,           "fluid_ounces_cubic_meters": 2.95735e-5,
        "fluid_ounces_gallons": 0.0078125,            "gallons_fluid_ounces": 128,

    }

    formula_conversions = {
        # Temperature
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
        "celsius_kelvin": lambda c: c + 273.15,
        "kelvin_celsius": lambda k: k - 273.15,
        "fahrenheit_kelvin": lambda f: ((f - 32) * 5/9) + 273.15,
        "kelvin_fahrenheit": lambda k: ((k - 273.15) * 9/5) + 32
    }

    from_units = from_units.lower().replace(" ", "_")
    to_units = to_units.lower().replace(" ", "_")
    key = f"{from_units}_{to_units}"

    if from_units == to_units:
        return value
    elif key in conversions:
        return value * conversions[key]
    elif key in formula_conversions:
        return formula_conversions[key](value)
    else:
        return None

st.set_page_config(page_title="Universal Unit Converter", layout="centered" )
st.title("🌐 Universal Unit Converter")


value = st.number_input("Enter the value to convert:", step=0.1)

length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"]
weight_units = ["Grams", "Kilograms", "Pounds", "Ounces", "Milligrams", "Tons"]
time_units = ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"]
volume_units = ["Liters", "Milliliters", "Gallons", "Cups", "Fluid Ounces", "Cubic Meters"]
temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

category = st.selectbox("Select category:", ["📏 Length", "⚖️ Mass", "⏰ Time", "🥛 Volume", "🌡️ Temperature"])

if category == "📏 Length":
    units = length_units
elif category == "⚖️ Mass":
    units = weight_units
elif category == "⏰ Time":
    units = time_units
elif category == "🥛 Volume":
    units = volume_units
elif category == "🌡️ Temperature":
    units = temperature_units
else:
    units = []

from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None and isinstance(result, (int, float)):
        rounded_result = round(result, 6) 
        rounded_value = round(value, 6)    
        st.success(f"Result: {rounded_value} {from_unit} = {rounded_result} {to_unit}")
    else:
        st.error("Conversion not supported for selected units.")



# Footer
st.markdown("---", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; font-size: 16px; color: #00BFFF;'>
        Made with ❤️ by <a href='https://github.com/wasi811' style='color: #00BFFF; text-decoration: none; font-weight: bold;'>Wasi Ahmed</a>
    </div>
    """,
    unsafe_allow_html=True
)
