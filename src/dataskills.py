import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


######### FOR DEMO ONE ##############
def magic_math_op_method(base, power):
    value = base ** power
    # Uncover for demo:
    #value = np.log10(value)
    return value








######### FOR DEMO TWO AND THREE ##############
def collaborative_method():
    nyt_url_counties = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    plot_cases_spring(nyt_url_counties)

def load_nyt_data(url):
    df = pd.read_csv(url, index_col=0, na_filter=True)
    print(df.head(5))
    return df

def plot_cases_spring(url):
    # also good for demo
    df = load_nyt_data(url)
    nyc = df[df['county'].str.contains('New York City', na=False)]

    # Rates of change, raw diffs between cases
    plt.plot(nyc['cases'].diff()[1:].index, nyc['cases'].diff()[1:], label='NYC New Cases Daily')
    plt.xticks(['2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01',
                '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'])

    plt.legend(loc='upper left')
    plt.show()
    #plot_cases_with_population_data(nyc)

def plot_cases_with_population_data(covid_data_df):
    pop_data = pd.read_csv('../../PopulationEstimates.csv', delimiter=',', encoding="ISO-8859-1") #Remove encoding for demo
    combodf = covid_data_df.join(pop_data.set_index('FIPStxt'), on='fips')
    print(combodf.head(5))