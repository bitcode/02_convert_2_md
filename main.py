import argparse
from markdownify import markdownify as md
import os

def convert_html_to_markdown(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_directory, file.replace('.html', '.md'))
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                with open(file_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()
                    markdown_content = md(html_content, heading_style="ATX")

                with open(output_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(markdown_content)
                print(f"Converted {file_path} to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML files to Markdown.")
    parser.add_argument("input_directory", type=str, help="Input directory containing HTML files")
    parser.add_argument("output_directory", type=str, help="Output directory for converted Markdown files")
    args = parser.parse_args()

    convert_html_to_markdown(args.input_directory, args.output_directory)
