# Dependencies: textblob
# Usage: python main.py filename

from textblob import TextBlob
import json
import sys
import os

file = open(sys.argv[1], "r")
text = file.read()

unicode_content = text.decode('utf-8')
xml_content = unicode_content.encode('ascii', 'xmlcharrefreplace')

blob = TextBlob(xml_content)

tags_words = {}

for word, tag in blob.tags:
	if (tag in tags_words.keys()):
		tags_words[tag].append(word)
	else:
		tags_words[tag] = []
		tags_words[tag].append(word)


with open('tags_words.js', 'w') as outfile:
    data = json.dumps(tags_words)
    outfile.write("var tags_words = " + data)

print("New file: "+os.getcwd()+"/tags_words.js")