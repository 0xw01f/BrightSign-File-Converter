import xml.etree.ElementTree as ET
import os
import re
from shutil import copyfile

regex = r"^(.+)\/([^\/]+)$"
mytree = ET.parse('./UNSORTED FILES/current-sync.xml')
#mytree = ET.parse('example.xml')
myroot = mytree.getroot()


def create(hashh, path):
    test_str = path
    src = find('sha1-' + hashh, './UNSORTED FILES/')
    matches = re.finditer(regex, test_str, re.MULTILINE)
    if "/" not in path:
        print('[-]:' + path)
        copyfile(src, './SORTED FILES/' + path)
    else:
        for matchNum, match in enumerate(matches, start=1):
            if not os.path.exists('./SORTED FILES/' + match.group(1)):
                os.makedirs('./SORTED FILES/' + match.group(1))
            print('[+]:' + match.group(0))
            copyfile(src, './SORTED FILES/' + match.group(1) + '/' + match.group(2))




def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

for x in myroot[1].findall('download'):
    hashh = x.find('hash').text
    name =x.find('name').text
    link = x.find('link').text

    create(hashh, name)

print('[!] Completed.')