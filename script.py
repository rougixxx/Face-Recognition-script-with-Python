import cv2
import time
import os

def getListofFiles(dirName):
    fileslist = os.listdir(dirName)
    allFiles = list()
    for entry in fileslist:
        print(entry)
        fullpath = os.path.join(dirName, entry)
        if os.path.isdir(fullpath):
            allFiles = allFiles + getListofFiles(fullpath)
        else:
            allFiles.append(fullpath)

    return allFiles
def main():
    dirName = "pictures"
    listOfFiles = getListofFiles(dirName)

    for i in range(20):
        imagePath = listOfFiles[i]
        print(imagePath)
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255, 0), 2)

        cv2.imshow("Faces found", image)
        cv2.waitKey(4)
        time.sleep(5)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
