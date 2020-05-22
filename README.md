# topwords-fbchat

## Visualization of top words used in Facebook group chat

![alt text](https://github.com/srijansingh21/topwords-fbchat/blob/master/wordsVISUAL_FB.PNG 'Facebook group chat')

## Visualization of top words used in Instagram group chat

![alt text](https://github.com/srijansingh21/topwords-fbchat/blob/master/wordsVISUAL_IG.PNG 'Instagram group chat')

- This is my first ever python project. Also my first github repository.\*

### All you need to know about this project

I am using my own Facebook and Instagram group chat data as the data set. The plan is to visualize the top words used in the chat using python and d3.js library of javascript.

### Note

> Due to privacy issues I am not gonna provide my own data here. You can use your data to generate the same result. Remember to change the _.html_ filename in the **scrap_words.py** file. Code snippet:

```python
with open('163.html', 'r', encoding='utf8') as file:
  data = file.read()
```

> Instead of _163.html_ you have to use your own filename

### Steps

1. scrap_words.py

- Scraping and parsing data from a .html file using python beautifulsoup library
- Cleaning the data to get words used in the chat
- Storing words in a database using Sqlite3

2. visualize_words.py

- Retrieving data from the database
- Calculating highest and lowest word frequency from top 100 words
- Setting up font sizes for words according to their frequency
- Saving words - frequency in gwords.js file.

Once you have completed the above steps you would have generated the **gword.js** file using that in the **gword.htm** you could easily visualize your data.

To better understand the visualiztion part you have to understand the workings of [d3.js library](https://github.com/d3/d3/wiki)

> If you have any questions or a project suggestion, you can reach me here: `srofficialsingh@gmail.com`
