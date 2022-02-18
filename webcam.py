import sys
import cv2

from time import sleep, time

# define a video capture object
vid = cv2.VideoCapture("rtmp://localhost:1935/live/henrik")

frames = 4
interval = 1
currentFrame = 0

fps = 30
buffer = 0.0
debug = False


_diff = 1000/(fps * 4)
_buffer = _diff * buffer

milliseconds = time() % 1 * 1000


if (debug):
    print(_diff)
    print(_buffer)
    print("grenser")
    print(_buffer)
    print(_diff - _buffer)
    print((_diff) + _buffer)
    print((_diff * 2) - _buffer)
    print("3-4")
    print((_diff*2) + _buffer)

    print((_diff * 3) - _buffer)

    print((_diff * 3) + _buffer)
    print((_diff * 4) - _buffer)

# sys.exit(1)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    milliseconds = time() % 1 * 1000 / fps

    resized = cv2.resize(frame, (854, 480), interpolation=cv2.INTER_AREA)

    if (_buffer < milliseconds < _diff - _buffer):  # 50 -> 200
        if (not debug):
            cv2.imshow("frame0", resized)
        else:
            print(1)

    elif ((_diff) + _buffer < milliseconds < (_diff * 2) - _buffer):  # 300 -> 450
        if (not debug):
            cv2.imshow("frame1", resized)
        else:
            print(2)
    elif ((_diff*2) + _buffer < milliseconds < (_diff * 3) - _buffer):  # 550 -> 700
        if (not debug):
            cv2.imshow("frame2", resized)
        else:
            print(3)
    elif ((_diff * 3) + _buffer < milliseconds < (_diff * 4) - _buffer):  # 800 -> 950
        if (not debug):
            cv2.imshow("frame3", resized)
        else:
            print(4)
    else:
        if(debug):
            print("")
        print(milliseconds)
        print("else")

    # for frame in range(frames):
    #     if (frame == currentFrame):
    #         print("Current frame")
    #         cv2.imshow("frame", frame)
    #         sleep(0.1)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
