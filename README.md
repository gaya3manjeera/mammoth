# Mammoth
A python library to convert word to Markdown such as those created by Microsoft Word, Google Docs and LibreOffice, and convert them to HTML.

The following features are currently supported:

- Headings.

- Lists.

- Customisable mapping from your own docx styles to HTML. For instance, you could convert WarningHeading to h1.warning by providing an appropriate style mapping.

- Tables. **The formatting of the table itself, such as borders, is currently ignored,** but the formatting of the text is treated the same as in the rest of the document.

- Footnotes and endnotes.

- Images.

- Bold, italics, underlines, strikethrough, superscript and subscript.

- Links.

- Line breaks.

- Text boxes. The contents of the text box are treated as a separate paragraph that appears after the paragraph containing the text box.

- Comments.

# Install Mammoth
To install the Mammoth, please make sure that you have Python and PIP installed on your PC. Then, you can open CMD or Terminal and use the following command:

**$ pip install mammoth** 
