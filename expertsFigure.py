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
from statistics import mean, stdev
# =========================================================================== #

def expertsFigure():
    
    df = pandas.read_csv('classification-master.csv')
    
    means = []
    computer = []
    boxes = []
    pca = []
    numbers = []
    
    computer_similarities = 0
    box_similarities = 0
    pca_similarities = 0
    
    computer_false_positive = 0
    computer_true_positive = 0
    computer_false_negative = 0
    computer_true_negative = 0
    
    pca_false_positive = 0
    pca_true_positive = 0
    pca_false_negative = 0
    pca_true_negative = 0
    
    box_false_positive = 0
    box_true_positive = 0
    box_false_negative = 0
    box_true_negative = 0
        
    for i in range(0, len(df['File name'])):
        numbers.append(i)
        
        fileName = df['File name'][i]
        
        currMean = df['means'][i]
        means.append(currMean)
        
        computer.append(df['computer'][i])
        boxes.append(df['box'][i])
        pca.append(df['pca'][i])
                    
        if currMean <= 1.2 and df['computer'][i] <= 1.2:
            computer_true_positive += 1
            computer_similarities += 1
        elif currMean > 1.2 and df['computer'][i] > 1.2:
            computer_true_negative += 1
            computer_similarities += 1
        elif currMean <= 1.2 and df['computer'][i] > 1.2:
            computer_false_negative += 1
        elif currMean > 1.2 and df['computer'][i] <= 1.2: 
            computer_false_positive += 1
        else: 
            pass
        
        if currMean <= 1.2 and df['box'][i] <= 1.2:
            box_true_positive += 1
            box_similarities += 1
        elif currMean > 1.2 and df['box'][i] > 1.2:
            box_true_negative += 1
            box_similarities += 1
        elif currMean <= 1.2 and df['box'][i] > 1.2:
            box_false_negative += 1
        elif currMean > 1.2 and df['box'][i] <= 1.2:
            box_false_positive += 1
        else:
            pass
        
        if currMean <= 1.2 and df['pca'][i] <= 1.2:
            pca_true_positive += 1
            pca_similarities += 1
        elif currMean > 1.2 and df['pca'][i] > 1.2:
            pca_true_negative += 1
            pca_similarities += 1
        elif currMean <= 1.2 and df['pca'][i] > 1.2:
            pca_false_negative += 1
        elif currMean > 1.2 and df['pca'][i] <= 1.2:
            pca_false_positive += 1
        else:
            pass
    
    print('Computer True positive rate:', (computer_true_positive)/(computer_true_positive + computer_false_negative))
    print('Computer False positive rate:', (computer_false_positive)/(computer_false_positive + computer_true_negative))
    print('Computer True negative rate:', (computer_true_negative)/(computer_true_negative + computer_false_positive))
    print('Computer False negative rate:', (computer_false_negative)/(computer_false_negative + computer_true_positive))
    
    print('Box True positive rate:', (box_true_positive)/(box_true_positive + box_false_negative))
    print('Box False positive rate:', (box_false_positive)/(box_false_positive + box_true_negative))
    print('Box True negative rate:', (box_true_negative)/(box_true_negative + box_false_positive))
    print('Box False negative rate:', (box_false_negative)/(box_false_negative + box_true_positive))
    
    print('PCA True positive rate:', (pca_true_positive)/(pca_true_positive + pca_false_negative))
    print('PCA False positive rate:', (pca_false_positive)/(pca_false_positive + pca_true_negative))
    print('PCA True negative rate:', (pca_true_negative)/(pca_true_negative + pca_false_positive))
    print('PCA False negative rate:', (pca_false_negative)/(pca_false_negative + pca_true_positive))

    print('Box similarities:', box_similarities)
    print('Computer similarities:', computer_similarities)
    print('PCA similarities:', pca_similarities)
    
    fig, (ax1, ax2) = plt.subplots(2)
    
    predictions1 = np.array([means[0:27], boxes[0:27], pca[0:27], computer[0:27]])
    predictions2 = np.array([means[27:], boxes[27:], pca[27:], computer[27:]])
    
    predictionMethods = ('Human', 'FLSC', 'Unsupervised', 'Supervised')
    plt.rcParams["figure.figsize"] = (8, 8)
    
    im1 = ax1.imshow(predictions1, interpolation='none', cmap='RdYlGn')
    im2 = ax2.imshow(predictions2, interpolation='none', cmap='RdYlGn', extent=[27,53, 4, 0])
    
    ax1.yaxis.set_ticks(np.arange(0, 4, 1))
    ax1.set_yticklabels(predictionMethods, fontsize=14)
    ax1.xaxis.set_ticks(np.arange(0, 26, 5))
    ax2.yaxis.set_ticks(np.arange(.5, 4.5, 1))
    ax2.xaxis.set_ticks(np.arange(27, 53, 5))
    ax2.set_yticklabels(predictionMethods, fontsize=14)
    ax = fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Video Number", fontsize = 18)
    plt.ylabel("Method", fontsize = 18)
    ax.yaxis.set_label_coords(-.1, .5)
    ax1.tick_params(axis='x', labelsize=14)
    ax2.tick_params(axis='x', labelsize=14)
    
    
    axins = inset_axes(ax2,
                   width="2%", 
                   height="280%", 
                   loc='lower left',
                   bbox_to_anchor=(1.01, 0, 1, 1),
                   bbox_transform=ax2.transAxes,
                   borderpad=0,
                   )
    
    cbar = fig.colorbar(im1, orientation='vertical', ticks=[0, 1, 2], aspect=80, cax = axins)
    cbar.ax.set_yticklabels(['Unstable', 'Uncertain', 'Stable'], fontsize=14)
    
    plt.show()
    
if __name__ == "__main__":
    expertsFigure()
        