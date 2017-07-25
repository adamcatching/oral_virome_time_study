# Metadata_graphs.py
# Benjamin Adam Catching
# Oral Virome Study
# June 6th, 2017

# Take metadata and show graphs that are visually informative

# Import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
sns.set_context("paper")
sns.set_color_codes("colorblind")

# Read in the data necessary
df = pd.read_csv('metadata.csv')
# Display contents
fig = plt.figure(1)
gridspec.GridSpec(54, 35)

# Set up new 2x9 grid of plots
#fig, axarr = plt.subplots(9, 2, figsize=(15,90), sharex=False, sharey=True)
#sub1 = df['Subject'] == 1
#plt.subplot2grid((31,27), (0,0), colspan=30, rowspan=3)
#sns.barplot(df[sub1].Day, df[sub1].Calorie, color='darkorange')
D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Go through each subject
for i in range(9):

    # This block changes the value i to the subject number, as the list of
    # subjects is not linear (e.g. 1, 2, 4, 6...)
    if i < 2:
        j = i + 1
    elif i == 2:
        j = i + 2
    elif 5 > i > 2:
        j = i + 4
    elif i >= 5:
        j = i + 4
    print(j)

    # Using the pandas package define the subject whose data will be handled
    sub = df['Subject'] == j
    # Define the days of subject's data
    days = df[sub].Day
    # Define the data structure of total calories consumed
    cal = df[sub].Calorie
    # Define the data structure of the total amount of carbohydrates consumed
    # The multiplier 4 is the number of calories per gram of carbohydrate
    carb = df[sub].Carbohydrate * 4
    # Define the data structure of the total amount of fat consumed
    # The multiplier 9 is the number of calories per gram of fat
    fat = df[sub].Lipid * 9
    # Define the data structure of the total amount of protein consumed
    # The multiplier 4 is the number of calories per gram of protein
    protein = df[sub].Protein * 4

    # These values are such that the cumulative bars can 'stack'
    # Carbohydrates go in front, the red bar, so they must be added in all bars
    # carb_fat is the addition of carbohydrates and fat, the blue bar
    carb_fat = carb + fat
    # tot_cal is the addition of all macronutrients, must be displayed last to
    # be in the background
    tot_cal = protein + carb + fat
    # This is the errorbar, if called, on the calorie estimate
    tot_cal_err = tot_cal * .4
    # This is the difference between calories every day, comparing the current
    # day with the previous day
    diff = df[sub].Cal_Diff
    # This is the subplot breakdown
    # A 3x30 space is given to the calorie barplot
    ax0 = plt.subplot2grid((54, 35), (6*i,0), colspan=32, rowspan=3)
    # A 3x2 space is given to the violin distribution plot
    ax1 = plt.subplot2grid((54,35), (6*i,32), colspan=2, rowspan=3)
    # A 2x30 space is given to the calorie difference barplot
    ax2 = plt.subplot2grid((54,35), (6*i+3,0), colspan=32, rowspan=2)

    # Plot the background total number of calories barplot
    sns.barplot(x=days, y=tot_cal, color='darkorange', ax=ax0, 
            label='Protein')
    # Plot the middle barplot of calories from fat and carbohydrates
    sns.barplot(x=days, y=carb_fat, color='royalblue', ax=ax0,
                label='Fat')
    # Plot the front barplot of calories from carbohydrates
    sns.barplot(x=days, y=carb, color='crimson', ax=ax0,
                label='Carbohydrate')
    # Plot the violinplot of calorie distribution 
    sns.violinplot(y=tot_cal, ax=ax1, color='darkseagreen', width=.8)
    # Plot the calorie difference below the total calorie barplot
    sns.barplot(x=days, y=diff, color='silver', ax=ax2)
    # Set the limits for the calorie difference plot
    ax2.set_ylim(-2000, 2000)

    # This is to affect labeling of the plots, most ticks are silenced
    # The subject number is given for each horizontal set of plots
    ax0.set_ylabel('Subject ' + str(j))
    ax0.set_xlabel('')
    ax0.set_xticks([])
    ax1.set_ylabel('')
    ax1.set_xlabel('')
    ax1.set_yticks([])
    ax2.set_yticks([-1500,0, 1500])
    ax2.set_ylabel('')
    #ax2.set_xticks([])
    #ax2.set_xlabel('')

    # If the plot being used is the first one, give a header to the plot
    if i == 0:
        ax0.legend(ncol=3, loc='upper left', frameon=True)
        ax0.set_title('Subject Calorie Breakdown over 30 Days')
    # If the plot is the last one, give the violin plot a description
    if i == 8:
        ax1.set_xlabel(' Daily \nCalorie\n   Distribution')
        #ax2.set_xticks(D)
        #ax2.set_xlabel('Days')

# Plot a the bottom of the graph the type of graph, visualization of calorie
# distribution per subject per day
#fig.text(0.9, 0.04, 'Daily Calories \n Distribution ', ha='right')
fig.text(0.04, 0.5, 'Calorie Contribution', ha='center', rotation='vertical')
plt.show()
