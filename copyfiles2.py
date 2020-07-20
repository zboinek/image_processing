#copy files in directory
import os, shutil

IMAGE_DIR = "./Coronahack-Chest-XRay-Dataset/Coronahack-Chest-XRay-Dataset/"
TRAIN_DIR = IMAGE_DIR + 'train/'
FILES = os.listdir(TRAIN_DIR)
def renameFiles(FILE_LIST):
    new_FILE_LIST = []
    for file in FILE_LIST:
        file = file.rsplit('.',1)[0] + "_2.jpeg"
        new_FILE_LIST.append(file)
    return new_FILE_LIST
        
FILES1 = renameFiles(FILES)


for i in range(0, len(FILES)):
    shutil.copyfile(TRAIN_DIR + FILES[i], TRAIN_DIR + FILES1[i])