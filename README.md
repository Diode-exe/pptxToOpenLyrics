# PPTX to OpenLyrics

A small command-line script that extracts text from a PowerPoint presentation (`.pptx`) and writes an [OpenLyrics](https://openlyrics.org/) XML song file.

## Requirements

- Python 3.12 or newer
- A `.pptx` presentation
- The project dependency `python-pptx` (declared in `pyproject.toml`)

Install the dependency with pip:

```powershell
python -m pip install "python-pptx>=1.0.2"
```

## Usage

Run the script from the project directory:

```powershell
python main.py
```

When prompted, enter:

1. The path to the PowerPoint file
2. The song title
3. The author

For example:

```text
Filename? songs\example.pptx
Title? Example Song
Author? Songwriter Name
```

The script writes an XML file by replacing `.pptx` in the entered filename with `.xml`. For the example above, the output is `songs\example.xml`.

## What it converts

- It visits slides in presentation order and checks each shape on each slide.
- For every shape with a text frame, it prints the shape's text and adds that text to the OpenLyrics XML.
- Each text-bearing shape becomes its own `<verse>` element. Verse names use the slide number (`verse1`, `verse2`, and so on), so multiple text-bearing shapes on the same slide produce multiple verses with the same name.
- The XML includes the prompted title and author, an OpenLyrics version of `0.8`, and the extracted text.
- Extracted shape text is also appended to `lines.txt` in the current working directory. Repeated runs append more text; they do not clear this file.

## Limitations

- The script is interactive; it does not accept command-line arguments.
- It does not infer song sections such as chorus or bridge. All extracted text is added as verses.
- Only shape text is extracted; images and other non-text slide content are not converted.
- The output filename is formed by a case-sensitive replacement of `.pptx` with `.xml`. Use a lowercase `.pptx` extension to get the expected output name.
- Invalid paths or unreadable presentations are not handled by the script.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
