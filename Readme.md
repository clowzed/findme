# FINDER PROJECT
Navigation:  
- [I am a junior developer and want to take part in this project. What can I do for you?](#i-am-a-junior-developer-and-want-to-take-part-in-this-project-what-can-i-do-for-you)
- [How it works? Why should not I run anything?](#how-it-works-why-should-not-i-run-anything)
- [Installing](#installing)
- [Options](#options)
- [Runing](#runing)
- [Output example](#output-example)

# I am a junior developer and want to take part in this project. What can I do for you?

`Hi!`  
If you want to take part in this project you need to understand what this project is about.  
The idea was taken from the popular repository `Sherlock`.

I found out that it is very hard to take part in their project so I decided to write it by myself so any developer can easily take part in it.

&nbsp;
&nbsp;

`So what is this project about?`

Users often use the same nicknames on different sites.  
Using this project you can create a list of sites on which the user is registered.

&nbsp;
&nbsp;

`Example:`  
GitHub site - https://github.com/  
Any user Url: https://github.com/%username%  
So I can request  https://github.com/YoungMeatBoy to find me  
If response code == 200 then I am registered on this site.

&nbsp;
&nbsp;

In this project, I call such sites `Universal sites` and store them in file `sites.txt`.
When a user runs an application trying to find a nickname on this universal sites.

&nbsp;
&nbsp;

For each url: 
- create a class (`UniversalParser`) which adds name to an url (github.com/ + name = github.com/name)
- Run function `search` from this parser
- Get a dict

```python
name = "useraname"
url = "https://github.com/"
response, data = get_site_data(url + name)
return {
        'url': url,
        'nickname': name,
        'found': response == 200
        }
```
&nbsp;
&nbsp;

`But what can I do with sites where it is much harder to check if the user exists? `

`THIS IS HOW YOU CAN HELP A PROJECT`  
In this repository, you can find a folder named `custom`.  
There we store files with custom parsers for sites.  
Open file `custom_parser_pattern.py` and check information inside.  

Create your own file same as `custom_parser_patter.py`  
`Example:`
- I want to create my parser for `Github`:

```python
# ./custom/test_github_parser.py

# NOTHING WILL WORK WITHOUT IHIS IMPORT
from finder import Finder

# Name of the class is not important
# Just check that there is not a class with the same name

# THIS CLASS SHOULD BE A CHILD OF FINDER CLASS
class GitHubCustomParser(Finder):
    def __init__(self):
        self.url = 'https://github.com/'
    
    # Name of this function is important
    # and should always be `search`
    def search(self, name):
        # finder class has fuction 
        # get site data which returns 
        # response :int
        # data: str
        url = self.url + name
        response, data = self.get_site_data(url)
        
        # FIELDS NAMES ARE VERY IMPORTANT!
        return {
        'url': url,
        'nickname': name,
        'found': response == 200
        }

```
`THAT'S ALL YOU HAVE TO DO!`  
`YOU DO NOT HAVE TO RUN ANYTHING!`  
1) Just define a class with a function `search`!  
2) Place your file in folder `custom` and try to run the application!  
3) It will be automatically run in the custom parsers section.

# How it works? Why should not I run anything?

1) In file `run.py` I import all classes from all modules form `custom` folder.  
2) I create class `Finder`  
3) This class creates a list of all child classes (Your custom classes).
4) Inits them 
5) Runs them in the Thread pool and prints a result!

Read file `custom_parser_pattern.py` and create your first pull request!

# Installing

```bash
git clone https://github.com/YoungMeatBoy/findme.git

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
