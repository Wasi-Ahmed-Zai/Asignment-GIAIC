import streamlit as st
import requests as req

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = req.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        currencies = country_data.get("currencies", {})
        currency_code = list(currencies.keys())[0] if currencies else "N/A"
        currency_info = currencies.get(currency_code, {})
        currency_name = currency_info.get("name", "N/A")
        currency_symbol = currency_info.get("symbol", "N/A")

        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        region = country_data.get("region", "N/A")

        return name, capital, population, area, currency_name, currency_symbol, region
    else:
        return None

def main():
    st.title("🌍 Country Information App")

    country_name = st.text_input("Enter a Country Name:")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency_name, currency_symbol, region = country_info

            st.subheader("📌 Country Information")
            st.write(f"**Name:** { name}")
            st.write(f"**Capital:** { capital}")
            st.write(f"**Population** { population}")
            st.write(f"**Area** { area} km²")
            st.write(f"**Currency** { currency_name}")
            st.write(f"**Currency Symbol:** { currency_symbol}")
            st.write(f"**Region:** { region}")
        else:
            st.error("❌ Country data not found. Please check the name.")

if __name__ == "__main__":
    main()
