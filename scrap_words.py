from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import string
import re
import time
import os
import sqlite3

start_time = time.time()

with open('163.html', 'r', encoding='utf8') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
div_messages = soup.find_all('p')

# print(div_messages[:100]) - Checking data

con = sqlite3.connect('words_freq.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS WordsFreq')
cur.execute('''CREATE TABLE WordsFreq
           (ID INTEGER PRIMARY KEY, Words TEXT, Frequency INTEGER)''')

# List of stopwords using nltk
stopwords = set(stopwords.words('english'))
names = ['shubhàm', 'pằtįl', 'srijan', 'rajput', 'shubham', 'karde', 'mrinal', 'sharma', 'ankur', 'sinha', 'click', 'audio', 'video']

working = 'Working...'
n = 0
counts = dict()
for lines in div_messages:
    line = lines.get_text()
    if line is None:
        continue
    # Cleaning message line
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
        if len(word) < 4:
            continue
        # Removes emojis from word
        word = RE_EMOJI.sub(r'', word)
        counts[word] = counts.get(word, 0) + 1

    time.sleep(.1)
    print('Working!')
    time.sleep(.1)
    os.system('clear')

# Inserting data into WordsFreq Table
for word, freq in counts.items():
    cur.execute('INSERT INTO WordsFreq (Words, Frequency) Values (?,?)', (word, freq))
    con.commit()
cur.close()

print('DONE!')
end_time = time.time()
total_time = end_time - start_time
print('Total Time-Taken: '"{0:2f}".format(total_time))
