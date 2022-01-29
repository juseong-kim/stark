import re
s = 'an2:1221.65m\r\n'
pattern = ":(.*?)m"

substring = re.search(pattern, s).group(1)
print(substring)
