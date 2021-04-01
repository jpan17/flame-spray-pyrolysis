import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import spatial
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.cm as cm
import math
# =========================================================================== #
 
# apply PCA with 2 components
def applyPCA(array, frameCount, test, videos, stability, sample = None):
    
    pca = PCA(n_components = 25)
    
    principalComponents = pca.fit_transform(array)    
    print(pca.explained_variance_ratio_)
    
    cumulative_variance = []
    count = 0
    for ratio in pca.explained_variance_ratio_:
        count += ratio
        cumulative_variance.append(count)
    
    plt.plot(cumulative_variance)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel("Explained Variance (cumulative)", fontsize = 20)
    plt.xlabel("Number of Principal Components", fontsize = 20)
    plt.title("Explained Variance vs Number of Principal Components", fontsize = 24)
    plt.show()
    # print(pca.explained_variance_ratio_)
    
    return