import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import spatial
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.cm as cm
# =========================================================================== #

# apply PCA with 2 components
def applyPCA(array, frameCount, test, videos, stability, sample = None):
    
    pca = PCA(n_components = 2)
    
    principalComponents = pca.fit_transform(array)
    # print(type(array))
    # print(array.shape)
    # print(principalComponents.shape)
    # print(sample.shape)
    # print(type(sample))
    components = (pca.components_)
    print(components.shape)
    frames = 0
    
    for i in range(0, len(videos) - 1):
        isStable = stability[i]
        # print(isStable)
        for j in range(0, videos[i]):

            if isStable > 1.25:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'blue')
            elif isStable > .75:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'purple')
            elif isStable >= 0:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'red')
            else:
                print("idk")
            
            frames += 1        

    if sample is not None:
        # sample = np.transpose(sample)
        # projected_sample = np.dot(np.transpose(sample), components)
        projected_sample = np.dot(sample, np.transpose(components))
        print(projected_sample)
        # new_sample = pca.transform(sample)
        plt.scatter(projected_sample[0, 0],
                    projected_sample[0, 1], c = 'green')
        
    plt.xlabel("Principal Component 1", fontsize = 24)
    plt.ylabel("Principal Component 2", fontsize = 24)
    
    # decide how you want to cluster them
    choice = input("Do you want to apply 1) kmeans 2) affinity propogation" +
                   " or 3) mean shift to this data? Press enter to skip" +
                   " cluster step.\n")    
     
    legend_elements = [Line2D([0],[0], marker = 'o', color = 'w', 
                              label = 'Stable',
                              markerfacecolor = 'blue', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Unstable',
                              markerfacecolor = 'red', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Uncertain',
                              markerfacecolor = 'purple', markersize = 10)]
    
    plt.legend(handles = legend_elements, fontsize = 18)
    print(pca.explained_variance_ratio_)
    
    if choice == "1":
        clusterNum = input("How many clusters do you want? (no more than 5) \n")
        applyKmeans(principalComponents, int(clusterNum), test)
    elif choice == "2":
        applyAffinity(principalComponents, test)
    elif choice == "3":
        applyMeanShift(principalComponents, test)
    else:
        # plt.title("2 Component PCA on " + test + " Pixel Values")
        plt.title("2 component PCA on Bounding Box Pixel Luminosity (per 30 frames)", fontsize = 24)
        
    plt.show()
    return

# =========================================================================== #

# apply kmeans algorithm to data
def applyKmeans(array, clusterNumber, test):
    
    
    kmeans = KMeans(n_clusters = clusterNumber)
    kmeans.fit(array)
    
    # instnatiate  dictionaries
    clustersX = {}
    clustersY = {}
    
    for i in range(0, len(kmeans.cluster_centers_)):
        clustersX[i] = []
        clustersY[i] = []
    
    # .. and fill them
    for i in range(0, len(array)):
        label = kmeans.labels_[i]
        clustersX[label].append(array[i, 0])
        clustersY[label].append(array[i, 1])
    
  
    # # encircle clusters
    # for i in range(0, len(kmeans.cluster_centers_)):
    #     if len(clustersX[i]) > 2:
    #         encircle(clustersX[i], clustersY[i], ec = "orange", fc = "gold", 
    #                 alpha = 0.2)
    
    # plt.title("2 Component PCA on " + test + " Values (per pixel) with " + 
    #           "kmeans = " + str(clusterNumber))
    plt.title("2 component PCA on Bounding Box Pixel Luminosity (per frame)", fontsize = 24)
    
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
                color = 'black')
    return

# =========================================================================== #

# apply affinity propagation algorithm to data
def applyAffinity(array, test):
    affinity = AffinityPropagation(damping = 0.5)
    affinity.fit(array)
    
    # instnatiate  dictionaries
    clustersX = {}
    clustersY = {}
    
    for i in range(0, len(affinity.cluster_centers_)):
        clustersX[i] = []
        clustersY[i] = []
    
    # .. and fill them
    for i in range(0, len(array)):
        label = affinity.labels_[i]
        clustersX[label].append(array[i, 0])
        clustersY[label].append(array[i, 1])
    
  
    # encircle clusters
    for i in range(0, len(affinity.cluster_centers_)):
        if len(clustersX[i]) > 2:
            encircle(clustersX[i], clustersY[i], ec = "orange", fc = "gold", 
                    alpha = 0.2)
    
    plt.title("2 Component PCA on " + test + " Values (per pixel) with " + 
              "affinity propagation")
    plt.scatter(affinity.cluster_centers_[:,0], affinity.cluster_centers_[:,1],
                color = 'black')
    return

# =========================================================================== #

# apply mean shift algorithm to data
def applyMeanShift(array, test):
    meanshift = MeanShift(bandwidth = 80, min_bin_freq = 5)
    meanshift.fit(array)
    
    # instnatiate  dictionaries
    clustersX = {}
    clustersY = {}
    
    for i in range(0, len(meanshift.cluster_centers_)):
        clustersX[i] = []
        clustersY[i] = []
    
    # .. and fill them
    for i in range(0, len(array)):
        label = meanshift.labels_[i]
        clustersX[label].append(array[i, 0])
        clustersY[label].append(array[i, 1])
    
  
    # encircle clusters
    for i in range(0, len(meanshift.cluster_centers_)):
        if len(clustersX[i]) > 2:
            encircle(clustersX[i], clustersY[i], ec = "orange", fc = "gold", 
                    alpha = 0.2)
    
    plt.title("2 Component PCA on " + test + " Values (per pixel) with " + 
              "mean shift")
    plt.scatter(meanshift.cluster_centers_[:,0], meanshift.cluster_centers_[:,1],
                color = 'black')
    
    return

# =========================================================================== #
# helper function to make cluster visualization easier
def encircle(x, y, ax = None, **kw):
    if not ax: ax = plt.gca()
    p = np.c_[x, y]
    hull = spatial.qhull.ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices,:], **kw)
    ax.add_patch(poly)