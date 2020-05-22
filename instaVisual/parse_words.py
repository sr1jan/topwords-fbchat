from nltk.corpus import stopwords
import string
import re

sent = []
with open('sent.txt', 'r') as fp:
    data = fp.readlines()
    for line in data:
        sent.append(line.strip())

stopwords = set(stopwords.words('english'))
names = ['shubhàm', 'pằtįl', 'srijan', 'rajput', 'shubham', 'karde', 'mrinal', 'sharma', 'ankur', 'sinha', 'click', 'audio', 'video', 'kidher', 'udhar', 'chahiye', 'idhar']

counts = dict()
for line in sent:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', '1234567890'))
    line = line.lower()
    line = line.strip()

    words = line.split()
    # Stripping emojis from words
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    for word in words:
        if word in stopwords or word in names:
            continue
        if len(word) < 5 or len(word) > 10:
            continue
        # Removes emojis from word
        word = RE_EMOJI.sub(r'', word)

        if len(word) < 5 or len(word) > 10: continue
        counts[word] = counts.get(word, 0) + 1

c = list()
x = sorted(counts, key=counts.get, reverse=True)
for k in x[:100]:
    c.append(counts[k])
highest = max(c)
lowest = min(c)
print('Range of counts:', highest, lowest)

# Spread the font sizes across 20-80 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js', 'w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first:
        fhand.write(",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '" + k + "', size: " + str(size) + "}")
fhand.write("\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.html in a browser to see the vizualization")
