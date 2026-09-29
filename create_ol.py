import xml.etree.ElementTree as ET
from xml.dom import minidom


class OpenLyricsSong:
    def create_openlyrics(self, title, author, filename):
        # 1. Create the root element with required namespaces
        root = ET.Element("song", {
            "xmlns": "http://openlyrics.info",
            "version": "0.8",
            "createdIn": "Python OpenLyrics Generator",
            "modifiedIn": "Python OpenLyrics Generator",
            "modifiedDate": "2026-09-29T17:42:00"
        })
        tree = ET.ElementTree(root)

        # 2. Add Properties (Metadata)
        properties = ET.SubElement(root, "properties")
        
        titles = ET.SubElement(properties, "titles")
        title_element = ET.SubElement(titles, "title")
        title_element.text = title
        
        authors = ET.SubElement(properties, "authors")
        author_element = ET.SubElement(authors, "author")
        author_element.text = author

        # 3. Add Lyrics Content
        lyrics = ET.SubElement(root, "lyrics")
        
        tree._setroot(root)
        tree.write(filename, encoding="utf-8")
        
        return root
        
    def add_verse(self, lyrics, verse_number, lines_text):
        # Verse 1
        verse = ET.SubElement(lyrics, "verse", {"name": verse_number})
        lines = ET.SubElement(verse, "lines")
        
        for line_text in lines_text:
            line = ET.SubElement(lines, "line")
            line.text = line_text

        with open("lines.txt", "a", encoding="utf-8") as f:
            for line_text in lines_text:
                f.write(line_text + "\n")

    def pretty_and_save_xml(self, root, filename):
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)