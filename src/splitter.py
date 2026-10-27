import pptx
import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import QFile # pylint: disable=E0611
from PySide6.QtUiTools import QUiLoader # pylint: disable=E0611

class Splitter:
    def __init__(self, presentation):
        self.prs = pptx.Presentation(presentation)
        ui_file = QFile("src/splitter.ui")

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.window.setWindowTitle("Slide Splitter")
        self.window.show()

    def get_slides(self):
        return self.prs.slides
    
    def get_slide_count(self):
        return len(self.prs.slides)
    
    def render_checkboxes(self):
        checkbox_src = []
        checkboxes = []
        for i, _ in enumerate(self.prs.slides):
            checkbox_src.append(f"Slide {i + 1}")
        for checkbox in checkbox_src:
            checkbox_widget = QtWidgets.QCheckBox(checkbox)
            checkboxes.append(checkbox_widget)
        return checkboxes