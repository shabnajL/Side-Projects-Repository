import cv2
from google.colab.patches import cv2_imshow # because Google colab crashes when try to display image using cv2.imshow()
import numpy

#reading the image
#img_rgb = cv2.imread("../content/testimg-2.jpg")
img_rgb = cv2.imread("../content/testimg-3.jpg")
 
#edges
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # work on gray scale
img_blur = cv2.medianBlur(img_gray, 5)
img_edged = cv2.adaptiveThreshold(img_blur, 255, # binary threshold
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9)

# apply bilateral filter with "big numbers" to get the cartoonized effect:
color = cv2.bilateralFilter(img_rgb, 10, 250, 250)

# Perform 'bitwise and' with the edged img as mask in order to set these values to the output
img_cartoon = cv2.bitwise_and(color, color, mask=img_edged)

#displaying the real image
cv2_imshow(img_rgb)
#diaplaying the image with edges
cv2_imshow(img_edged)
#output as the Cartoon version
cv2_imshow(img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
