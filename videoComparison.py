import pandas
import matplotlib.pyplot as plt
import numpy as np
# =============================================#

def videoComparison():
        
    pcaFrames = [30, 60, 90, 120, 150, 180, 210, 240]
    pcaUnstable = [0, 0, 0, 0, 0, 0, 0, 0]
    pcaStable = [1, 1, 1, 1, 1, 1, 1, 1]
    pcaUncertain = [1, 1, 1, 1, 1, 1, 1, 1]
    
    df = pandas.read_csv('supervised_data.csv')
    frames = []
    
    cvUnstable = []
    cvStable = []
    cvUncertain = []
    
    for i in range(len(df['frame'])):
        frames.append(i)
        
        cvStable.append(df['stable'][i] / 2)
        cvUnstable.append(df['unstable'][i] / 2)
        cvUncertain.append(df['uncertain'][i] / 2)
        
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
    fig.suptitle('Stability Classification vs Frames for Reference Videos', fontsize=24)
    ax1.scatter(frames, cvStable, color="green", alpha=0.3)
    ax1.scatter(pcaFrames, pcaStable, 60, color="red", alpha=0.5)
    ax2.scatter(frames, cvUnstable, color="green", alpha=0.3)
    ax2.scatter(pcaFrames, pcaUnstable, 60, color="red", alpha=0.5)
    ax3.scatter(frames, cvUncertain, color="green", alpha=0.3)
    ax3.scatter(pcaFrames, pcaUncertain, 60, color="red", alpha=0.5)
    
    ax1.set_title("Stable Reference Video", fontsize=14)
    ax2.set_title("Unstable Reference Video", fontsize=14)
    ax3.set_title("Uncertain Reference Video", fontsize=14)
    ax2.set_ylabel("Classification", labelpad=20, fontsize=20)   
    
    ax1.tick_params(labelsize=12)
    ax2.tick_params(labelsize=12)
    ax3.tick_params(labelsize=12) 
        
    plt.yticks([0, 1], ["unstable", "stable"])
    plt.ylim((-0.5,1.5))
    # ax2.yticks([0, 1], ["unstable", "stable"], fontsize=16)
    # ax2.ylim((-0.5,1.5))
    # ax3.yticks([0, 1], ["unstable", "stable"], fontsize=16)
    # ax3.ylim((-0.5,1.5))
    # plt.plot(frames, cvUncertain, color="black")
    # plt.scatter(pcaFrames, pcaUncertain, color="orange")
    plt.legend(['Supervised', 'Unsupervised'], fontsize=14, loc='lower right');
    plt.xlabel("Frame Number", fontsize=20)
    # plt.ylabel("Classification", fontsize=20)
    plt.show()
    
if __name__ == "__main__":
    videoComparison()
    
    

