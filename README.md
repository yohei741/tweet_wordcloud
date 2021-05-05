# tweet_wordcloud
Twitter APIを使用して、自身のTweetを収集し、WordCloudを作成する

## Output
![wordcloud_all](https://user-images.githubusercontent.com/43127213/117116802-c6300680-adc9-11eb-8296-b84dc9c6a894.png)

## Notices

- `getTimelines.py`で自身のツイートを取得
  - Twitter APIを利用するためのAPI KeyやAccess Tokenは、config.pyに格納（GitHubには上げていない）
  - 絵文字があるとWordCloudがうまく動作しない(らしい)ので除去
    - `emoji_test.py`でテスト
  - Twitter APIの仕様上、直近3200ツイートまでしか取得できない
    - [詳細はこちら](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline)
- `wordcloud_play.py`で取得したツイートをWordCloudで可視化
  - 形態素解析には`Mecab（ + neologd ）`を使用
  - ストップワードは、良い感じにアウトプットされるよう調整済み
  - WordCloudの可視化は、以下４パターンを出力できるようにfor文
    - 名詞のみ
    - 動詞のみ
    - 形容詞のみ
    - 上記３つすべて
    
## Reference
- [【Qiita】Word Cloudでツイートを可視化してみた(python)](https://qiita.com/turmericN/items/04cd0b40f91076f0ef42)  
- [WordCloudによるツイートの可視化](https://tech.unifa-e.com/entry/2021/03/11/082632)

