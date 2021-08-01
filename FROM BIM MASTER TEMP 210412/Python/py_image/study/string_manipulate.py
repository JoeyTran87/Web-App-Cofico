
import time
im_name = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_image\screen_shot_full.png"

t = time.strftime("%y%m%d%H%M%S",time.localtime(time.time()))
crop_im_name = f"{im_name[:-len(im_name.split('.')[-1])-1]}-crop-{t}.png"

print(crop_im_name)