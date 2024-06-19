# HTML to Markdown Converter

This Python script automates the conversion of HTML files to Markdown format. It traverses through a specified input directory, converts all HTML files to Markdown, and saves the converted files in a specified output directory.

## Dependencies

Before running the script, ensure you have the `markdownify` library installed. You can install it using pip:

```bash
pip install markdownify
```

Usage
To use this script, you need to provide two arguments:

The path to the input directory containing the HTML files.
The path to the output directory where the Markdown files will be saved.

Command Line Syntax

`python html_to_md_converter.py <input_directory> <output_directory>`

Example

Assuming you have a directory `./html_files` containing your HTML files and you want to save the Markdown files to `./markdown_files`, you would use the following command:

`python html_to_md_converter.py ./html_files ./markdown_files`

This will convert all HTML files found in ./html_files and save the corresponding Markdown files in ./markdown_files, maintaining the directory structure relative to the input directory.

Output
The script outputs the conversion status to the console, indicating the source HTML file and the destination Markdown file paths.

Converted `./html_files/example.html` to `./markdown_files/example.md`

This indicates that the HTML file example.html was successfully converted to Markdown format and saved as example.md in the output directory.

Additional Information
The script handles directory creation in the output path, so you don't need to create the output directory beforehand.
It only processes files with the .html extension and ignores all other file types in the input directory.
