**Binary Hash file**
Check the binary hash file with 'bvi'


Obtain the hash string in hex code from the binary file with:

hexdump -v -e '16/1 "%02X""\n"' level3.hash.bin


Generate md5 hex digests iteratively from a password list with:


for i in pos_pw_list: hashlib.md5(str.encode(i)).hexdigest()

