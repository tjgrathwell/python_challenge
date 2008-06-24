# http://www.pythonchallenge.com/pc/def/map.html

ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

import string
trans = string.maketrans(string.lowercase, string.lowercase[2:] + string.lowercase[:2])
print ciphertext.translate(trans)

# gives
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print 'map'.translate(trans)
# ocr