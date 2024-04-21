import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

#READ TXT FILE
with open('random_paragraphs.txt', 'r') as file:
    file_contents = file.read()

#Tokenize the text into words
words = nltk.word_tokenize(file_contents)

#Remove stop words and punctuation marks
filtered_words = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]


#Frequency of each word
freq_dist = FreqDist(filtered_words)
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")


#Most frequent word 
sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
most_frequent_word, frequency = sorted_freq_dist[0]
print(f"Most frequent word: {most_frequent_word}, Frequency: {frequency}")







