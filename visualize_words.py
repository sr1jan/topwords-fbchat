import sqlite3

con = sqlite3.connect('words_freq.sqlite')
cur = con.cursor()

cur.execute('SELECT Words, Frequency FROM WordsFreq')

counts = dict()
for row in cur:
    counts[row[0]] = row[1]

cur.close()

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
print("Open gword.htm in a browser to see the vizualization")
