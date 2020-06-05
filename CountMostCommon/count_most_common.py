# Python program to find the k most frequent words 
# from data set 
from collections import Counter, Counter 

def count_most_common():

    file1 = open("articles.txt")  
    articles = file1.read()
    articles = articles.split()
    
    articles_temp = subtract_common_words(articles)
    articles_temp = Counter(articles_temp)
    most_occuring = articles_temp.most_common(100) 
    
    return(most_occuring) 

def subtract_common_words(articles):

    file2 = open("words_to_ignore.txt")
    words_to_ignore = file2.read()
    words_to_ignore_temp = words_to_ignore.split()
    words_to_ignore_temp = Counter(words_to_ignore_temp)
    
    # subtracting common words
    articles_temp = []
    for word in articles:
        if word.isalpha() == False:
            word_temp = [letter for letter in word if letter.isalpha()]
            word = ''.join(word_temp)
        if word.lower() not in words_to_ignore.lower():
            # print(word)
            # O(1) time with a list as it is only enqueing
            articles_temp.append(word)
    return articles_temp

print(count_most_common())
