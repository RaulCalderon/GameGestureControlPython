import cv2
import numpy as np
import vgamepad as vg

# We create a virtual gamepad for the emulator
gamepad = vg.VX360Gamepad()

# Video Capture
cap = cv2.VideoCapture(0)

"""
np.array(H,S,V)

H = Hue           0 - 180
S = Saturation    0 - 255
V = Value         0 - 255
"""

# This is set to detect organge. (Adjust the steering wheel color as needed.)
lower_orange = np.array([5, 200, 100], np.uint8)
upper_orange = np.array([10, 255, 255], np.uint8)

# Maximum and minimum sizer to detect the object.
minSize = 2000
maxSize = 40000

while True:

    # ret: This boolean is to indicate if the capture was successfuly.
    # frame: Contains the image snapshot in RGB format.
    ret, frame = cap.read()

    # It there is an error in the capture, finish.
    if not ret:
        break

    # Flip the camera image (mirror effect).
    frame = cv2.flip(frame, 1)

    # We convert BGR to HSV values.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # We create a mask of range for the lower and upper values.
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # contours: We store the contours of the detections.
    # hierarchy: We store the hierarchy of the detected contours.
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # We get every contour detected.
    for contour in contours:

        # Get the area for each contour and return the area in pixrls.
        area = cv2.contourArea(contour)

        # Verify if the area is between a specific range to draw
        # the contour of the object to detect.
        if minSize < area < maxSize:

            # Adjust a rectangle min area around the contour.
            rect = cv2.minAreaRect(contour)

            # Calculate the vertexs of the rectangle.
            box = cv2.boxPoints(rect)

            # Integer matrix
            box = np.intp(box)

            """
            We set the angle of the object.
            (x,y): Coordinates of the rectangle.
            (w,h): Width and Height of the rectangle.
            """
            (x,y), (w,h), angle = rect
            if w > h:
                angle = angle + 90

            """
            Draw the object contour.
            frame: The original image.
            [box]: The matrix contour.
            0: Index for the contorn in the contours list.
            (0,255,0,2): Color of the contour to draw.
            """
            cv2.drawContours(frame,[box],0,(0,255,0,2))
            
            # currentPos = (int(x),int(y))
            # cv2.putText(frame, str(angle), (50,50), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,0))
            # cv2.putText(frame, str(currentPos), (50,100), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,0))

            # We assign the press button action value.
            # (Acelerate pressing 'A' when detecting object).
            # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

            # We assign values for the move stick actions (X axis - left or right)
            gamepad.left_joystick(x_value=int((angle - 92.5) / 0.0022), y_value=0)

            """
            If detects the object below 320 in Y axis, press 'A' to acelerate and release 'B' (if activated item).
            If y > 320, release 'A' to slow down and activate item (if any).
            """
            if y < 320:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

            # Update gamepad actions
            gamepad.update()


    cv2.imshow("Object Detector", frame)
    # cv2.imshow("mask", mask)
    # cv2.imshow("frame", frame)
    # cv2.imshow("hsv", hsv)
    
    # Exit pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)        
gamepad.left_joystick(x_value=0,y_value=0)
gamepad.update()