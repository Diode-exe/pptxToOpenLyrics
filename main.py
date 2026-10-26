from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QFileDialog,
    QCheckBox,
    QMessageBox,
    QLineEdit,
)

from pptx import Presentation
from create_ol import OpenLyricsSong

class GUI:
    def __init__(self):
        self.input_filename = None
        self.title = ""
        self.author = ""
        self.blank_slide = False
        self.prs = None
        self.ol_song = None

        ui_file = QFile("main.ui")

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        if self.window is None:
            raise RuntimeError(f"Could not load main.ui: {loader.errorString()}")

        self.window.setWindowTitle("PPTX to OpenLyrics Converter")
        layout = QVBoxLayout(self.window.centralWidget())

        self.title_label = self.window.findChild(QLabel, "title_label")
        # layout.addWidget(self.title_label)
        self.title_entry = self.window.findChild(QLineEdit, "title_entry")
        # layout.addWidget(self.title_entry)

        self.author_label = self.window.findChild(QLabel, "author_label")
        # layout.addWidget(self.author_label)
        self.author_entry = self.window.findChild(QLineEdit, "author_entry")
        # layout.addWidget(self.author_entry)

        self.file_chooser_button = self.window.findChild(QPushButton, "choose_file_button")
        self.file_chooser_button.clicked.connect(self.choose_file)
        # layout.addWidget(self.file_chooser_button)

        self.blank_slide_var = self.window.findChild(QCheckBox, "blank_slide_checkbox")
        # layout.addWidget(self.blank_slide_var)

        self.submit_button = self.window.findChild(QPushButton, "start_button")
        self.submit_button.clicked.connect(self.submit)
        # layout.addWidget(self.submit_button)

        self.window.show()

    def choose_file(self):
        self.input_filename = QFileDialog.getOpenFileName(
            self.window, "Select PPTX file", "", "PPTX files (*.pptx)"
        )[0]

    def submit(self):
        if not self.input_filename:
            QMessageBox.critical(
                self.window, "No file selected", "Please choose a PPTX file first."
            )
            return

        self.title = self.title_entry.text()
        self.author = self.author_entry.text()
        self.blank_slide = self.blank_slide_var.isChecked()

        converter = Converter()
        converter.convert(self.input_filename, self.title, self.author, self.blank_slide)

        QMessageBox.information(
            self.window,
            "Conversion Complete",
            "The PPTX file has been successfully converted to OpenLyrics XML.",
        )

class Converter:
    def __init__(self):
        self.input_filename = None
        self.title = ""
        self.author = ""
        self.blank_slide = False
        self.prs = None
        self.ol_song = None
        self.root = None
        self.lyrics = None

    def convert(self, input_filename, title, author, blank_slide):
        self.input_filename = input_filename
        self.title = title
        self.author = author
        self.blank_slide = blank_slide

        self.prs = Presentation(self.input_filename)
        self.ol_song = OpenLyricsSong()

        self.root = self.ol_song.create_openlyrics(self.title, self.author)
        self.lyrics = self.root.find("lyrics")

        # Loop through slides and shape elements
        for i, slide in enumerate(self.prs.slides):
            print(f"--- Slide {i+1} ---")
            for shape in slide.shapes:
                if shape.has_text_frame:
                    # for paragraph in shape.text_frame.paragraphs:
                        # if paragraph.text.strip():
                        #     print(paragraph.text)
                    print(shape.text)
                    self.ol_song.add_verse(self.lyrics, f"verse{i+1}", [shape.text])
            if self.blank_slide:
                self.ol_song.add_verse(self.lyrics, f"verse{i+1}", [""])

        self.ol_song.pretty_and_save_xml(self.root, self.input_filename.replace(".pptx", ".xml"))
        
if __name__ == "__main__":
    app = QApplication([])
    gui = GUI()
    app.exec()