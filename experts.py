import csv
import pandas
import statistics
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.lines import Line2D
from sklearn.metrics import mean_squared_error
from math import sqrt

# =========================================================================== #

def experts():
    
    df = pandas.read_csv('classification-master.csv')
    
    means = []
    predictions = []
    boxes = []
    videos = []
    baseline = []
    
    computer_similarities = 0
    box_similarities = 0
    
    for i in range(0, len(df['File name'])):
        
        fileName = df['File name'][i]
        
        currMean = df['means'][i]
        if currMean > 1:
            means.append(2)
        else:
            means.append(0)
        # means.append(currMean)
        
        predictions.append(df['computer'][i])
        boxes.append(df['box'][i])
        
        videos.append(int(fileName[12:14]))
        baseline.append(1)
        
        if currMean > 1 and df['computer'][i] > 1:
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
        
    axes = plt.gca()
    axes.set_xlim([0, 53])
    axes.set_ylim([-2, 4])
    
    legend_elements = [Line2D([0],[0], marker = 'o', color = 'w', 
                              label = 'Computer Vision Prediction',
                              markerfacecolor = 'red', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Actual',
                              markerfacecolor = 'black', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Box Prediction',
                              markerfacecolor = 'blue', markersize = 10)]

    
    plt.legend(handles = legend_elements, fontsize = 18)
    
    plt.xlabel('Video Number', fontsize = 24)
    plt.ylabel('Stability (0 = unstable, 1 = unsure, 2 = stable)', fontsize = 24)
    plt.title('Flame Stability vs Video Number', fontsize = 24)
    
    plt.plot(videos, predictions, c = 'red', linewidth = 2)
    plt.plot(videos, means, c = 'black', linewidth = 2)
    plt.plot(videos, boxes, c = 'blue', linewidth = 2)

    print(box_similarities)
    print(computer_similarities)
    
    # rmse_computer = sqrt(mean_squared_error(means, predictions))
    # rmse_box = sqrt(mean_squared_error(means, boxes))
    # rmse_baseline = sqrt(mean_squared_error(means, baseline))
    
    # print(rmse_computer)
    # print(rmse_box)
    # print(rmse_baseline)
    
    plt.show()
    
if __name__ == "__main__":
    experts()
        