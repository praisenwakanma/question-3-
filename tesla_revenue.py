!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
#!pip install plotly==5.3.1

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(url).text
beautiful_soup = BeautifulSoup(html_data, 'html.parser')

tesla_revenue_read = pd.read_html(url)
tesla_revenue = tesla_revenue_read[1]
tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for row in beautiful_soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date= col[0].text
    revenue= col[1].text
    tesla_revenue = tesla_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)
tesla_revenue
