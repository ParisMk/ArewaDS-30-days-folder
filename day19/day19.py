# Day 19, File handling

# Exercise: Level 1

# write a function which count number of lines and number of words in a text. All the file are in the data the folder
# 1) Read obama_speech.txt file and count number of lines and  words
# 2) Read michelle_obama_speech.txt file and count number of lines and words
# 3) Read donald_trump_speech.txt file and count number of lines and words
# 4) Read melina_trump_speech.txt file and count number of lines and words
import os
import re
import json
import pprint
import math
def count_lines(doc_path, filename):
    with open(doc_path,filename):
        lines = f.read()
        count_line =lines.splitlines()
        count_word = lines.split()
print(f"There are {len(count_line)} lines in {filename},{len(count_word)} words in {filename}")
pp =pprint.PrettyPrinter(indent=4)

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(file_path,rank_num):
    dict = {}
    final =[]
    with open(file_path) as f:
         countries = json.loads(f.read())
         for i in countries:
             for language in i["languages"]:
                 if dict.get("language"):
                     dict[language]+=1
                 else:
                     dict[language]=1
                     dict_val = sorted(dict.values(),reverse=True)
                     for i in sort_dict[:rank_num]:
                         final.append((i[1],i[0]))
                         return final
                     print(most_spoken_languages("/Users/ParisMk/projects/30days_of_python_note/data/countries_data.json",3))

                     # Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
                     def most_populated_countries(file_path,rank_num):
                         arr =[]
                         with open(file_path) as f:
                             countries = json.loads(f.read())
                             for country in countries:
                                 arr.append({"country":country["name"], "population": country["population"]})
                                 sort_dict = sorted(arr, key=lambda x: x["population"], reverse=True)
                                 return sort_dict[:rank_num]
                             print(most_populated_countries("/Users/ParisMk/projects/30day/30days_of_python_note/data/countries_data.json", 3))

# Exercise: Level 2

# Extract all incoming email addresses as a list from the email_exchange_big.txt file
def extract_email_address(doc_path):
    with open(doc_path) as f:
        lines = f.read()
        emails = set(re.findall(r"[a-z0-9/./-+_]+@[a-z0-9/./-+_]+/.[a-z]+", lines))
        with open("emails.txt", "a") as t:
            for email in emails:
                t.write(str(email))
                t.write("/n")
                pp.pprint(set(re,findall(r"[a-z0-9/./-+_]+@[a-z0-9/./-+_]+/.[a-z]+", lines)))
                return re.findall(r"[a-z0-9/./-+_]+@[a-z0-9/./-+_]+/.[a-z]+", lines)
            extract_email_address(
                "/Users/ParisMk/projects/30day/30days_of_python_note/data/email_exchanges_big.txt"
            )

# find the most words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. 
def find_most_common_words(doc_path,num):
    hash = {}
    with open(doc_path) as f:
        a = f.read()
        for i in a.split():
            if has.get(i):
                hash[i]+=1
            else:
                hash[i]=1
                sorted_hash = sorted(hash.items(), key=lambda x: x[1] ,reverse=True)
                print(find_most_common_words("example.txt",10))

# use the function,  find_most_frequent_words to find:
# a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
# b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
# c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
# d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)

# write a python application that checks similarity between two texts. 
import sys
sys.path.append('/Users/ParisMk/projects/30day/30days_of_python_note/data')
from stop_words import stop_words

def clean_text(doc_path):
    final =[]
    with open(doc_path) as f:
        a = f.read()
        data = a.split()
        for word in data:
            if word.isalpha():
                final.append(word)
                return final
            
def remove_support_words(txt):
    clean_text = clean_text(txt)
    final = []
    with open("/Users/ParisMk/projects/30day/sodays_of_python_note/data/stop_words.py") as f:
        a = f.read()
        for word in clean_text:
            if word.lower() not in stop_words:
                final.append(word)
                return final
            
def check_text_similarity(text_1,txt_1):
    txt_1_set = set(remove_support_words(txt_1))
    txt2_set = set(remove_support_words(txt_2))
    return f"The similarity of {txt_1} and {txt_2} is: {math.floor(len(txt2_set.intersection(txt_1_set))/len(txt1_set)*100)}%"

print(check_text_similarity("melina_trump_speech.txt","michelle_obama_speech.txt"))

# find the 10 most repeated words in the romeo_and_juliet.txt

#Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
# a) Count the number of lines containing python or Python
# b) Count the number lines containig JavaScript or Javascript
# c) Count the number lines containig Java and not JavaScript
