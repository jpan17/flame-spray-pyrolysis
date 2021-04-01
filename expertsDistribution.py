import csv
import pandas
import statistics
import matplotlib.pyplot as plt
import numpy as np 
import random
from matplotlib.lines import Line2D
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib.pyplot import colorbar, figure
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from statistics import mean, stdev
# =========================================================================== #

def plot_stackedbar_p(df, labels, colors, title, subtitle): 
    fields = df.columns.tolist()
    
    # figure and axis
    fig, ax = plt.subplots(1, figsize=(6,8))
    
    # plot bars
    left = len(df) * [0]
    for idx, name in enumerate(fields):
        plt.barh(df.index, df[name], left = left, color = colors[idx])
        left = left + df[name]
        
    # title and subtitle
    ax.set_title(title, loc="left", fontsize = 14, pad=22)
    plt.yticks(fontsize=8)
    plt.xlabel("Composition of Classifications", fontsize = 12)    
    plt.ylabel("Video Labels", fontsize = 12)
    # legend
    plt.legend(labels, bbox_to_anchor = ([0.7, 1, 0, 0]),ncol = 1, frameon = False)
    
    # remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    # format x ticks
    xticks = np.arange(0,1.1,0.1)
    xlabels = ['{}%'.format(i) for i in np.arange(0,101,10)]
    plt.xticks(xticks, xlabels)
    
    # adjust limits and draw grid lines 
    plt.ylim(-1, ax.get_yticks()[-1] + 1)
    ax.xaxis.grid(color='gray', linestyle='dashed')
    # plt.ylabels('Video Number'

def expertsDistribution():
    
    df = pandas.read_csv('classification-master.csv')
    
    videos = []
    videoNames = []
    stables = []
    unstables = []
    uncertains = []
    
    experts = ['shalaka', 'jerry', 'alex', 'julienne', 'sebastian', 'meuller', 'zirui', 'hongtao', 'linus', 'joe', 'debolina']
    
    for i in range(len(df['File name'])):   
        stableCount = 0
        unstableCount = 0
        uncertainCount = 0     
        for j in df.columns:
            if j in experts:
                if df[j][i] == 0:
                    unstableCount += 1
                elif df[j][i] == 1:
                    uncertainCount += 1
                else:
                    stableCount += 1
                    
        stables.append(stableCount / 11 )
        unstables.append(unstableCount / 11 )
        uncertains.append(uncertainCount / 11 )
        videos.append(str(i + 1))
        videoNames.append(df['File name'][i])
    
    data1 =  {'Stable': stables[:26],
             'Uncertain': uncertains[:26],
             'Unstable': unstables[:26]}
    data2 =  {'Stable': stables[26:],
            'Uncertain': uncertains[26:],
            'Unstable': unstables[26:]}
    
    dataAll = {'Stable': stables,
               'Uncertain': uncertains,
               'Unstable': unstables}
    
    frame1 = pandas.DataFrame(data1, index = videos[:26])
    frame2 = pandas.DataFrame(data2, index = videos[26:])
    
    frameAll = pandas.DataFrame(dataAll, index=videos)
        
    # variables
    labels = ['Stable', 'Uncertain', 'Unstable']
    colors = ['green', 'gold', 'red']
    title = 'Expert Evaluations of FSP Videos'
    subtitle = 'Proportion of Classifications per Video'
    
    plot_stackedbar_p(frameAll, labels, colors, title, subtitle)
    
    # plot_stackedbar_p(frame1, labels, colors, title, subtitle)
    # plot_stackedbar_p(frame2, labels, colors, title, subtitle)
    plt.show()
    
if __name__ == "__main__":
    expertsDistribution()
        