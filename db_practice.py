import os

path = "C:\\Users\\Binod\\OneDrive - MUET\\Desktop\\New Fyp\\FYP-Project\\TrainingImage"

# imagePath = [os.path.join(path, f) for f in os.listdir(path)]
for d in os.listdir(path):
    newdir = os.path.join(path, d)
    print(newdir)
    imagePath = [os.path.join(newdir, f) for f in os.listdir(newdir)]
print(imagePath)
