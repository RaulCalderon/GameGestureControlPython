# Game control by object detection.

This script allows you to control emulator games detecting objects by color using the web cam.

## Requirements
- Python 3.7+
- OpenCV
- NumPy
- vgamepad

## Install
```bash
pip install opencv-python numpy vgamepad
```

## Use
1. Run `gamepad-create.py` to configure the virtual gamepad.
2. Run `app.py` to start detecting.
3. Press 'q' to exit.

## Configs
- Adjust `lower_orange` and `upper_orange` to detect other colors.
- Modify `minSize` and `maxSize` to adjust the sensitivity.

## Use Cases
- Game control on emulators through computer vision.
- Control automation using the object detection.
- Educational projects using computer vision.
- **Originally developed and tested with racing games on emulators**

## Legal Notes
This project is a personal computer vision experiment.
The user is responsible for complying with the local laws or terms and conditions for any software or emulator that uses this tool. It is not affiliated with or endorsed by any company. The game and console names mentioned are trademarks of their respective owners.

