# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step1:
Import the necessary packages to do Erosion and Dilution.


### Step2:
Create the text image of our name using putText from cv2 package.

### Step3:

Create the required structural element.

### Step4:
Apply Erode and Dilution for our NameImage.



### Step5:
Display the output images.



### Step6:
End The Program.





 
## Program:
Name:P.Siva Naga Nitin
Reg.No:212221240037
``` Python
# Import the necessary packages

import cv2
import numpy


# Create the Text using cv2.putText

NameImage = numpy.zeros((100,1000),dtype='uint8')
font = cv2.FONT_ITALIC
cv2.putText(NameImage,'Koduru Sanath Kumar Reddy',(50,70),font,2,(255),5,cv2.LINE_4)
cv2.imshow("Name Image",NameImage)



# Create the structuring element

kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))



# Erode the image

erodeImage = cv2.erode(NameImage,kernel1)



# Dilate the image


dilationImage = cv2.dilate(NameImage,kernel1)

# Displaying the image
cv2.imshow("Name Image",NameImage)
cv2.imshow("Erode Image",erodeImage)
cv2.imshow("Dilated Image",dilationImage)

```
## Output:

### Display the input Image
![name](https://user-images.githubusercontent.com/94154780/169644451-85f3a695-0275-447d-9087-b38956f7701c.png)


### Display the Eroded Image
![name2](https://user-images.githubusercontent.com/94154780/169644578-b36863a8-871c-481d-878f-af5c438d167c.png)

### Display the Dilated Image
![name1](https://user-images.githubusercontent.com/94154780/169644592-4e8edde9-e589-4ff1-bd04-2427c9df2b59.png)


## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
