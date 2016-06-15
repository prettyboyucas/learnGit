# -*- coding: utf-8 -*-

#from PIL import Image, ImageFont
'''
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))

#if __name__ == '__main__':

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
'''
from Tkinter import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLable = Label(self, text='Hello, world!')
        self.helloLable.pack()
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()
app = Application()

app.master.title('Hello world')
app.mainloop()