# http://www.pythonchallenge.com/pc/return/evil.html

# image is evil1.jpg - evil2.jpg hints to look at evil2.gfx - a binary file. the implication being it's bits have been shuffled somehow.
# the dealer in the picture is making five

evil = open('evil2.gfx', 'rb').read()
outfiles = [open('evilout-'+str(n),'wb') for n in range(5)]
for i,b in enumerate(evil):
    target = outfiles[i%5]
    target.write(b)
    
# five files are jpg, png, gif, png and jpg in order. they spell out 'dis' 'pro' 'port' '???' '-ity', which I guess means 'disproportional'; something's fucked with the penultimate one