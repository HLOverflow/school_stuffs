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

# version 2. 
import random, os
import sys

def printprogress(total, progress):
    chars = ["*", "|", "/", "-", "\\", "|", "/", "-", "\\"]
    progressbar = (progress / (total/20))*'#'
    sys.stdout.write("\r[%s] [%-20s] %3d %%" % (chars[printprogress.index],progressbar, 100*progress/total) )
    sys.stdout.flush()
    printprogress.index = (printprogress.index + 1) % len(chars)
printprogress.index=0

# generate random strings to replace
def getReplacement(length):
    replacement = ''
    progress = 0
    for i in range(length):
        index = random.randint(33, 254)
        replacement += chr(index)
        progress += 1
        printprogress(length, progress)
    print
    return replacement

def shred(filepath, passes=3):
    # get size
    length = os.path.getsize(filepath)
    print length

    # overwrite file
    fo = open(filepath, "w")
    for count in range(passes):
        print "pass number: ", count
        data = getReplacement(length)
        fo.write(data)
        fo.seek(0)
        print "pass", count, "finished"
    fo.close()

    os.rename(filepath, "deadfile")
    os.unlink("deadfile")
    print "file has been shredded"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage:", argv[0], "<filepath>", "[numofpass=3]"
        exit(0)
    if len(sys.argv) == 2:
        shred(sys.argv[1])
    else:
        shred(sys.argv[1], int(sys.argv[2]))
    print "[*] done"
