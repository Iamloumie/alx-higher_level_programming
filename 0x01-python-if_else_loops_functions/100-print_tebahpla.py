#!/usr/bin/python3
i = 0
for char_code in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(char_code - i)), end="")
    i = 32 if i == 0 else 0
