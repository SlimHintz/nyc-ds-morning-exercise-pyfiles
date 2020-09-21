import pandas as pd
import matplotlib.pyplot as plt

def nytimes():
    return pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

def county_data(county, state):
    df = nytimes()
    return df[(df['county'] == county) & (df['state'] == state)]

def plot_county_cases(county, state):
    df = county_data(county, state)
    fig = df.plot(x='date' ,y='cases', kind='line', rot=45)
    fig.set_title(f'COVID19 cases: {county} County, {state}');
    

 