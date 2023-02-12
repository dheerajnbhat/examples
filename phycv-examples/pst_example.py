from phycv import PST
from PIL import Image

image = "images/retina.jpg"

# initialize PST class
page = PST()

# PST Parameters
phase_strength = 0.5  # phase strength of PST
warp_strength = 30  # warp strength of PST
sigma_LPF = 0.05  # std of the low pass filter
thresh_min = 0.05  # minimum threshold, we keep features < thresh_min
thresh_max = 0.7  # maximum threshold, we keep features > thresh_max
morph_flag = 1  # whether apply morphological operation

new_image = page.run(
    image,
    phase_strength,
    warp_strength,
    sigma_LPF,
    thresh_min,
    thresh_max,
    morph_flag,
)

im = Image.fromarray(new_image)
im = im.convert("L")
im.save("images/retina_output.jpg")


# run this file from phycv-examples folder using the command:
# python pst_example.py