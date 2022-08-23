import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import math


def stacked_plot(columns_to_plot, super_title, df):
    
    '''
    makes some neat little bar graphs showing which make the best features to use based on simple trends
    '''
    
    number_of_columns = 2
    number_of_rows = math.ceil(len(columns_to_plot)/2)

    # create a figure
    fig = plt.figure(figsize=(12, 5 * number_of_rows)) 
    fig.suptitle(super_title, fontsize=20,  y=.95)
 

    # loop to each column name to create a subplot
    for index, column in enumerate(columns_to_plot, 1):

        # create the subplot
        ax = fig.add_subplot(number_of_rows, number_of_columns, index)

        # calculate the percentage of observations of the response variable for each group of the independent variable
        # 100% stacked bar plot
        prop_by_independent = pd.crosstab(df[column], df['churn']).apply(lambda x: x/x.sum()*100, axis=1)

        prop_by_independent.plot(kind='bar', ax=ax, stacked=True,
                                 rot=0, color=['red','blue'])

        # set the legend in the upper right corner
        ax.legend(loc="upper right", bbox_to_anchor=(0.62, 0.5, 0.5, 0.5),
                  title='Churn', fancybox=True)

        # set title and labels
        ax.set_title('Observations by ' + column,
                     fontsize=16, loc='left')

        ax.tick_params(rotation='auto')

        # eliminate the frame from the plot
        spine_names = ('top', 'right', 'bottom', 'left')
        for spine_name in spine_names:
            ax.spines[spine_name].set_visible(False)



def lets_make_some_graphs(df):
    #checking number or percentage of churn yes to no on df with numbers
    sns.countplot(y="churn", data=df, palette="tab10")


  

    # plot distributions of numerical values

    yes_account_columns = ['internet_service_type_id',
 'payment_type_id',
 'contract_type_id',
 'tenure',
 'monthly_charges',
 'number_services',
 'monthly_avg']

# stacked plot of customer account columns
    stacked_plot(yes_account_columns, 'Churn by Select Feature',df)
    

def average_plot(df):
    '''
    Function to display a factor plot with the rate of churn for customers who have a 
    montly bill above or below average 
    '''
    # create subsets of df for those with montly bill above or below average
    bill_above = df[df.monthly_avg ==1 ]
    bill_bellow = df[df.monthly_avg == 0] 
    # get baseline churn rate for the horizontal line
    baseline = round(df.churn.mean() ,4)

    # display factorplot
    p = sns.factorplot( x="monthly_avg", y="churn",  data=df, size=7, 
                   aspect=2, kind="bar", palette="tab10", ci=None,
                   edgecolor=".2")
    plt.axhline(baseline, label = 'overall churn rate', ls='-')
    p.set_xticklabels(['No','Yes'])
    p.set_ylabels("Churn Rate")
    p.set_xlabels("Avg Monthly Bill")
    plt.title('Do those with bill high than average Churn more?')
    plt.show()
    # compare rates of churn in each sample
    print('Churn rate of those whose montly bill is above montly avg', round(bill_above.churn.mean(),4))#  big
    print('Churn rate of those whose montly bill is below montly avg', round(bill_bellow.churn.mean(),4))#  big