from pptx import Presentation
from create_ol import OpenLyricsSong

# Load the PresentationML file (.pptx)
prs = Presentation("Trembling and Shaking.pptx")
ol_song = OpenLyricsSong()

root = ol_song.create_openlyrics("Trembling and Shaking", "Author Name", "Trembling_and_Shaking.xml")
lyrics = root.find("lyrics")

# Loop through slides and shape elements
for i, slide in enumerate(prs.slides):
    print(f"--- Slide {i+1} ---")
    for shape in slide.shapes:
        if shape.has_text_frame:
            # for paragraph in shape.text_frame.paragraphs:
                # if paragraph.text.strip():
                #     print(paragraph.text)
            print(shape.text)
            ol_song.add_verse(lyrics, f"verse{i+1}", [shape.text])

ol_song.pretty_and_save_xml(root, "Trembling_and_Shaking.xml")