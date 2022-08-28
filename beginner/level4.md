Transfer the binary hash into a text file:
hexdump -v -e '16/1 "%02x""\n"' level4.hash.bin > level4.hash.txt

Copy the positive password list to cycle through
pos_pw_list = ["6b3e", "989c", "4b17", "d06f", "f495", "6ea1", "44e4", "1d45", "3e1a", "b0b4", "8c65", "3276", "c496", "9d3d", "2476", "6ef4", "6b7f", "c184", "c2a8", "9708", "7bea", "9a2d", "4a22", "93ae", "826b", "9a50", "8b39", "5410", "a86c", "3760", "6426", "ec8e", "c294", "a909", "cbc6", "2e75", "f137", "9cb3", "79e7", "469f", "a9f9", "3e37", "b33e", "3f31", "4b27", "2f06", "cc2f", "d9e4", "2de7", "7328", "b4d4", "8e74", "a677", "b139", "9c74", "8ea4", "36f6", "613b", "7a7a", "5710", "838c", "44d5", "7190", "99d9", "c0a6", "b218", "3223", "477e", "38e5", "19b4", "3267", "2287", "b947", "a8d0", "fd9c", "e99c", "d8b7", "4c82", "b289", "332b", "bba5", "716d", "653e", "eb5d", "ad77", "ad3a", "3922", "7565", "947d", "928c", "2937", "823f", "f362", "79cf", "4582", "c0d0", "ed20", "d89a", "129c", "4e81"]

created findpw4.py program
