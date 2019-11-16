# 1st import the package and check its version
import MTM
print("MTM version : ", MTM.__version__)
from MTM import matchTemplates, drawBoxesOnRGB
import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

image = "Testcopy.png"
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(image, cmap="gray")

temp0 = image[784:784+400, 946:946+414] # with well 49
plt.axis("off")
plt.imshow(temp0, cmap="gray")

listTemplate = [('temp0', temp0)]
Hits = matchTemplates(listTemplate, image, N_object=4, score_threshold=0.3, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0.3)
print(Hits)

# Generate gaussian distributed noise, the noise intensity is set by the level variable
noise = np.empty_like(image, dtype="int8")
level = 50
cv2.randn(noise,(0),(level)) # Matrix element are 0 in average

plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(noise, cmap="gray")

imageNoise = cv2.add(image,noise, dtype=cv2.CV_8U)

plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(imageNoise, cmap="gray")


# Call again matchTemplates with the noisy image this time, but the same template
Hits_Noise = matchTemplates(listTemplate, imageNoise, N_object=4,  score_threshold=0.3, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0.3)

print("Initial detections")
print(Hits)

print("\nDetections with noise")
print(Hits_Noise)

Overlay1 = drawBoxesOnRGB(image, Hits, boxThickness=5)
Overlay2 = drawBoxesOnRGB(imageNoise, Hits_Noise, boxThickness=5)

plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(Overlay1)

plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(Overlay2)
