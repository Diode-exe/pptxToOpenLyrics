# PPTX to OpenLyrics

Convert the text from a PowerPoint presentation into an [OpenLyrics](https://openlyrics.org/) XML song file.

The converter treats each slide as one verse. Text is collected from shapes that contain a text frame, then written to both the OpenLyrics XML output and a plain-text file.

## Requirements

- Python 3.12 or newer
- A `.pptx` presentation
- `python-pptx` 1.0.2 or newer

## Installation

Create and activate a virtual environment, then install the project dependency:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "python-pptx>=1.0.2"
```

## Usage

The current script uses fixed filenames. Place the presentation below in the project directory:

```text
Trembling and Shaking.pptx
```

Run the converter from the project directory:

```powershell
python main.py
```

The script prints the text found on each slide and creates or updates:

- `Trembling_and_Shaking.xml` - an OpenLyrics 0.8 XML file with the title, author, and one verse per slide.
- `lines.txt` - plain-text output containing the extracted shape text.

## Output structure

Each slide becomes a verse named `verse1`, `verse2`, and so on. Each text-bearing shape on a slide is currently added as one line in that verse.

The title and author are set in `main.py`:

```python
ol_song.create_openlyrics(
	"Trembling and Shaking",
	"Author Name",
	"Trembling_and_Shaking.xml",
)
```

Edit these values, along with the input filename, when converting a different presentation.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Loads the presentation and coordinates conversion. |
| `create_ol.py` | Builds OpenLyrics XML and writes extracted text. |
| `pyproject.toml` | Project metadata and dependency declaration. |
| `Trembling_and_Shaking.xml` | Example/generated OpenLyrics output. |
| `lines.txt` | Example/generated plain-text extraction. |

## Current limitations

- Input and output filenames are hardcoded; there are no command-line arguments yet.
- The author is hardcoded to `Author Name` in `main.py`.
- Each slide is always classified as a verse; chorus and bridge sections are not inferred.
- `lines.txt` is opened in append mode, so repeated runs add to the existing file.
- Missing files, malformed presentations, and other conversion errors are not handled explicitly.

## License

This project is licensed under the terms in [LICENSE](LICENSE).
