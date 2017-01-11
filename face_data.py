#creating database
import cv2, sys, numpy, os
haar_file = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
datasets = 'bryan_dp'  #All the faces data will be present this folder
sub_data = 'Bryan'     #These are sub data sets of folder, for my faces I've used my name use always different name for different people.
path = os.path.join(datasets, sub_data)
cv2.namedWindow('OpenCV')
print(path)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100) # defining the size of images
face_cascade = cv2.CascadeClassifier(haar_file)
if face_cascade.empty():
    print("Wrong path for haar_file")
    sys.exit()
webcam = cv2.VideoCapture(-1) #'0' is use for my webcam, if you've any other camera attached use '1'
if not webcam.isOpened():
    ret = webcam.open(0)
    if not webcam.isOpened():
        print("Camera not opened", ret)
        sys.exit()

# The program loops until it has 30 images of the face.
#count = 43
count = 1

#for i in range(count):
#    im = cv2.imread(datasets+'/'+str(i+1)+'.jpg')
#    if im == None:
#        print("ERROR", datasets+str(i+i)+'.jpg')
#        sys.exit()
while count <= 50:
    (_, im) = webcam.read()
    if im == None:
        print("Can't read image")
        sys.exit()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if faces == None:
        print("No face")
    else:
        print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
        print(count)
        count += 1
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
