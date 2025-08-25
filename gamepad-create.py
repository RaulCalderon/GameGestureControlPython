import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

while True:

    ask = input("Press A to exit, or press enter to assign (you have 6 seconds): ")
    if ask == "A":
        break
    
    """
    Pressing anything but 'A', you have 6 seconds to assign buttons on emulator
    depending on what you have set below.
    """
    time.sleep(6)

    # Assign values when using the stick gamepad (adjust if needed)
    # gamepad.left_joystick(x_value=32760, y_value=0) # (Right)
    # gamepad.left_joystick(x_value=-32760, y_value=0) # (Left)

    # Assign value to buttons on gamepad
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A) # (Button A)
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Z) # (Button Z)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B) # (Button B)

    # Update gamepad actions
    gamepad.update()

# Releasing the button when object not detected.
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
# gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
# gamepad.left_joystick(x_value=0,y_value=0)
gamepad.update()