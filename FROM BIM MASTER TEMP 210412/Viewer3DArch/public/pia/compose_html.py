from genericpath import isdir
import os

from PIL import ImageColor, Image

sampble = """
                <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
                    <a href="./animals/animal (2).jpg" data-caption="Sea side, south shore<br><em class='text-muted'>© Dominik Schröder</em>" data-width="600" data-height="900" itemprop="contentUrl">>
                        <img src="./animals/animal (2).jpg" itemprop="thumbnail" alt="Image description">
                    </a>
                </figure>"""
pattern = """
                <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
                    <a href="{0}" data-caption="Baby Play Learn Program<br><em class='text-muted'>Tran Vo Phuong Duy +84 9 327 82 327<br>duytran.arch@gmail.com</em>" data-width="{1}" data-height="{2}" itemprop="contentUrl">
                        <img src="{0}" itemprop="thumbnail" alt="Image description">
                    </a>
                </figure>"""
def read_img(file_name):
    """### Đọc thông tin ảnh
    ##### return: width, height, format, format_description"""
    im = Image.open(file_name)
    width, height = im.size
    file_name = im.filename
    format = im.format # extension
    format_description = im.format_description
    return width, height, format, format_description

if __name__ == '__main__':
    

    file = __file__#[0].upper()+__file__[1:]
    print(file)

    file_dir = file[:-len(file.split('\\')[-1])-1]
    print(file_dir)

    folders = [f"{file_dir}\{f}" for f in os.listdir(file_dir) if os.path.isdir(f"{file_dir}\{f}")]    
    [print(f) for f in folders]

    htmls = []
    for fd in folders:
        d = fd.split('\\')[-2] + '/' + fd.split('\\')[-1]
        html_text = []
        for file_name in os.listdir(fd):
            try:
                file_path = f"{fd}\\{file_name}"
                info = read_img(file_path)                
                fn = f"./{d}/{file_name}"

                w = info[0]
                h = info[1]

                if w > h:
                    h = h * 900/w
                    w = 900
                elif w == h:
                    w = 900
                    h = 900
                elif w < h:
                    w = w * 900/h
                    h = 900

                text = pattern.format(fn,w,h)
                html_text.append(text)
            except:
                pass
        htmls.append(html_text)    
        with open(f"{fd}.txt",'w') as f:
            f.write('\n'.join(html_text))

    # for h in htmls:
    #     # print('-'*50)
    #     # print('-'*50)
    #     # print('\n'.join(h))
    #     with open()

    pass