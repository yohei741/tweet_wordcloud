"""
ツイートの取得
"""

import json
from requests_oauthlib import OAuth1Session
import emoji

import config # config.pyファイルを別途作成

# config.pyでの設定値を呼び出し
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) # 認証処理

#タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json" 

params = {'screen_name': 'rinascimento741',
    'exclude_replies': True,
    'include_rts': False,
    'count': 200}

# 出力先ファイル
f_out = open("./output/tweet_data", "w")

# 絵文字を除去（wordcloudでバグとなるため）
# `emoji.UNICODE_EMOJI_ENGLISH`とする必要あり
def remove_emoji(src_str):
    return "".join(c for c in src_str if c not in emoji.UNICODE_EMOJI_ENGLISH)


# コード上では、20,000(=200×100回)ツイート分取得するようになっているが、
# API仕様上、3200ツイートまでしか取得できない
# 参照：https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
for _ in range(100):

    # リクエストを投げる
    res = twitter.get(url, params=params)

    if res.status_code == 200:
        limit = res.headers["x-rate-limit-remaining"]
        print("API 残り回数: " + limit)
        if limit == 1:
            sleep(60 * 15)
        
        timelines = json.loads(res.text)
        for i in range(len(timelines)):
            if i != len(timelines) - 1:
                f_out.write(remove_emoji(timelines[i]["text"]) + "\n")
            else:
                f_out.write(remove_emoji(timelines[i]["text"]) + "\n")
                
                # 一番最後のツイートIDをパラメータmax_idに追加
                params["max_id"] = timelines[i]["id"]-1

f_out.close()
