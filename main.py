import cv2
import numpy
NameImage = numpy.zeros((100,1000),dtype='uint8')
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(NameImage,'Popuri Siva Naga Nithin',(50,70),font,2,(255),5,cv2.LINE_4)
cv2.imshow("Name Image",NameImage)
kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
erodeImage = cv2.erode(NameImage,kernel1)
dilationImage = cv2.dilate(NameImage,kernel1)
cv2.imshow("Erode Image",erodeImage)
cv2.imshow("Dilated Image",dilationImage)
cv2.waitKey(0)

cv2.destroyAllWindows()