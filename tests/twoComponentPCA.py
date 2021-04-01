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
# calculate mean stabilities of videos
def calculateMeanStability(array, increment):
    tempSum = 0
    for i in range(0, len(array)):
        tempSum += array[i]
        if (i + 1) % increment == 8:
            print(tempSum / increment)
            tempSum = 0

# calculate distance between two coordinates
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist
 
def printStability(unstableCluster, stableCluster, uncertainCluster, tempPoint):
    stability = 2
    
    toUnstable = calculateDistance(unstableCluster[0], unstableCluster[1], tempPoint[0], tempPoint[1])
    
    toUncertain = calculateDistance(uncertainCluster[0], uncertainCluster[1], tempPoint[0], tempPoint[1])
    
    toStable = calculateDistance(stableCluster[0], stableCluster[1], tempPoint[0], tempPoint[1])  
    
    if toUnstable < toUncertain and toUnstable < toStable:
        stability = 0
        
    print(stability)

 
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
    # print(components.shape)
    frames = 0
    meanStability = []
    for i in range(0, len(videos) - 1):
        isStable = stability[i]
        # print(isStable)
        # print('Video: ' + str(i))
        # tempStability = 2
        
        print("Video:", i)
        unstableCluster = [-278.61387137, 131.97666309]
        stableCluster = [207.35019784, 33.99327416]
        uncertainCluster = [-45.99092389, -36.15059771]
        
        for j in range(0, videos[i]):
            tempPointX = principalComponents[frames, 0]
            tempPointY = principalComponents[frames, 1]
            
            tempPoint = [tempPointX, tempPointY]
            frames += 1     
            
            printStability(unstableCluster, stableCluster, uncertainCluster, tempPoint)
                             
            if isStable > 1.20:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'green')
            elif isStable > .80:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'gold')
            elif isStable >= 0:
                plt.scatter(principalComponents[frames, 0],
                            principalComponents[frames, 1], c = 'red')
            else:
                print("idk")
        # meanStability.append(tempStability)
    
    # videoMeans = []
    # tempSum = 0
    # for m in range(0, len(meanStability)):
    #     tempSum += meanStability[m]
    #     if (m + 1) % 8 == 0:
    #         videoMeans.append(tempSum // 8)
    #         tempSum = 0
    #     # print(calculateMeanStability(meanStability, 8))
        
    # for mean in range(len(videoMeans)):
    #     print("Video:", mean)
    #     print(videoMeans[mean])
        
    # if sample is not None:
        # sample = np.transpose(sample)
        # projected_sample = np.dot(np.transpose(sample), components)
        # projected_sample = np.dot(sample, np.transpose(components))
        # print([c[0:15] for c in components])
        # print(sample[0][0:15])
        # sample = sample / np.mean(sample)
        # # print(pca.mean_)
        # sample = np.dot(sample, pca.components_.T)
        # if pca.whiten:
        #     sample /= np.sqrt(pca.explained_variance_)

        # comp1 = np.dot(components[0], sample[0]) / np.sqrt(sum(components[0]**2))
        # comp2 = np.dot(components[1], sample[0]) / np.sqrt(sum(components[1]**2))
        # projected_sample = [comp1, comp2]
        # print(projected_sample)
        # new_sample = pca.transform(sample)
        # print(new_sample)
        # print(projected_sample)
        # plt.scatter(projected_sample[0],
        #             projected_sample[1], c = 'cyan')
        
    plt.xlabel("Principal Component 1", fontsize = 24)
    plt.ylabel("Principal Component 2", fontsize = 24)

    # decide how you want to cluster them
    choice = input("Do you want to apply 1) kmeans 2) affinity propogation" +
                   " or 3) mean shift to this data? Press enter to skip" +
                   " cluster step.\n")    
     
    legend_elements = [Line2D([0],[0], marker = 'o', color = 'w', 
                              label = 'Stable',
                              markerfacecolor = 'green', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Uncertain',
                              markerfacecolor = 'gold', markersize = 10),
                       Line2D([0],[0], marker = 'o', color = 'w',
                              label = 'Unstable',
                              markerfacecolor = 'red', markersize = 10)]
    
    plt.legend(handles = legend_elements, fontsize = 18)
    # print(pca.explained_variance_ratio_)
    
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
    
  
    # encircle clusters
    for i in range(0, len(kmeans.cluster_centers_)):
        if len(clustersX[i]) > 2:
            encircle(clustersX[i], clustersY[i], ec = "gray", fc = "gray", 
                    alpha = 0.2)
    
    # plt.title("2 Component PCA on " + test + " Values (per pixel) with " + 
    #           "kmeans = " + str(clusterNumber))
    # plt.title("2 component PCA on Bounding Box Pixel Luminosity (per 30 frames)", fontsize = 24)
    
    print(kmeans.cluster_centers_)
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