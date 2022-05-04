
# Copyright (C), 2022, Yuqing Guo
f = open("leakage.txt", 'w')     # create output file

for i in range (0, 63):
    str1 = "%02x" % i
    str2 = "%02x" % (63-i)
    str3 = "%02x" % (i+1)
    str4 = "%02x" % (63-(i+1))

    print("{:<8}".format(45500 + 100 + i*700) + 
          "{:<3}".format(str1) +
          "{:<3}".format(str2) +
          "00 00 ffffffffffffffff 0000000000000000 0 1 0 0 0 0 1 1 0 1 0 1", file = f )
    print("{:<8}".format(45500 + 170 + i*700) + 
          "{:<3}".format(str3) +
          "{:<3}".format(str4) +
          "00 00 ffffffffffffffff 0000000000000000 1 1 0 1 1 1 1 1 0 1 1 1", file = f )


f.close()
