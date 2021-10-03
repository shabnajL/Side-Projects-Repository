import pywhatkit as mykit
import cv2


def main():
    # text
    text = "Here's Scarlett, in the garden of a friend's house in London on a sunny summer " \
           "morning, the kind of mornings that are unusual in England. Scarlett is twelve years" \
           " old ('Thirteen in November,' she tells me), and is trying to understand the world " \
           "around her. She asks questions about everything, all the time." \
           "\nChris Rose"

    # converting text to handwritten image
    # rgb: to set the ink color in white board
    # save_to: to save the output image in handwritten version
    mykit.text_to_handwriting(text, rgb=[0, 0, 0], save_to="handwriting_output.png")

    # to fetch the output image
    img = cv2.imread("handwriting_output.png")
    # to show the output image
    cv2.imshow("Text to Handwriting", img)


main()

cv2.waitKey(0)
cv2.destroyAllWindows()
