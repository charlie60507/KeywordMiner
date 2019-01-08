import codecs
import jieba
import jieba.analyse

# configs
PUNCTUATION_FILE_PATH = "punctuation.txt"
STOP_WORD_FILE_PATH = "stopword_chinese.txt"
ARTICLES_FILE_PATH = "news_files.txt"
CLEAN_ARTICLES_FILE_PATH = "news_files_clean.txt"
KEYWORD_FILE_PATH = "top_keywords.txt"

def loadFile(file_name):
    f = codecs.open(file_name, 'r', encoding='utf-8-sig')
    read_file = f.read()
    f.close()
    return read_file


def removeWords(article, stopword_list):
    article_replace = article
    for item in stopword_list:
        print("Processing ", item, "...")
        article_replace = article_replace.replace(item, "")
    return article_replace


def getTopKeyWords(article):
    terms = jieba.analyse.extract_tags(
        article, topK=20, withWeight=True, allowPOS=())
    return terms


# load files
punctuation = loadFile(PUNCTUATION_FILE_PATH)
stopword = loadFile(STOP_WORD_FILE_PATH)
articles = loadFile(ARTICLES_FILE_PATH)

# preprocessing
punctuationList = punctuation.split('\r\n')
punctuationList.pop(punctuationList.index(''))
stopwordList = stopword.split('\r\n')
stopwordList.pop(stopwordList.index(''))
removeList = punctuationList + stopwordList
cleanArticles = removeWords(articles, removeList)

# get top key words
terms = getTopKeyWords(cleanArticles)

# output files
textFile = open(CLEAN_ARTICLES_FILE_PATH, "w")
textFile.write(cleanArticles)
textFile.close()

keywordsFile = open(KEYWORD_FILE_PATH, "w")
for item in terms:
    print(item[0], str(item[1]))
    keywordsFile.write(item[0] + " " + str(item[1])+'\n')

keywordsFile.close()