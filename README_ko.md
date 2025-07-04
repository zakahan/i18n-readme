# i18n-readme
AI 번역을 사용하여 다국어 README 파일을 자동으로 생성하는 명령줄 도구입니다.

[영어](README.md) | [중국어](README_zh.md) | [일본어](README_ja.md) | [한국어](README_ko.md)

## Installation
```bash
# Install with uv (recommended)
uv add --dev git+https://github.com/zakahan/i18n-readme.git

# Or with pip
pip install git+https://github.com/zakahan/i18n-readme.git
```

## Usage
```bash
cd /your/project/path  # 프로젝트에는 README.md 파일이 있어야 합니다
i18n-readme run \
  --base_lang en \  # 원본 README.md 언어 유형을 제외하기 위한 것입니다
  --api_key your_api_key \
  --api_model_name doubao-seed-1-6-250615 \
  --api_base_url https://ark.cn-beijing.volces.com/api/v3 \
  --lang_list zh,ja,ko
```

## 매개변수 설명
- `--base_path`: 기본 README 파일의 경로 (기본값: `README.md`)
- `--base_lang`: 원본 README의 기본 언어 (기본값: `en`, 지원: zh, en, ja, ko, fr, de, es, ru, ar, pt, it, hi, bn, pa, jv, id, ms)
- `--api_key`: 번역 서비스용 API 키 (제공되지 않으면 `API_KEY` 환경 변수에서 읽습니다)
- `--api_model_name`: 사용할 AI 모델의 이름 (필수 항목이며 제공되지 않으면 `API_MODEL_NAME` 환경 변수에서 읽습니다)
- `--api_base_url`: API의 기본 URL (제공되지 않으면 `API_BASE_URL` 환경 변수에서 읽습니다)
- `--lang_list`: 대상 언어의 쉼표로 구분된 목록 (기본값: `zh,en,ja,ko`)

## 지원되는 언어
이 도구는 현재 다음 언어로의 번역을 지원합니다: 
(실제로는 귀하의 모델이 지원하는 언어에 따라 달라집니다. 따라서 언어 기능은 모델 기능에 완전히 의존합니다. 번역에 문제가 있다고 생각하시면 저를 탓하지 마세요, orz)
- 중국어 (zh)
- 영어 (en)
- 일본어 (ja)
- 한국어 (ko)
- 프랑스어 (fr)
- 독일어 (de)
- 스페인어 (es)
- 러시아어 (ru)
- 아랍어 (ar)
- 포르투갈어 (pt)
- 이탈리아어 (it)
- 힌디어 (hi)
- 벵골어 (bn)
- 펀자브어 (pa)
- 자바네스어 (jv)
- 인도네시아어 (id)
- 말레이어 (ms)

## 출력
번역된 파일은 `README_{lang}.md` 형식으로 현재 디렉토리에 생성됩니다. 예시: `README_zh.md`, `README_ja.md`

## 환경 변수
명령줄 인수 대신 환경 변수를 사용하여 API 자격 증명을 구성할 수 있습니다:
```bash
# Set API key
export API_KEY=your_api_key

# Set model name
export API_MODEL_NAME=doubao-seed-1-6-250615

# Set API base URL (optional)
export API_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

### 사용 설명
현재 모델 호출은 litellm과 OpenAI API 모드를 기반으로 하므로 호출에 기본적으로 OpenAI 형식이 사용됩니다.

## 향후 계획
- `diff` 및 `overwrite` 모드 지원
- 여러 문서 파일의 일괄 처리
- 사용자 정의 번역 프롬프트
- 번역 품질 개선

## 한편

예상하셨듯이, 이러한 README는 물론 이 프로젝트에 의해 생성되었습니다. 
(따라서 언어 번역 오류에 대해 저를 탓하지 마세요. `非我也，兵也`)