import argparse
import asyncio
import os
from i18n_readme.agent import run_agent


def main():
    parser = argparse.ArgumentParser(description="i18n-readme command line tool.")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Subcommands"
    )

    # Run command
    run_parser = subparsers.add_parser("run", help="Run the translation process")
    run_parser.add_argument(
        "--base_lang", default="en", help="Base language of the README (default: en)"
    )
    run_parser.add_argument("--api_key", help="API key for translation service")
    run_parser.add_argument("--api_model_name", help="Model name for translation API")
    run_parser.add_argument("--api_base_url", help="Base URL for translation API")
    run_parser.add_argument(
        "--lang_list",
        default="zh,en,ja,ko",
        help="Comma-separated list of target languages (default: zh,en,ja,ko)",
    )
    run_parser.add_argument(
        "--base_path",
        default="README.md",
        help="Path to the base README file (default: README.md)",
    )

    args = parser.parse_args()

    if args.command == "run":
        execute_translation(args)


def execute_translation(args):
    # Set environment variables for agent.py
    if args.api_key:
        os.environ["API_KEY"] = args.api_key
    if args.api_model_name:
        os.environ["API_MODEL_NAME"] = args.api_model_name
    if args.api_base_url:
        os.environ["API_BASE_URL"] = args.api_base_url

    if os.environ["API_BASE_URL"] is None:
        raise ValueError("API_BASE_URL is not set")

    # Read source content
    with open(args.base_path, "r", encoding="utf-8") as f:
        source_content = f.read()

    # Parse target languages
    # Define supported languages and validate
    SUPPORTED_LANGUAGES = {
        "zh",
        "en",
        "ja",
        "ko",
        "fr",
        "de",
        "es",
        "ru",
        "ar",
        "pt",
        "it",
        "hi",
        "bn",
        "pa",
        "jv",
        "id",
        "ms",
    }
    target_languages = [
        lang.strip().lower() for lang in args.lang_list.split(",") if lang.strip()
    ]

    for lang in target_languages:
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported language: {lang}. Supported languages are: {', '.join(SUPPORTED_LANGUAGES)}"
            )

    # Translate and write files
    # Process each target language, skipping base language
    base_lang_lower = args.base_lang.lower()
    for lang in target_languages:
        if lang == base_lang_lower:
            print(f"Skipping base language {lang}...")
            continue

        print(f"Translating to {lang}...")
        translated_content = asyncio.run(
            run_agent(target_language=lang, source_content=source_content)
        )
        output_path = f"README_{lang}.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)
        print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
