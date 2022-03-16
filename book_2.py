from urllib.request import urlopen

url = "https://www.gutenberg.org/cache/epub/67628/pg67628.txt"

local_name = "youth_and_life.txt"
import certifi
import ssl

def save_locally():
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)

punctuation = ",;!.?-()"
def get_unique_words():
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words

save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            unique_words[unique_word] = -1
            break

count = 0
for i in range(0, len(unique_word)):
    if(unique_word[i] != ' '):
        count = count + 1
print("Total number of characters: " + str(count))