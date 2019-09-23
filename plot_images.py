import matplotlib.pyplot as plt
import cv2
from pathlib import Path
import glob

cats= Path("../animal_images/cats")
dogs= Path("../animal_images/dogs")
cats= cats.glob("*.jpg")
dogs= dogs.glob("*.jpg")
samples = list(cats) + list(dogs)
print(samples)


SMALL_SIZE = 12
BIG_SIZE = 30

plt.rc('axes', titlesize=BIG_SIZE)     # fontsize of the axes title
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels

f, ax = plt.subplots(2,5, figsize=(30,10))
for i in range(10):
    img = cv2.imread(str(samples[i]))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ax[i//5, i%5].imshow(img)
    if i<5:
        ax[i//5, i%5].set_title("Cat")
    else:
        ax[i//5, i%5].set_title("Dog")
    ax[i//5, i%5].axis()
    ax[i//5, i%5].set_aspect('auto')
plt.savefig("plotted_images.png")
