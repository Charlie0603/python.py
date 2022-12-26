import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

from requests.api import patch
url1 = 'https://invoice.etax.nat.gov.tw/'
html1 = requests.get(url1)
sp = BeautifulSoup(html1.text, 'lxml')
all1 = sp.find("table", class_="etw-table-bgbox etw-tbig")

tb = sp.find('span', class_='font-weight-bold etw-color-red')
st.write("特別獎:", tb.text)
t = sp.find_all('span', class_='font-weight-bold etw-color-red')[1]
st.write("特獎:", t.text)
