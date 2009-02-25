import EXIF, PIL

f = open("evil2.gfx", "rb")
files = [open("out1.out","wb"), open("out2.out","wb"), open("out3.out","wb"), open("out4.out","wb"), open("out5.out","wb")]

i = 0
byte = True
while byte:
    byte = f.read(1)
    files[i%5].write(byte)
    i = i+1

#solution disproportional