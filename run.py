import frameProcessor as fp
import time

IMAGE_DIR = "Images"
FRAMERATE = 2

frames = [
    "TEST.png"
]

def main():
    for frame in frames:
        frame = fp.processFrame(f"{IMAGE_DIR}/{frame}")
        outputFrame(frame)

def outputFrame(frame):
    for row in frame:
        out = ""
        for px in row:
            out += "x" if px else " "
        print(out)
        time.sleep(1/(FRAMERATE * len(frame)))

main()