# Putting images all together horizontally without using numpy and hstack

import sys
from PIL import Image

# image path
# if height doesn't match with another image, they will align the top side
images = [Image.open(x) for x in ['/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder/1-10-252-360.jpg', '/Users/Shih-Hsi Chien/Desktop/jupyter/image/boulder_180/2-1-0-222.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.show()
# save if needed
# new_im.save('/Users/Shih-Hsi Chien/Desktop/jupyter/image/result/full 28.jpg')

# print(im.size)