import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
BMI=df.weight/((df.height/100)**2)
BMI=BMI>25

# Add 'overweight' column
df['overweight'] = BMI.astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol=df.cholesterol>1
df.cholesterol=df.cholesterol.astype(int)

df.gluc=df.gluc>1
df.gluc=df.gluc.astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat =pd.melt(df,id_vars='cardio',value_vars=['cholesterol','gluc','smoke','active','overweight']) 


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio','variable','value'])['value'].count())
    df_cat.rename(columns={'value':'total'},inplace=True)
    df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(data=df_cat, kind="bar",  x="variable", hue="value", col="cardio",y='total')
    graph.set_ylabels('total', fontsize=10) 
    fig=graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat =df.loc[(df['ap_lo']<=df['ap_hi']) 
              & (df['height'] >= df['height'].quantile(0.025)) 
              & (df['height'] <= df['height'].quantile(0.975))
              & (df['weight'] >= df['weight'].quantile(0.025))
              & (df['weight'] <= df['weight'].quantile(0.975)),:]
    # Calculate the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(15, 10))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, cmap='mako', fmt=".1f")
    plt.show()      
    fig=ax.fig

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
