import qrcode
ID = input('enter Your ID for QRcode ? ')

img = qrcode.make(ID)
img.save("image\\"+ID+'.png')
