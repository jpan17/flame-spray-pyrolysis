import csv
import pandas
import statistics
import matplotlib.pyplot as plt
import numpy as np 
import random
from matplotlib.lines import Line2D
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib.pyplot import colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
# =========================================================================== #

def expertsFigure():
    
    df = pandas.read_csv('classification-master.csv')
    
    means = []
    computer = []
    boxes = []
    pca = []
    randoms = []
    numbers = []
    
    computer_similarities = 0
    box_similarities = 0
    pca_similarities = 0
    rand_similarities = 0
    
    false_positive = 0
    all_positive = 0
    
    for i in range(0, len(df['File name'])):
        numbers.append(i)
        
        fileName = df['File name'][i]
        
        currMean = df['means'][i]
        means.append(currMean)
        
        computer.append(df['computer'][i])
        boxes.append(df['box'][i])
        pca.append(df['pca'][i])
        
        rand = random.uniform(0, 1);
        if rand >= 0.5:
            randoms.append(2)
        else:
            randoms.append(0)
        
        if currMean > 1 and df['computer'][i] > 1:
            all_positive += 1
            computer_similarities += 1
        elif currMean <= 1 and df['computer'][i] <= 1:
            computer_similarities += 1
        else: 
            pass
        
        if currMean > 1 and df['box'][i] > 1:
            box_similarities += 1
        elif currMean <= 1 and df['box'][i] <= 1:
            box_similarities += 1
        else:
            pass
        
        if currMean > 1 and df['pca'][i] > 1:
            pca_similarities += 1
        elif currMean <= 1 and df['pca'][i] <= 1:
            pca_similarities += 1
        else:
            pass
                
        if currMean > 1 and randoms[i] > 1:
            rand_similarities += 1
        elif currMean <= 1 and randoms[i] <= 1:
            rand_similarities += 1
        else:
            pass

    print(box_similarities)
    print(pca_similarities)
    print(computer_similarities)
    
    fig, (ax1, ax2) = plt.subplots(2)
    
    predictions1 = np.array([means[0:27], boxes[0:27], pca[0:27], computer[0:27]])
    predictions2 = np.array([means[27:], boxes[27:], pca[27:], computer[27:]])
    
    predictionMethods = ('Human', 'FLSC', 'Unsupervised', 'Supervised')
    plt.rcParams["figure.figsize"] = (8, 8)
    
    im1 = ax1.imshow(predictions1, interpolation='none', cmap='RdYlGn')
    im2 = ax2.imshow(predictions2, interpolation='none', cmap='RdYlGn', extent=[27,53, 4, 0])
    
    ax1.yaxis.set_ticks(np.arange(0, 4, 1))
    ax1.set_yticklabels(predictionMethods)
    ax1.xaxis.set_ticks(np.arange(0, 26, 5))
    ax2.yaxis.set_ticks(np.arange(.5, 4.5, 1))
    ax2.xaxis.set_ticks(np.arange(27, 53, 5))
    ax2.set_yticklabels(predictionMethods)
    plt.xlim(27, 53)
    ax = fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Video Number", fontsize = 18)
    plt.ylabel("Method", fontsize = 18)
    ax.yaxis.set_label_coords(-.1, .5)
    
    
    axins = inset_axes(ax2,
                   width="2%",  # width = 5% of parent_bbox width
                   height="280%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.01, 0, 1, 1),
                   bbox_transform=ax2.transAxes,
                   borderpad=0,
                   )
    
    cbar = fig.colorbar(im1, orientation='vertical', ticks=[0, 1, 2], aspect=80, cax = axins)
    cbar.ax.set_yticklabels(['Unstable', 'Uncertain', 'Stable'])
    
    plt.show()
    
if __name__ == "__main__":
    expertsFigure()
        