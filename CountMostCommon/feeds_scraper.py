import feedparser

def get_new_feeds():    

    urls = []  # these urls are what the html_scraper actually scrapes
    article_list = []
    file1 = open("feeds_to_read.txt")
    feeds = file1.readlines()

    for feed in feeds:
        #feed parser logic
        d = feedparser.parse(feed)
        i = 1
        for link in feed:
            while i < 10:
                try: 
                    url = d.entries[i].link
                    urls.append(url)
                    i+=1
                except(IndexError):
                    continue
        save_to_file(urls)        
    return urls

def save_to_file(urls):
    with open('urls_to_read.txt', 'w') as filehandle:
        for url in urls:
            filehandle.write('%s\n' % url)

get_new_feeds()
