# Jersey CTF

## Osint

### where-is-it
use binwalk to extract the txt file inside the image file
`binwalk -e WhereIsIt.jpg`

### beyond-the-packet
The below paragraph is found in one of the requests from the client to the
server.

Meet at the heart of Greenwich Village, we will then walk to my regular drinking
spot where my favorite musician is displayed on a door. You should listen to
Voodoo Chile, it's like one of my favorite songs by him. Oh did you know that
the Voice of a Generation as he was named during that era must've hung out
there. Seems like the place fared well after the Fourth Corporate War despite
existing way before that calamity. I read that in the city paper. Oh well I'm
just rambling. You'll see where it's at.

Put it in chatgpt to get a hint of the bars. Cafe Wha? is the answer.

## advised-on-a-novel-idea

This paper <https://ieeexplore.ieee.org/document/10057978/citations#citations>
published by Zhixin Pan and Prabhat Mishra in 2020 is the one that is mentioned
in the challenge.

The book link <https://link.springer.com/book/10.1007/978-3-031-46479-9>
Get ISBN for hardcover

From Wikipedia page on Prabhat Mishra, we know that he graduated in 2004.
Using <https://scholar.google.com/citations?user=ZlhpUZoAAAAJ&hl=fil> for his
publications, we can see that Nikhil Dutt was his advisor who published with him
in 2003 and 2004. Also <https://ics.uci.edu/~aces/people.htm> shows that Nikhil
was his advisor.

So flag is jctf{Mishra_Pan_isbn_Dutt} (replace the isbn with the actual isbn)

## Misc

### internal-tensions

Go on Wayback and see the HTML comments

### welcom-hackers

On discord, react with thumbs up on rules

### data-divergence-discover

Use diff to see the difference.
Concatenate the characters that cause spelling mistakes to get the flag.



### Augmented-&-Fragmented


### the-droid-youre-looking-for

`app-debug.apk` is an Android application that contains a flag. Your goal is to
extract the flag from the application.

To get the flag, I installed apktool

`apktool d app-debug.apk -o app-apk-output`

```bash
grep -R jctf
grep -R flagBegin
```

### lockbox

mayae has the lockbox file



## crypto

### adversary
Refer `./crypto-adveRSAry` folder scripts
get value of d using a python script `./crypto-adveRSAry/get_rsa_d.py`
put d in `./crypto-adveRSAry/decode_cipher.py` and
decrypt the message using `./crypto-adveRSAry/decode_cipher.py`

## forensics

### All-Along-the-Watchtower

binwalk to get password protected 7z file and the password wordlist
use 7ztojohn to get the hash of the protected 7z file.
Use john to crack the password and extract the files from 7z
Using hint as Base FFFF+1 which is base 65536, covert the numbers to plain text
at <https://www.better-converter.com/Encoders-Decoders/Base65536-Decode>

## bin/rev

### searching-through-vines
Just open vim
Use `:Ex` to see the files and open the flag file.
