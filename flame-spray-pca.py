import cv2
import csv
import pandas
from sklearn.preprocessing import StandardScaler
import tests.luminance as luminance
import tests.twoComponentPCA as twoComponentPCA
import tests.moreComponentPCA as moreComponentPCA
# =========================================================================== #

scaler = StandardScaler()

# standardize the values in array
def standardize(array):
    global scaler
    scaler = StandardScaler()
    scaler = scaler.fit(array)
    standardized = scaler.transform(array)
    return standardized

# =========================================================================== #

# main function
def main():
    
    df = pandas.read_csv('classification-master.csv')
    
    features = []
    frameCount = 0
    videos = []
    stability = []
    test = ''
    temp = []
    tempStability = 1
    sample = None
    for i in range(0, len(df['File name'])):
        
        # if i == 0:
        #     numFrames = 0
            
        #     # read in video
        #     fire = cv2.VideoCapture('./flame-spray-videos/' + df['File name'][i])
        #     print(df['File name'][i])
            
        #     # print error message if you can't read it in
        #     if (fire.isOpened() == False):
        #         print("Error opening video file or stream")
                
        #     # initialize video variables
        #     ret, frame = fire.read()
        #     height, width, channels = frame.shape
        #     vidHeight = height
        #     vidWidth = width
            
        #     # display the video until 'q' is pressed or until it terminates
        #     while (fire.isOpened() and numFrames < 30):
        #         ret, frame = fire.read()
                
        #         if ret == True:
                    
        #             # cv2.imshow('Fire', frame)
                    
        #             temp += luminance.lumArray(frame, vidHeight, vidWidth)
        #             numFrames += 1
        #             if numFrames == 30:
        #                 sample = []
        #                 sample.append(temp)
        #                 temp = []
                    
        #             # terminates the video before it finishes
        #             if cv2.waitKey(25) == ord('q'):
        #                 break
                    
        #         else:
        #             break
        
        if i >= 0:
            numFrames = 0
            
            # read in video
            fire = cv2.VideoCapture('./flame-spray-videos/' + df['File name'][i])
            print(df['File name'][i])
            
            # print error message if you can't read it in
            if (fire.isOpened() == False):
                print("Error opening video file or stream")
                
            # initialize video variables
            ret, frame = fire.read()
            height, width, channels = frame.shape
            vidHeight = height
            vidWidth = width 
            test = ''
            # use 'box' for flsc classifier
            tempStability = int(df['box'][i])
            # tempStability = df['means'][i]
            
            # display the video until 'q' is pressed or until it terminates
            while (fire.isOpened() and numFrames < 250):
                ret, frame = fire.read()
                
                if ret == True:
                    
                    # cv2.imshow('Fire', frame)
                    
                    frameCount += 1
                    temp += luminance.lumArray(frame, vidHeight, vidWidth)
                    numFrames += 1
                    if frameCount % 30 == 0: 
                        numFrames += 1
                        features.append(temp)
                        temp = []
                        videos.append(1)
                        stability.append(tempStability)
                    
                    # terminates the video before it finishes
                    if cv2.waitKey(25) == ord('q'):
                        break
                    
                else:
                    # videos.append(numFrames)
                    # temp = []
                    break
    # print(features)
    features = standardize(features)
    # sample = scaler.transform(sample)
    # print(frameCount)
    # print(features.shape)
    # print(len(videos))
    # sample=None
    twoComponentPCA.applyPCA(features, frameCount, '', videos,
                             stability, sample)
        
    fire.release()
    cv2.destroyAllWindows()
   
        
if __name__ == "__main__":
    main()