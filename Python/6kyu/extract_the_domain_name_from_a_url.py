"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

import re 

def domain_name(url):
    ne = re.sub('http\:\/\/|https\:\/\/|\/.*|\?.*|www.|\#.*",""','',url)
    ne = ne.split(".")
    return str(ne[0])

def domain_name_pythonic_way(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("hs5jy01wrldi9zjzrmxj5.pro/"))
print(domain_name("www.xakep.ru"))