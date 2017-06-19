################################
# Author: Tay Hui Lian
# Description:
# this program will compute hashes with the 4 common hashes you see online for file integrity
#
# more hashes can be added by modifying "select hash type section"
# refer to hashlib regarding available hashes
# 
########### Usage #############
#
# D:\scripts>python checkHash.py
#
# Available hash options
# 1. md5
# 2. sha1
# 3. sha256
# 4. quit
# option: 1
# C:/Users/LENOVO/Downloads/python-2.7.13.amd64.msi md5 268fd335aad649df7474adb13b6cf394

import Tkinter
import tkFileDialog
import hashlib

# get file path
root = Tkinter.Tk()
root.withdraw()
filepath = tkFileDialog.askopenfilename()
root.destroy()

# extract data
fo = open(filepath, "rb")
data = fo.read()
fo.close()

# select hash type
print '''
Available hash options
1. md5
2. sha1
3. sha256
4. quit'''
option = raw_input("option: ")

try:
    opt = int(option)
except:
    print "This crashed because you didn't key in numbers"
    exit(1)

if (opt == 1):
    m = hashlib.md5()
elif (opt == 2):
    m = hashlib.sha1()
elif (opt == 3):
    m = hashlib.sha256()
elif (opt == 4):
    print "quitting the program"
    exit(0)
else:
    print "invalid option"
    exit(0)

m.update(data)
h = m.hexdigest()
print "%s %s %s" % (filepath, m.name, h)
