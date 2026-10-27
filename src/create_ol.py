import xml.etree.ElementTree as ET
from xml.dom import minidom


def _xml_safe_text(text):
    return "".join(
        "\n" if char == "\v" else char
        for char in text
        if char == "\v"
        or char in "\t\n\r"
        or "\x20" <= char <= "\ud7ff"
        or "\ue000" <= char <= "\ufffd"
        or "\U00010000" <= char <= "\U0010ffff"
    )


class OpenLyricsSong:
    def create_openlyrics(self, title, author):
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
        title_element.text = _xml_safe_text(title)
        
        authors = ET.SubElement(properties, "authors")
        author_element = ET.SubElement(authors, "author")
        author_element.text = _xml_safe_text(author)

        # 3. Add Lyrics Content
        lyrics = ET.SubElement(root, "lyrics")
        
        return root
        
    def add_verse(self, lyrics, verse_number, lines_text):
        # Verse 1
        verse = ET.SubElement(lyrics, "verse", {"name": verse_number})
        lines = ET.SubElement(verse, "lines")
        
        for line_text in lines_text:
            line = ET.SubElement(lines, "line")
            line.text = _xml_safe_text(line_text)

        with open("lines.txt", "a", encoding="utf-8") as f:
            for line_text in lines_text:
                f.write(line_text + "\n")

    def pretty_and_save_xml(self, root, filename):
        tree = ET.ElementTree(root)
        xml_str = ET.tostring(root, encoding="utf-8")
        parsed_str = minidom.parseString(xml_str)
        pretty_xml_as_string = parsed_str.toprettyxml(indent="  ")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pretty_xml_as_string)