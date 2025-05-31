"""button.py

Button App using PySide6 & QtWidgets

:author:	Sackey Ezekiel Etrue (djoezeke)
:created:	2025.02.11
"""

# imports
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Create the application instance
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("My QT Button")
window.setGeometry(100, 100, 400, 300)

# Create a button and set its properties
button = QPushButton(window)
button.setText("press Me")
button.setGeometry(100, 100, 200, 50)
button.setStyleSheet("background-color: red; color: white; font-size: 20px;")

if __name__ == "__main__":
    # Show the main window
    window.show()
    app.exec()
