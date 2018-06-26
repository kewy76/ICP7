# Kate Williams
# 6/26/2018

from bs4 import BeautifulSoup
import urllib.request
from nltk import wordpunct_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
from nltk import ngrams

html = urllib.request.urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")  # Open the file using url
soup = BeautifulSoup(html, "html.parser")  # Read file using BeautifulSoup
html.close()  # Close the file

soup = soup.find('p')  # Find a paragraph
soup = soup.get_text()  # Get the text from the file

writeFile = open("input.txt", "w")  # Open text file so we can write to it
writeFile.write(soup + "\n")  # Write the data to the file

tokens = wordpunct_tokenize(soup)  # Tokenize the data
writeFile.write("The tokenized data is ")  # Write the tokenized data to the file
for s in tokens:
    writeFile.write(s + " ")
writeFile.write("\n")

stemmed = PorterStemmer()  # Stem the data
writeFile.write("The stemmed data is ")  # Write the stemmed data to the file
writeFile.write(str(stemmed.stem('Duck')) + " ")
writeFile.write(str(stemmed.stem('dynamic')) + " ")
writeFile.write(str(stemmed.stem('strong')) + " ")
writeFile.write(str(stemmed.stem('since')) + " ")
writeFile.write(str(stemmed.stem('version')) + " ")
writeFile.write(str(stemmed.stem('3.5')) + " ")
writeFile.write("\n")

tags = pos_tag(tokens)  # Tag the parts of speech using the tokens
writeFile.write("The tagged parts of speech are ")  # Output the tagged data
for tuple in tags:
    writeFile.write(str(tuple) + " ")
writeFile.write("\n")

lemmatizer = WordNetLemmatizer()  # Create a lemmatizer
writeFile.write("The lemmatized data is ")  # Lemmatize the data and output it
writeFile.write(lemmatizer.lemmatize("Duck") + " ")
writeFile.write(lemmatizer.lemmatize("dynamic") + " ")
writeFile.write(lemmatizer.lemmatize("strong") + " ")
writeFile.write(lemmatizer.lemmatize("since") + " ")
writeFile.write(lemmatizer.lemmatize("version") + " ")
writeFile.write(lemmatizer.lemmatize("3.5") + " ")
writeFile.write("\n")

trigrams = []
c = 2
while c < len(tokens) - 2:
    trigrams.append((tokens[c], tokens[c + 1], tokens[c + 2]))
    c += 2
writeFile.write("The trigrams are ")  # Write the trigram data to the file
writeFile.write(str(trigrams) + "\n")

writeFile.write("The NER data is ")  # Find the NER data and write it to the file
writeFile.write(str(ne_chunk(pos_tag(tokens))))
writeFile.write("\n")

writeFile.close()  # Close the file
