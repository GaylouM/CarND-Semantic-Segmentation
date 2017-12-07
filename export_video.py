import cv2
import glob

def process_image_to_video(path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Output.avi', fourcc, 5.0, (576, 160))
    for filename in glob.glob("./runs/images/*.png"):
        image = cv2.imread(filename)
        out.write(image)
        print("finished {0}".format(filename))
    out.release()
path = './'
process_image_to_video(path)
