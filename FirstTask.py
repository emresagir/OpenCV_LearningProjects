from cv2 import cv2 as cv
import numpy as np 
import time

def empty(a):
    pass

def getContours(imgCanny, imgOrg):
    contours, hierarchy = cv.findContours(imgCanny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # Resimdeki kapalı kenarlar tespit edilir.
    for cnt in contours:
        area = cv.contourArea(cnt) # Alan hesabı yapılarak çok küçük boyuttaki şekillerin filtresi yapılır.
        if area > 10000:
            cv.drawContours(imgOrg, cnt, -1, (255,0,0), 3) # Kenarlar çizdirilir.
            (x,y),(MA,ma),angle = cv.fitEllipse(cnt) # Major, Minor ve açı hesabı yapılır.
            ellipse = cv.fitEllipse(cnt) # Şekilin içerisine elips sığdırılır.
            cv.ellipse(imgOrg, ellipse, (0,255,0), 2) #Elips çizdirilir.
            return angle # Hesaplama sonucu bulunan açı geri döndürülür.
    
def trackbarFunc():
    f_min = cv.getTrackbarPos("First Min", "TrackBars") # Trackbarlardan Treshold değerleri alınır.
    s_min = cv.getTrackbarPos("Sec Min", "TrackBars") 
    return f_min, s_min

def filterFunc(f_min, s_min):
    imgOrg = frame 
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Kameradan alınan görüntü grayScale'a çevirilir.
    imgCanny = cv.Canny(imgGray, f_min, s_min)  # Gray resim üzerine Canny işlemi uygulanır.
    return imgOrg, imgCanny

def angleCalculationFunc(imgCanny, imgOrg):

    angle = getContours(imgCanny, imgOrg) # Canny resim Kenar hesaplama fonksiyonuna gönderilir ve tespit edilen şeklin açısı döndürülür.
    strAngle = str(angle) 
    cv.putText(imgOrg, strAngle, (50,50), font, 1, (0,255,255), 2) # Videonun üzerine açı değeri yazdırılır.

def showResults():
    cv.imshow("Video", imgCanny)   
    cv.imshow("Original Video", imgOrg)

def ascend(cm):
    pass
def descend(cm):
    pass
def moveForward(cm):
    pass
def moveBackward(cm):
    pass
def moveRight(cm):
    pass
def moveLeft(cm):
    pass
def turnRight():
    pass
def turnLeft():
    pass

def isDoorsInFrame(): #Kapı framede mi kontrol fonksiyonu 0 yada 1 dönmeli.
    pass

def isDoorsFound(): #Kapı arama fonksiyonu, 0 yada 1 dönmeli.
    pass

def movingFunct(doorsFound, doorsInFrame, angle):
    if doorsFound == 0: # Tarama algoritması
        doorsFound = isDoorsFound() #returns 0 or 1

    if doorsFound == 1: # Kapıya ilerleme algoritması
      
        if 85 < angle < 95: # Kapı ortalandı.
            doorsInFrame = isDoorsInFrame() #returns 0 or 1
           
            if doorsInFrame == 0:
                moveForward(50)
       
        elif angle < 85:
            pass #90 a çıkılmaya çalışılır.
      
        elif angle > 95:
            pass #90 a inilmeye çalışılır.


capture = cv.VideoCapture(0)  # Treshold seviyesinin el ile ayarlanması için trackbar oluşturulur.
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("First Min","TrackBars",100,333,empty) 
cv.createTrackbar("Sec Min","TrackBars",200,333,empty)

font = cv.FONT_HERSHEY_SIMPLEX 

doorsFound = 0 #kapı bulundu/bulunmadı değişkeni kontrol sağlayacak
doorsInFrame = 0 #kapıya yaklaşılırken framede olup olmadığı kontrol edilecek
wantedDepth = 100 #kapının ortalandığı, istenilen derinlik

descend(wantedDepth) #istenilen derinliğe görüntü işleme başlamadan önce inilir


while True:
    isTrue, frame = capture.read()
   
    (f_min, s_min) = trackbarFunc()
    (imgOrg, imgCanny) = filterFunc(f_min, s_min)
    angleCalculationFunc(imgCanny, imgOrg)
    showResults()

    #Buraya kadar görüntü işleme kısmı, sonrası hareket.

    movingFunct(angle)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()