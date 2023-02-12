import numpy as np
from phycv import PAGE
from PIL import Image

image = "images/wind_rose.png"

# initialize PAGE class
direction_bins = 10 # number of different directions of edge to be extracted
page = PAGE(direction_bins)


# PAGE Parameters
mu_1 = 0.01  # Center frequency of a normal distributed passband filter ϕ1
mu_2 = 0.35  # Center frequency of log-normal  distributed passband filter ϕ2
sigma_1 = 0.05  # Standard deviation of normal distributed passband filter ϕ1
sigma_2 = 0.8  # Standard deviation of log-normal distributed passband filter ϕ2
s1 = 0.8  # Phase strength of ϕ1
s2 = 0.8  # Phase strength of ϕ2
sigma_LPF = 0.1  # std of the low pass filter
thresh_min = 0.0  # minimum threshold, we keep features < thresh_min
thresh_max = 0.8  # maximum threshold, we keep features > thresh_max
morph_flag = 1  # whether apply morphological operation

new_image = page.run(
    image,
    mu_1,
    mu_2,
    sigma_1,
    sigma_2,
    s1,
    s2,
    sigma_LPF,
    thresh_min,
    thresh_max,
    morph_flag,
)

im = Image.fromarray((new_image * 255).astype(np.uint8))
im.save("images/wind_rose_output.png")


# run this file from phycv-examples folder using the command:
# python page_example.py