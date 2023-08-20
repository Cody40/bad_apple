import cv2
import keyboard

count = int(input("starting frame: "))

while count < 6572:

    if keyboard.is_pressed("space"):
        print("You pressed space")
        break

    imgcode = str()
    a = str()

    img = cv2.imread(('frame' + str(count) +'.jpg'), cv2.IMREAD_GRAYSCALE)

    w, h = 128, 96
    img = cv2.resize(img, (w, h))

    for row in img:
        for pixel in row:
            index = int((pixel/256)*4)
            if index > 2:
                imgcode = (imgcode + "1")
            else:
                imgcode = (imgcode + "0")
                

    def add(pix):
        if (int(imgcode[pix])) > 0:
            return 0
        else:
            return 1


    for row in range(1, 24):
        for i in range(1, 64):
            center = int((((row*4)-4)*128)+((i*2)-2))
            braille = str()
            braille = str(braille + str(add(center+385)))#80
            braille = str(braille + str(add(center+384)))#40
            braille = str(braille + str(add(center+257)))#20
            braille = str(braille + str(add(center+129)))#10
            braille = str(braille + str(add(center+1)))#8
            braille = str(braille + str(add(center+256)))#4
            braille = str(braille + str(add(center+128)))#2
            braille = str(braille + str(add(center)))#1
            a = (a + (str(chr((int(braille, 2))+10240))))
        a = str(a + '\n')

    print(a)
    count +=1

print("finished!")