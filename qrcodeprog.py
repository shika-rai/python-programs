import qrcode
a=qrcode.QRCode()
text_mg="hi students how are you"
a.add_data(text_mg)
a.make(fit=True)
abhijith=a.make_image(fill_color="black",back_color="white")
abhijith.save("abhyu.png")
print("saved successfullly")
