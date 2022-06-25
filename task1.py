def domain_name(url):
  return url.split('//')[-1].split('www.')[-1].split('.')[0]

assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("xakep.ru") == "xakep"
assert domain_name("https://www.cnet.com") == "cnet"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"

#Второй вариант решения
# def domain_name(url):
#   if url.find('www.') != -1:
#     url = url[url.find('www.') + 4 : ]
#     domain = url[: url.find('.')]
#   elif url.count("//"):
#     domain = url[url.find("//") + 2 : url.find('.')]
#   else:
#     domain = url[: url.find('.')]
#   return domain