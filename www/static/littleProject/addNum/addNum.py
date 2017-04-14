from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    myfront = ImageFont.truetype('C:/Windows/Fonts/Candara.ttf', size=int(width / 4))
    fillcolor = '#ff0000'
    draw.text((width-width / 4, 0), '10', font=myfront, fill=fillcolor)
    img.save('reslut.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
