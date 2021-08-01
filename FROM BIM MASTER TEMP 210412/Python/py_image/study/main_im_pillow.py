from PIL import ImageColor, Image
#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,sys
os.chdir(os.getcwd())


#---------------------------------------------------------#
# Study color
#---------------------------------------------------------#
#https://www.w3schools.com/tags/ref_colornames.asp
# print (ImageColor.getcolor('turquoise','RGBA')) 

#---------------------------------------------------------#
# Read image
#---------------------------------------------------------#
def read_img():
    pia_img = Image.open('20191008_151142(1).jpg')
    width, height = pia_img.size
    file_name = pia_img.filename
    format = pia_img.format # extension
    format_description = pia_img.format_description

# print(format_description)
#---------------------------------------------------------#
# New image
#---------------------------------------------------------#
def new_img():
    im = Image.new('RGBA',(200,100),'red')
    im.save("new_image.png")

#---------------------------------------------------------#
# Crop image
#---------------------------------------------------------#
def crop_img():
    im = Image.open("new_image.png")
    cropim = im.crop((25,25,50,50))
    cropim.save("new_image_crop.png")
# crop_img()

#---------------------------------------------------------#
# Copy Paste image
#---------------------------------------------------------#
def copy_paste():
    im1 = Image.new('RGBA',(200,100),'red')
    im2 = Image.new('RGBA',(200,100),'green')
    cropim = im2.crop((25,25,50,50))
    im3 = im1.copy()
    im3.paste(cropim,(0,0))

    im3.save("new_image_copy_paste.png")

# copy_paste()
#---------------------------------------------------------#
# JPG to PNG
#---------------------------------------------------------#
def jpg_to_png():
    pia_img = Image.open('20191008_151142(1).jpg')
    pia_img.save('20191008_151142(1).png')
# jpg_to_png()
#---------------------------------------------------------#
# Clone tile
#---------------------------------------------------------#
def clone_tile():
    pia_img = Image.open('20191008_151142(1).png')
    cropim = pia_img.crop((200,200,400,400))
    w,h = cropim.size
    pia_img_copy = pia_img.copy()
    imW, imH = pia_img_copy.size

    for left in range(0,imW,w):
        for top in range(0,imH,h):
            print(left,top)
            pia_img_copy.paste(cropim,(left,top))

    pia_img_copy.save('clone_tile.png')
# clone_tile()
#---------------------------------------------------------#
# Resize
#---------------------------------------------------------#
def resize_img():
    pia_img = Image.open('20191008_151142(1).png')
    imW, imH = pia_img.size
    new_pia_img = pia_img.resize((int(imW/2),int(imH/2)))
    new_pia_img.save('resize.png')
# resize_img()
#---------------------------------------------------------#
# Rotate
#---------------------------------------------------------#
def rotate_img():
    pia_img = Image.open('resize.png')
    pia_img.rotate(90).save('rotate.png')
# rotate_img()
def rotate_img_expand():
    pia_img = Image.open('resize.png')
    pia_img.rotate(15,expand= True).save('rotate_expand.png')
# rotate_img_expand()

#---------------------------------------------------------#
# Flip
#---------------------------------------------------------#
def flip_LR():
    pia_img = Image.open('resize.png')
    pia_img.transpose(Image.FLIP_LEFT_RIGHT).save('flip_LR.png')
def flip_TB():
    pia_img = Image.open('resize.png')
    pia_img.transpose(Image.FLIP_TOP_BOTTOM).save('flip_TB.png')
flip_LR()
flip_TB()