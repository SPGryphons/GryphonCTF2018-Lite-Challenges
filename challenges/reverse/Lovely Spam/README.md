# Lovely Spam

## Question Text

I discovered this masterpiece recently, wanted to share it with you guys. 

*Creator - PotatoDrug*

## Distribution
- lovelyspam.pyc `545fc657dff777d84e40b07c8892746b`

## Solution
Use uncompyle2 to decompile the pyc file `uncompyle2 545fc657dff777d84e40b07c8892746b.pyc > source.py`. After decompiling we see the getFlag function which needs the correct seed.

```python
def getFlag(key):
    random.seed(key)
    dontskip = {20, 34, 53, 78, 109, 114, 
    166, 279, 297, 383, 389, 401, 413, 438, 
    444, 447, 466, 514, 525, 549, 560, 569, 
    574, 611, 644, 653, 725, 726, 769, 804}
    charset = 'abcdefghijklmnopqrstuvwxyz_'
    flag = 'GCTF{'
    for i in range(805):
        if i in dontskip:
            flag += charset[random.randint(0,26)]
        else:
            random.randint(0,26)
    flag += '}'
    print flag
```

If we wait for the script to finish running or just execute the last line

`exec('7072696e742027353337303631366432303639373332303734363836353230366236353739272e6465636f646528276865782729'.decode('hex'))`

It will print out `Spam is the key`. If we modify the source code and call getFlag with 'Spam', it will print out the flag.

```python
def main():
	getFlag('Spam')
```

### Flag

`GCTF{lovely_wonderful_spammy_python}`