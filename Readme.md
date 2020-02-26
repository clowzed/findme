Fastly move to any section of readme
- [Installing](#installing)
- [Options](#options)
- [Runing](#runing)
- [Output example](#output-example)
# Installing

```bash
git clone https://github.com/YOungMeatBoy/findme.git

cd findme

make install
```

# Options
|shot flag|long flag| description| default|
|---------|---------|------------|--------|
|-n|--name| sets name of the user to search for| None|
|-s|--success| prints only suceeded urls| False|
|-j|--json| Save data from parsers in json file|False|
|-c|--csv| Save data from parsers in csv file|False|
|-u|--universal|Runs universal parsing for site in file `sites.txt`|False|


# Runing

``` bash
python run.py -n username --universal
```
# Output example
```bash

Running custom parsers...
[-] - https://example.com/ - username

Running universal parsers...
[-] - https://9gag.com/username - username
[+] - https://www.alik.cz/username - username
[+] - https://about.me/username - username
[-] - https://archive.org/username - username
[-] - https://audiojungle.net/username - username
[+] - https://www.avizo.cz/username - username
[-] - https://ask.fedoraproject.org/username - username
[+] - https://ask.fm/username - username
..........

```