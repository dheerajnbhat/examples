from phycv import VEVID
from PIL import Image

image = "images/street_scene.png"

# initialize VEVID class
vevid = VEVID()

# VEVID parameters
S = 0.2  # phase strength
T = 0.001  # variance of the spectral phase function
b = 0.16  # regularization term
G = 2.5  # phase activation gain

new_image = vevid.run(image, S, T, b, G)

im = Image.fromarray(new_image)
im.save("images/street_scene_output.png")


# run this file from phycv-examples folder using the command:
# python vevid_example.py