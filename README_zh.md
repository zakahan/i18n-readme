# i18n-readme
一个使用AI翻译自动生成多语言README文件的命令行工具。

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

## 安装
```bash
# 使用 uv 安装（推荐）
uv add --dev git+https://github.com/zakahan/i18n-readme.git

# 或使用 pip
pip install git+https://github.com/zakahan/i18n-readme.git
```

## 使用方法
```bash
cd /your/project/path  # 项目必须包含 README.md 文件
i18n-readme run \
  --base_lang en \  # 用于排除原始 README.md 的语言类型
  --api_key your_api_key \
  --api_model_name doubao-seed-1-6-250615 \
  --api_base_url https://ark.cn-beijing.volces.com/api/v3 \
  --lang_list zh,ja,ko
```

## 参数说明
- `--base_path`: 基础 README 文件的路径（默认：`README.md`）
- `--base_lang`: 原始 README 的基础语言（默认：`en`，支持：zh, en, ja, ko, fr, de, es, ru, ar, pt, it, hi, bn, pa, jv, id, ms）
- `--api_key`: 翻译服务的 API 密钥（如果未提供，将从 `API_KEY` 环境变量读取）
- `--api_model_name`: 要使用的 AI 模型名称（必填，如果未提供，将从 `API_MODEL_NAME` 环境变量读取）
- `--api_base_url`: API 的基础 URL（如果未提供，将从 `API_BASE_URL` 环境变量读取）
- `--lang_list`: 目标语言的逗号分隔列表（默认：`zh,en,ja,ko`）

## 支持的语言
此工具目前支持翻译成以下语言：
（实际上，这取决于您的模型支持哪些语言。因此，语言能力完全取决于模型能力。如果您认为翻译有问题，请不要责怪我，orz）
- 中文 (zh)
- 英语 (en)
- 日语 (ja)
- 韩语 (ko)
- 法语 (fr)
- 德语 (de)
- 西班牙语 (es)
- 俄语 (ru)
- 阿拉伯语 (ar)
- 葡萄牙语 (pt)
- 意大利语 (it)
- 印地语 (hi)
- 孟加拉语 (bn)
- 旁遮普语 (pa)
- 爪哇语 (jv)
- 印尼语 (id)
- 马来语 (ms)

## 输出
翻译后的文件将生成在当前目录中，格式为：`README_{lang}.md`
示例：`README_zh.md`、`README_ja.md`

## 环境变量
您可以使用环境变量而非命令行参数来配置 API 凭据：
```bash
# 设置 API 密钥
export API_KEY=your_api_key

# 设置模型名称
export API_MODEL_NAME=doubao-seed-1-6-250615

# 设置 API 基础 URL（可选）
export API_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

### 说明
当前模型调用基于 litellm 和 OpenAI API 模式，因此默认使用 OpenAI 格式进行调用。

## 后续计划
- 支持 `diff` 和 `overwrite` 模式
- 多文档文件批量处理
- 自定义翻译提示词
- 翻译质量提升

## 顺便说一下

正如您所猜测的，这些 README 当然是由本项目生成的。
（因此，如果出现任何语言翻译错误，请不要责怪我。`非我也，兵也`（这句不是它干的，我修正了一下，原文大模型翻译的啥玩意））