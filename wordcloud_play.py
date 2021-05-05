"""
取得したツイートをWordCloudで可視化
"""

import csv
import MeCab
from wordcloud import WordCloud

# 参照：https://qiita.com/berry-clione/items/b3a537962c84244a2a09
dicdir = '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
tagger = MeCab.Tagger(dicdir)

with open("./output/tweet_data", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    texts = []
    for row in reader:
        texts.append(row)

# 4パターンのWordCloudを作成
patterns = [[["名詞","動詞","形容詞"],"all"], [["名詞"],"noun"], 
    [["動詞"],"verb"], [["形容詞"],"adjective"]]

# 形態素解析（Mecab） -> WordCloud 処理
for pattern in patterns:
    words = []
    for text in texts:
        text = " ".join(text)
        text = text.split("http")[0] # http 以降はトリ（URLは最後に載せるパターンが多いため）
        node = tagger.parseToNode(text)
        while node:
            if node.feature.split(",")[0] in pattern[0]:
                words.append(node.feature.split(",")[6]) # 原形の語句を取得
            node = node.next

    FONT_PATH = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
    STOPWORDS = ['ある', 'いい', 'いる', '思う', 'くる', 'くれる', 'こと', 'これ',
        'さん', 'する', 'せる', 'そう', 'てる', 'ない', 'なる', 'の',
        'みたい', 'やる', 'よい', 'よう', 'られる', 'れる', 'ん',
        "メモ", "的", "さ", "ため", "何", "方", "とき","もの", "感", "ここ",
        "あと", "ところ","気", "化", "やすい", "人", "いま", "こちら"]

    wordcloud = WordCloud(background_color='white', font_path=FONT_PATH,
        stopwords=STOPWORDS, width=900, height=500)
    wordcloud.generate(' '.join(words))
    wordcloud.to_file(f'./output/wordcloud_{pattern[1]}.png')
