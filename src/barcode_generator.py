"Code128 generator for testing scanners"

# Global imports
import sys
import os
import datetime
import logging
import configparser

# Libray imports
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot, QTimer, SIGNAL
from PySide2.QtGui import QPixmap
import code128
import PIL

# Local imports
from bc_generator_qt_design import Ui_MainWindow


# ------------------------------------------------------------------------------
def get_version(filename="buildinfo.txt") -> str:
    """Get version information from buildinfo.txt file

    :param filename: The file to inspect
    :returns: String with version number
    """

    config = configparser.ConfigParser()
    config.read(filename)
    version = config["DEFAULT"]["version"]
    return version


# ------------------------------------------------------------------------------
def generate_barcode(counter=0):
    """Generate the barcode, which shows a running counter and the current time.

    :param counter: sequence number to embed in the barcode
    :returns: tuple of
    * the incremented counter,
    * the data to display and
    * the filename of the saved barcode
    """

    now = datetime.datetime.now()
    timestr = now.strftime("%H:%M:%S.%f")
    data_to_display = "#%05d %s" % (counter, timestr)
    counter += 1
    # print(f"{data_to_display=}")

    pil_image = code128.image(data_to_display)

    # Resize the image to maximum 640x120
    maxsize = (640, 120)
    pil_image.thumbnail(maxsize, PIL.Image.ANTIALIAS)

    filename = 'generated_barcode.jpg'
    pil_image.save(filename)
    # qt_image = ImageQt.ImageQt(pil_image)      # Make it an QT image
    # pix = QPixmap.fromImage(qt_image)

    return counter, data_to_display, filename


# -----------------------------------------------------------------------------
class MainWindow(QMainWindow):
    """Main QT window
    """

    def __init__(self):
        """Intialize the main window and parameters
        """
        super(MainWindow, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        # Set the values of the input windows
        self.set_ui_properties()

        self.counter = 0
        self.looping = False
        self.delay = 1000

        self.gui.pushButtonStartLoop.clicked.connect(self.start_stop_generator)
        self.gui.pushButtonExit.clicked.connect(self.quit_app)

        self.generate_timer = QTimer(self)
        self.connect(self.generate_timer, SIGNAL("timeout()"), self.generate_and_show_barcode)

    # -----------------------------------------------------------------------------
    # @dumpFuncname
    def get_ui_properties(self):
        """Get the values from the UI textfields, checkboxes and radiobuttons.
        """

        try:
            self.delay = int(self.gui.lineEdit_IterationDelay.text())
        except ValueError:
            self.delay = 1000   # Fall back to a standard 1 second delay

    # -----------------------------------------------------------------------------
    # @dumpFuncname
    def set_ui_properties(self) -> bool:
        """Set the values from the UI textfields, checkboxes and radiobuttons

        At this moment, it only sets the window title, including verison number
        """

        try:
            # Main window properties
            version = get_version()
            self.setWindowTitle(f"Auto Code128 Generator for testing scanners - V {version}")
        except ValueError as exept_str:
            # debug(e)
            print(exept_str)
            return False
        return True

    # -----------------------------------------------------------------------------
    @Slot()
    def start_stop_generator(self):
        """Start or stop the barcode generator

        It will make use of a timer with a user configurable delay (default 1000 ms)
        Each time the timer expires, a new barcode will be generated and displayed
        """

        self.get_ui_properties()

        if not self.looping:
            # print("Starting barcode generator")
            self.gui.pushButtonStartLoop.setText("Stop")
            self.looping = True
            self.generate_timer.start(self.delay)
        else:
            # print("Stop barcode generator")
            self.gui.pushButtonStartLoop.setText("Start")
            self.looping = False
            self.generate_timer.stop()
            return

    # -----------------------------------------------------------------------------
    @Slot()
    def generate_and_show_barcode(self) -> None:
        """This function is called when the generation timer expires.

        It will generate a barcode with the current counter, and the current date and time.
        The it will display it in the lable, and show the contents in a text window.

        :returns: Nothing
        """

        # print("Timer fired")
        self.counter, data, filename = generate_barcode(self.counter)
        pixmap = QPixmap(filename)
        self.gui.label_imageviewer.setPixmap(pixmap)
        self.gui.lineEditData.setText(data)

    # -----------------------------------------------------------------------------
    @Slot()
    def quit_app(self):
        """Quit this application.
        At this moment, it will use sys.exit()
        """

        # Enter here actions to perform before actually quitting.

        sys.exit(0)


# -----------------------------------------------------------------------------
def main():
    """The main function.
    """

    # clear_debug_window()

    # -----------------------------------
    # Logging setup
    # -----------------------------------
    if not os.path.isdir("log"):
        os.mkdir("log")
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(message)s", filename="log/bcgenerator.log",
        filemode="w"
    )

    # define a Handler which writes ERROR messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)         # Was logging.ERROR
    logging.getLogger("").addHandler(console)  # add the handler to the root logger

    # Start the main GUI
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
