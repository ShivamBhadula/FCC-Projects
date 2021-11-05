import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=['date'])
# Clean data
df=df.loc[(df.value>df.value.quantile(0.025))
         & (df.value<df.value.quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(12,6))
    fig=plt.plot(df.index,df.value,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df['month']=df.index.month
    df['year']=df.index.year
    df_bar=df.groupby(['month','year']).value.mean()
    # Draw bar plot
    fig = df_bar.unstack(0).plot.bar(figsize=(12,6))
    fig.set_xlabel('Years')
    fig.set_ylabel('Average Page Views')
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    plt.legend(fontsize = 10, labels = months)
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig=plt.figure(figsize=(20,5))
    plt.subplot(1,2,2)

    sns.boxplot(x="month", y="value", data=df)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title("Month-wise Box Plot (Seasonality)")

    plt.subplot(1,2,1)
    sns.boxplot(x="year", y="value", data=df)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title("Year-wise Box Plot (Trend)")

    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
