from cv2 import cv2 as cv
import numpy as np 
import time

def empty(a):
    pass

def getContours(imgCanny, imgOrg, doors):
    contours, hierarchy = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # Resimdeki kapalı kenarlar tespit edilir.
    for cnt in contours:
        area = cv.contourArea(cnt) # Alan hesabı yapılarak çok küçük boyuttaki şekillerin filtresi yapılır.
        if area > 10000:
            doors = doors + 1
            cv.drawContours(imgOrg, cnt, -1, (255,0,0), 3) # Kenarlar çizdirilir.
            (x,y),(MA,ma),angle = cv.fitEllipse(cnt) # Major, Minor ve açı hesabı yapılır.
            ellipse = cv.fitEllipse(cnt) # Şekilin içerisine elips sığdırılır.
            cv.ellipse(imgOrg, ellipse, (0,255,0), 2) #Elips çizdirilir.
            return angle, doors # Hesaplama sonucu bulunan açı geri döndürülür.
    
capture = cv.VideoCapture(0)  # Treshold seviyesinin el ile ayarlanması için trackbar oluşturulur.
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("First Min","TrackBars",100,333,empty) 
cv.createTrackbar("Sec Min","TrackBars",200,333,empty)

font = cv.FONT_HERSHEY_SIMPLEX 

doors = 0

while True:
    isTrue, frame = capture.read()
        
    f_min = cv.getTrackbarPos("First Min", "TrackBars") # Trackbarlardan Treshold değerleri alınır.
    s_min = cv.getTrackbarPos("Sec Min", "TrackBars") 
    
    imgOrg = frame
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Kameradan alınan görüntü grayScale'a çevirilir.
    imgCanny = cv.Canny(imgGray, f_min, s_min)  # Gray resim üzerine Canny işlemi uygulanır.

    #BURADAKALDIM angle none geldiği için yanına doors yazamıyorum
    angle= getContours(imgCanny, imgOrg, doors) # Canny resim Kenar hesaplama fonksiyonuna gönderilir ve tespit edilen şeklin açısı döndürülür.
    strAngle = str(angle) 
   # strdoorsfounded = str(doorsFounded)

    cv.putText(imgOrg, strAngle, (50,50), font, 1, (0,255,255), 2) # Videonun üzerine açı değeri yazdırılır.
   #cv.putText(imgOrg, strdoorsfounded, (50,100), font, 1, (0,255,255), 2)

    cv.imshow("Video", imgCanny)   
    cv.imshow("Original Video", imgOrg)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
