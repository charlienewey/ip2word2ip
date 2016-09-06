Convert between IP addresses and unique phrases.

# Convert IPs to phrases

```bash
$ python2 ip2word.py --wordlist wordlist.txt "127.0.0.1" "8.8.8.8"
kuomintang.aardvark
andorran.andorran
```

# Convert phrases to IPs

```
$ python2 word2ip.py --wordlist wordlist.txt "kuomintang.aardvark" "andorran.andorran"
127.0.0.1
8.8.8.8
```
