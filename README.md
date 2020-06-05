# Count-Common-News-Words
This is a small python program that parses text from the ten most recent articles from major news sites. It then logs to the console the 100 most frequent words for each news site.
Summary: 

Reads from various widely read newspapers daily, returns the 100 
most common words found from each outlet. React app currently being worked on 
to display the data in a GUI (visual) format. 


Structure: 

Parse Feeds: 

"main.py" calls "feed_scraper.py", which then reads through "feeds.txt" and grabs all
recent (that day) articles from each feed (in each line) and sends the titles, urls, 
and other details to "titles_from_today.txt", in xml format. 

Parse HTML:

"html_scraper.py" is called from "main.py", which then reads urls from "titles_from_today.py",
and parses the <p> tags from each feed for their content, popping them to an efficient
python collection, and then dumping the collection to "articles.txt".

Delete Too Common Words:

In our articles, there are many words that are not useful (the, and, because), and
I have chosen to remove these words from the articles before making word counts
in the next step.

Count the Most Common Words: 

"main.py" then calls "count_most_common.py", which uses a Counter object to keep track 
of the hundred most words from each. It returns a xml file with each newssite and their
word counts. 

Display to the Console:

"main.py" then calls "display.py" to display these to the console in a formatted way.


