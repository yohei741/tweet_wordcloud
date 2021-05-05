# 文中の絵文字を削除するためのテスト
# https://qiita.com/yoshimo123/items/85331d881aed9ad41020

import emoji

def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI_ENGLISH)

emojis = '(｀ヘ´) 🤗⭕🤓🤔🤘🦁⭐🆗🆖🈲🤐🤗🤖🤑🆙⏩'
print(remove_emoji(emojis))

# 出力 
# '(｀ヘ´) 