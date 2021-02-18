import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


######### FOR DEMO ONE ##############
def magic_math_op_method(base, power):
    value = base ** power
    # Uncover for demo:
    value = np.log10(value)
    return value


























######### FOR DEMO TWO AND THREE ##############
def covid_data_demo():
    nyt_url_counties = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    plot_cases(nyt_url_counties)

def load_nyt_data(url):
    df = pd.read_csv(url, index_col=0, na_filter=True)
    print(df.head(5))
    return df

def plot_cases(url):
    df = load_nyt_data(url)
    nyc = df[df['county'].str.contains('New York City', na=False)]
    losangeles = df[df['county'].str.contains('Los Angeles', na=False)]
    chittenden = df[df['county'].str.contains('Chittenden', na=False)]

    # Rates of change, raw diffs between cases
    plt.plot(nyc['cases'].diff()[1:].index, nyc['cases'].diff()[1:], label='NYC New Cases Daily')
    plt.plot(losangeles['cases'].diff()[1:].index, losangeles['cases'].diff()[1:], label='Los Angeles New Cases Daily')
    plt.plot(chittenden['cases'].diff()[1:].index, chittenden['cases'].diff()[1:], label='Chittenden New Cases Daily',
             alpha=0.75, color='green')
    plt.xticks(['2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01',
                '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'])
    plt.xticks(rotation=20)

    plt.legend(loc='upper left')
    plt.show()


    ###### DEBUG DEMO PARt TWO ##############
    ny_with_pop = cases_with_population_data(nyc)
    la_with_pop = cases_with_population_data(losangeles)

    plt.plot(ny_with_pop['cases'].diff()[1:].index, ny_with_pop['cases'].diff()[1:] / (ny_with_pop['POP_ESTIMATE_2019'])[1:], label='NY New Cases By Pop')
    plt.plot(la_with_pop['cases'].diff()[1:].index, la_with_pop['cases'].diff()[1:]/(la_with_pop['POP_ESTIMATE_2019'])[1:], label='LA New Cases By Pop')


    plt.xticks(['2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01',
                '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'])
    plt.xticks(rotation=20)

    plt.legend(loc='upper left')
    plt.show()

    ######## DEBUG DEMO part 3##############
    nyc_pop = determine_nyc_pop()

    plt.plot(ny_with_pop['cases'].diff()[1:].index, ny_with_pop['cases'].diff()[1:]/nyc_pop, label='NY New Cases By Pop')
    plt.plot(la_with_pop['cases'].diff()[1:].index, la_with_pop['cases'].diff()[1:]/(la_with_pop['POP_ESTIMATE_2019'])[1:], label='LA New Cases By Pop')

    plt.xticks(['2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01',
                '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'])
    plt.xticks(rotation=20)

    plt.legend(loc='upper left')
    plt.show()


def cases_with_population_data(covid_data_df):
    pop_data = pd.read_csv('../../PopulationEst.csv', delimiter=',', thousands=',')
                                                                                                                                                            #, encoding="ISO-8859-1") #Remove encoding for demo
    combodf = covid_data_df.join(pop_data.set_index('FIPStxt'), on='fips')
    print(combodf.head(5))
    return combodf



def determine_nyc_pop():
    pop_data = pd.read_csv('../../PopulationEstimates.csv', delimiter=',', thousands=',', encoding="ISO-8859-1")
    nyc_fips = [36005, 36047, 36061, 36081, 36085]
    total_pop = 0
    for code in nyc_fips:
        subpop = pop_data[pop_data['FIPStxt'] == code]
        total_pop += int(subpop['POP_ESTIMATE_2019'])

    return total_pop


    # The
    # Bronx is Bronx
    # County(ANSI / FIPS
    # 36005)
    # Brooklyn is Kings
    # County(ANSI / FIPS
    # 36047)
    # Manhattan is New
    # York
    # County(ANSI / FIPS
    # 36061)
    # Queens is Queens
    # County(ANSI / FIPS
    # 36081)
    # Staten
    # Island is Richmond
    # County(ANSI / FIPS
    # 36085)