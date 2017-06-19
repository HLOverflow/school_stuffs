#########################
# Author: Tay Hui Lian
# Description:  Just a simple way to overwrite original with random data
#
#########################
# Tested with Recuva.
# The final result is that Recuva will know this file as deadfile,
# record it as excellent, no overwritten cluster detected.
#
# However, as shown below, we managed to overwrite the original data with garbage random characters
#
# "This is a top secret document. This is using python file shredder"
#       became
# "cs¾…Ì¦Æ¾le6-·I.í¶Æå‹sù@fÔsˆ¬0i8œ6ÎëÞc¯ÔAG«L$ˆþU¯3Q©¹*?'á]çî³ö{pt"
#
##########################

import tkFileDialog
import Tkinter
import os
import random

# variables
PASSES = 3

# get file path
root = Tkinter.Tk()
root.withdraw()
filepath = tkFileDialog.askopenfilename()
print filepath
root.destroy()

# get size
length = os.path.getsize(filepath)
print length

# generate random strings to replace
def getReplacement(length):
    replacement = ''
    for i in range(length):
        index = random.randint(33, 254)
        replacement += chr(index)
    return replacement

# overwrite file
fo = open(filepath, "w")
for count in range(PASSES):
    data = getReplacement(length)
    fo.write(data)
    fo.seek(0)
fo.close()

os.rename(filepath, "deadfile")
os.unlink("deadfile")
print "file has been shredded"






