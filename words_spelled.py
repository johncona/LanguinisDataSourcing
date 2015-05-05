# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:54:53 2015 @author: Andrew
"""

good_name = 'good_word_dump.txt'
bad_words = 'bad_word_dump.txt'

def english_words_spelled_text(good_file,bad_file,json_data):
    good_file = open(good_file,'w')
    bad_file = open(bad_file,'w')
    for line in json_data:
        try:
            bad_words = line['properties']['words_spelled_incorrectly']
            good_words = line['properties']['words_spelled']
            good_file.write(good_words + ',\n')
            bad_file.write(bad_words + ',\n')
        except:
            pass
    good_file.close()
    bad_file.close()

def words_spelled(file_name,json_data):
    csv_file = open(file_name,'w')
    header = "user_id,language_code,good_words,bad_words\n"
    csv_file.write(header)
    for line in json_data:
        try:
            bad_words = []
            good_words = []
            distinct_id = line['properties']['distinct_id']
            bad_words.append(line['properties']['words_spelled_incorrectly'].replace(',',';'))
            good_words.append(line['properties']['words_spelled'].replace(',',';'))
            language_code = line['properties']['language_code']
            words = str(distinct_id) + "," + str(language_code) + "," + str(good_words) + "," + str(bad_words) + "\n"
            csv_file.write(words)
        except:
            pass
    csv_file.close()

def unique_words(file_name,column):
    csv_file = open(file_name,'r')
    #for i in csv_file[]:

df = pd.read_csv(csv_name,encoding='utf-16',sep=',')