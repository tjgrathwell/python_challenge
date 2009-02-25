message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
message2 = ""

import string

for char in message:
  if char in string.lowercase:
      new = chr((ord(char)+2))
      if ord('Z') < ord(new) < ord('a') or ord(new) > ord('z'):
        new = chr(ord(new) - 26)
      message2 = message2 + new
  else: message2 = message2 + char
  
print message2