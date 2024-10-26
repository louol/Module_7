
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                words =[]
                a =  [',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    line = line.lower()

                    lines = line.replace(',', '').replace('.', '').replace('=', '').replace('!',  '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', '')
                    words += lines.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            index = words.index(word)
            result[file_name] = index + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


