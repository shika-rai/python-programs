import qrcode
def get_info():
    file=open("github.txt","r")
    x=file.read()
    return x

a=qrcode.QRCode()
text_mg=get_info()
a.add_data(text_mg)
a.make(fit=True)
res=a.make_image(fill_color="black", back_color="white")
res.save("git.png")
print("Save successfully")