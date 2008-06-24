# http://www.pythonchallenge.com/pc/def/oxygen.html

# oxygen.png is here, with some fun gray squares that obviously encode some neat text. gotta PIL it
# band starts (from image inspection) around y=45 and has chunks 7 pixels wide. ends at 609

import Image
im = Image.open("oxygen.png")
sampler = 1
samples = []
while sampler < 609:
    samples.append(chr(im.getpixel((sampler,45))[0]))
    sampler += 7
    
print ''.join(samples), len(samples)
    
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
clue = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(c) for c in clue])

# integrity