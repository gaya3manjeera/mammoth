import mammoth
import os

def convert_docx_to_markdown(docx_path, markdown_path):
    # Convert DOCX to Markdown using Mammoth
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
        markdown_content = result.value  # The generated markdown

    with open(markdown_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
    print(f"Converted {docx_path} to {markdown_path}.")

def main(docx_path):
    output_dir = "/content/mammothoutput"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
  
    markdown_path = os.path.join(output_dir, "output.md")
    
    convert_docx_to_markdown(docx_path, markdown_path)    

if __name__ == "__main__":
    docx_path = "/content/sample.docx"  # Replace with the path to your DOCX file
    main(docx_path)
