import cv2

image=cv2.imread('ehtesham.jpg')

if image is None:
     print("image not found")

else:
    resize_image=cv2.resize(image,(200,200))
    grey=cv2.cvtColor(resize_image,cv2.COLOR_BGR2GRAY)
    HSV=cv2.cvtColor(resize_image,cv2.COLOR_BGR2HSV)
    CrCb=cv2.cvtColor(resize_image,cv2.COLOR_BGR2YCrCb)
    VNG=cv2.cvtColor(resize_image,cv2.COLOR_BGR2RGBA)
    Rectangle=cv2.rectangle(image, (100, 100), (300, 300), (0, 0, 255), 3)
    Circle=cv2.circle(image, (250, 250), 100, (0, 0, 255), 3)
    Text=cv2.putText(image, "Hello Ehtesham !!!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Resized",resize_image)
    cv2.imshow("Grey", grey)
    cv2.imshow("HSV", HSV)
    cv2.imshow("CrCb", CrCb)
    cv2.imshow("VNG", VNG)
    cv2.imshow("Rectangle", Rectangle)
    cv2.imshow("Circle ",Circle)
    cv2.imshow("Text ",Text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

