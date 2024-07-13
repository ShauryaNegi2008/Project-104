import cv2

img=cv2.imread("solar-system.jpg")



cv2.putText(img,"Sun",(7,235),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255))
cv2.putText(img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Venus",(190,260),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Earth",(290,270),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Mars",(390,260),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))
cv2.putText(img,"Jupiter",(550,400),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255))
cv2.putText(img,"Saturn",(775,325),cv2.FONT_HERSHEY_COMPLEX,1.1,(255,255,255))
cv2.putText(img,"Uranus",(930,300),cv2.FONT_HERSHEY_COMPLEX,1.1,(255,255,255))
cv2.putText(img,"Neptune",(1080,300),cv2.FONT_HERSHEY_COMPLEX,1.1,(255,255,255))

cv2.imshow("hi",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)