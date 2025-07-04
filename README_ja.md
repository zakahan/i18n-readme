# i18n-readme
AI翻訳を使用して多言語のREADMEファイルを自動生成するコマンドラインツールです。

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

## インストール
```bash
# uvでインストール（推奨）
uv add --dev git+https://github.com/zakahan/i18n-readme.git

# またはpipでインストール
pip install git+https://github.com/zakahan/i18n-readme.git
```

## 使用方法
```bash
cd /your/project/path  # プロジェクトにはREADME.mdファイルが必要です
i18n-readme run \
  --base_lang en \  # 元のREADME.mdの言語タイプを除外するためだけです
  --api_key your_api_key \
  --api_model_name doubao-seed-1-6-250615 \
  --api_base_url https://ark.cn-beijing.volces.com/api/v3 \
  --lang_list zh,ja,ko
```

## パラメータの説明
- `--base_path`: 基本READMEファイルへのパス (デフォルト: `README.md`)
- `--base_lang`: 元のREADMEの基本言語 (デフォルト: `en`, サポート言語: zh, en, ja, ko, fr, de, es, ru, ar, pt, it, hi, bn, pa, jv, id, ms)
- `--api_key`: 翻訳サービスのAPIキー (指定されていない場合は`API_KEY`環境変数から読み取ります)
- `--api_model_name`: 使用するAIモデルの名前 (必須, 指定されていない場合は`API_MODEL_NAME`環境変数から読み取ります)
- `--api_base_url`: APIのベースURL (指定されていない場合は`API_BASE_URL`環境変数から読み取ります)
- `--lang_list`: ターゲット言語のカンマ区切りリスト (デフォルト: `zh,en,ja,ko`)

## サポートされている言語
このツールは現在、次の言語への翻訳をサポートしています: 
(実際には、モデルがサポートしている言語に依存します。したがって、言語能力は完全にモデルの能力に依存します。翻訳に問題があると思われる場合は、私を責めないでください、orz)
- 中国語 (zh)
- 英語 (en)
- 日本語 (ja)
- 韓国語 (ko)
- フランス語 (fr)
- ドイツ語 (de)
- スペイン語 (es)
- ロシア語 (ru)
- アラビア語 (ar)
- ポルトガル語 (pt)
- イタリア語 (it)
- ヒンディー語 (hi)
- ベンガル語 (bn)
- パンジャブ語 (pa)
- ジャワ語 (jv)
- インドネシア語 (id)
- マレー語 (ms)

## 出力
翻訳されたファイルは、`README_{lang}.md` の形式でカレントディレクトリに生成されます
例: `README_zh.md`, `README_ja.md`

## 環境変数
コマンドライン引数の代わりに環境変数を使用してAPI認証情報を設定できます:
```bash
# APIキーを設定
export API_KEY=your_api_key

# モデル名を設定
export API_MODEL_NAME=doubao-seed-1-6-250615

# APIベースURLを設定（オプション）
export API_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

### 説明
現在のモデル呼び出しはlitellmとOpenAI APIモードに基づいているため、呼び出しにはデフォルトでOpenAI形式が使用されます。

## 今後の予定
- `diff` モードと `overwrite` モードのサポート
- 複数のドキュメントファイルのバッチ処理
- カスタム翻訳プロンプト
- 翻訳品質の向上

## ちなみに

お察しの通り、これらのREADMEはもちろんこのプロジェクトによって生成されました。 
(ですので、言語翻訳エラーがあっても私を責めないでください。`非我也，兵也` )