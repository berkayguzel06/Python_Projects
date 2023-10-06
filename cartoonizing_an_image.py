import math
import cv2 as cv

IMAGE = input("Image path: ")

img = cv.imread(IMAGE)

X=img.shape[0]#Image shape row
Y=img.shape[1]#Image shape column

resized = cv.resize(img,(480,480))
gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
blur=cv.blur(resized,(2,2))
cascade = cv.Canny(blur,125,175)

casc=[]
countX=0
countY=0
for i in cascade:
    countY=0
    for x in i:
        if x>=1:
            casc.append((countX,countY))
        countY+=1
    countX+=1


#Paint pixels
for i, row in enumerate(blur):
  # get the pixel values by iterating
    for j, pixel in enumerate(blur):
        t = (i,j)
        if t in casc:
            print(f"Processing.....  %{math.floor((i/480)*100)}")
            blur[i][j] = [0, 0, 0]
print("Image Converted")
    
resized2 = cv.resize(blur,(Y,X)) 
        
cv.imshow("BASIC",img)           
cv.imshow('Cartoon',resized2)

cv.waitKey(0)

cv.imwrite("cartoon.jpg",resized2)
