from PIL import Image
import os


path = 'D:\pygit\www\static\littleProject\ChangePicture\pictureDir'
resultPath = 'D:\pygit\www\static\littleProject\ChangePicture/resultP'
if not os.path.isdir(resultPath):
    os.mkdir(resultPath)
for picName in os.listdir(path):
    picPath = os.path.join(path, picName)
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1336 if (w / 1336) >= (h / 640) else h / 640
        im.thumbnail((w / n, h / n))
        im.save(resultPath + '/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')
