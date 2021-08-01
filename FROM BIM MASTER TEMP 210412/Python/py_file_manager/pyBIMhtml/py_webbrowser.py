import webbrowser

path = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\html\base.html"
# webbrowser.get("google-chrome").open(path)
# webbrowser.get("firefox").open(path)
# webbrowser.open('http://google.com')

url = "file:///"+ path
webbrowser.open(url,new=2)