#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.


#https://automatetheboringstuff.com/2e/chapter12/
#Duy+An+Co.Ltd.+1006+Lê+Văn+Lương+Ấp+3+Phước+Kiển+Nhà+Bè+Tp+HCM/@10.7097617,106.7030966,16.85z
#1006 le van luong to 8 ap 3 xa phuoc kien huyen nha be tp hcm

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste() # PAST trong CMD se kích hoạt

webbrowser.open('https://www.google.com/maps/place/' + address)