import os
from pyfiglet import Figlet

f = Figlet(font='slant')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


class displayDirs():

    def print(self, path):
        self.path = path
        try:
            self.dirs = os.listdir(path=self.path)
        except Exception as e:
            print(f"Exception: {e}")

        for self.dir in self.dirs:
            if os.path.isdir(f"{self.path}{self.dir}"):
                print(bcolors.HEADER + f"{self.path}{self.dir}\\")
            else:
                print(bcolors.HEADER + f"{self.path}{self.dir}")

    def printSupportedFiles(self, path):
        self.path = path
        try:
            self.dirs = os.listdir(path=self.path)
        except Exception as e:
            print(f"Exception: {e}")

        for self.dir in self.dirs:
            # Audio files
            if self.dir.endswith(".aif"):
                print(bcolors.HEADER + f"AIF audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cda"):
                print(bcolors.HEADER + f"CD audio track file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mid"):
                print(bcolors.HEADER + f"MIDI audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".midi"):
                print(bcolors.HEADER + f"MIDI audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mp3"):
                print(bcolors.HEADER + f"MP3 audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mpa"):
                print(bcolors.HEADER + f"MPEG-2 audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ogg"):
                print(bcolors.HEADER + f"Ogg Vorbis audio file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wav"):
                print(bcolors.HEADER + f"WAV file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wma"):
                print(bcolors.HEADER + f"WMA audio file :{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wpl"):
                print(bcolors.HEADER + f"Windows Media Player playlist:{bcolors.OKBLUE} {self.dir}")

            # Compressed files
            elif self.dir.endswith(".7z"):
                print(bcolors.HEADER + f"7-Zip compressed file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".arj"):
                print(bcolors.HEADER + f"ARJ compressed file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".deb"):
                print(bcolors.HEADER + f"Debian software package file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pkg"):
                print(bcolors.HEADER + f"Package file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".rar"):
                print(bcolors.HEADER + f"RAR file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".rpm"):
                print(bcolors.HEADER + f"Red Hat Package Manager:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tar.gz"):
                print(bcolors.HEADER + f"Tarball compressed file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".z"):
                print(bcolors.HEADER + f"Z compressed file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".zip"):
                print(bcolors.HEADER + f"Zip compressed file:{bcolors.OKBLUE} {self.dir}")

            # Disc and media files
            elif self.dir.endswith(".bin"):
                print(bcolors.HEADER + f"Binary disc image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".dmg"):
                print(bcolors.HEADER + f"macOS X disk image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".iso"):
                print(bcolors.HEADER + f"ISO disc image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".toast"):
                print(bcolors.HEADER + f"Toast disc image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".vcd"):
                print(bcolors.HEADER + f"Virtual CD:{bcolors.OKBLUE} {self.dir}")

            # Data and database files
            elif self.dir.endswith(".csv"):
                print(bcolors.HEADER + f"Comma separated value file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".dat"):
                print(bcolors.HEADER + f"Data file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".db"):
                print(bcolors.HEADER + f"Database file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".dbf"):
                print(bcolors.HEADER + f"Database file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".log"):
                print(bcolors.HEADER + f"Log file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mdb"):
                print(bcolors.HEADER + f"Microsoft Access database file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".sav"):
                print(bcolors.HEADER + f"Save file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".sql"):
                print(bcolors.HEADER + f"SQL database file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tar"):
                print(bcolors.HEADER + f"Linux / Unix tarball file archive:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".xml"):
                print(bcolors.HEADER + f"XML file:{bcolors.OKBLUE} {self.dir}")

            # Email File extensions
            elif self.dir.endswith(".email"):
                print(bcolors.HEADER + f"Outlook Express e-mail message file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".eml"):
                print(bcolors.HEADER + f"E-mail message file from multiple e-mail clients, including Gmail:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".emlx"):
                print(bcolors.HEADER + f"Apple Mail e-mail file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".msg"):
                print(bcolors.HEADER + f"Microsoft Outlook e-mail message file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".oft"):
                print(bcolors.HEADER + f"Microsoft Outlook e-mail template file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ost"):
                print(bcolors.HEADER + f"Microsoft Outlook offline e-mail storage file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pst"):
                print(bcolors.HEADER + f"Microsoft Outlook e-mail storage file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".vcf"):
                print(bcolors.HEADER + f"E-mail contact file:{bcolors.OKBLUE} {self.dir}")

            # Executable file extensions
            elif self.dir.endswith(".apk"):
                print(bcolors.HEADER + f"Android package file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".bat"):
                print(bcolors.HEADER + f"Batch file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cgi"):
                print(bcolors.HEADER + f"Perl script file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".com"):
                print(bcolors.HEADER + f"MS-DOS command file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".exe"):
                print(bcolors.HEADER + f"Executable file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".gadget"):
                print(bcolors.HEADER + f"Windows gadget:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".jar"):
                print(bcolors.HEADER + f"Java Archive file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pl"):
                print(bcolors.HEADER + f"Perl script file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".msi"):
                print(bcolors.HEADER + f"Windows installer package:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".py"):
                print(bcolors.HEADER + f"Python file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wsf"):
                print(bcolors.HEADER + f"Windows Script File:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".bin"):
                print(bcolors.HEADER + f"Binary file:{bcolors.OKBLUE} {self.dir}")

            # Font file extensions
            elif self.dir.endswith(".fnt"):
                print(bcolors.HEADER + f"Windows font file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".fon"):
                print(bcolors.HEADER + f"Generic font file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".otf"):
                print(bcolors.HEADER + f"Open type font file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ttf"):
                print(bcolors.HEADER + f"TrueType font file:{bcolors.OKBLUE} {self.dir}")

            # Image file extensions
            elif self.dir.endswith(".ai"):
                print(bcolors.HEADER + f"Adobe Illustrator file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".bmp"):
                print(bcolors.HEADER + f"Bitmap image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".gif"):
                print(bcolors.HEADER + f"GIF image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ico"):
                print(bcolors.HEADER + f"Icon file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".jpeg"):
                print(bcolors.HEADER + f"JPEG image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".jpg"):
                print(bcolors.HEADER + f"JPEG image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".png"):
                print(bcolors.HEADER + f"PNG image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ps"):
                print(bcolors.HEADER + f"PostScript file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".psd"):
                print(bcolors.HEADER + f"PSD image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".svg"):
                print(bcolors.HEADER + f"Scalable Vector Graphics file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tif"):
                print(bcolors.HEADER + f"TIFF image:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tiff"):
                print(bcolors.HEADER + f"TIFF image:{bcolors.OKBLUE} {self.dir}")

            # Internet file extensions
            elif self.dir.endswith(".asp"):
                print(bcolors.HEADER + f"Active Server Page file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".aspx"):
                print(bcolors.HEADER + f"Active Server Page file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cer"):
                print(bcolors.HEADER + f"Internet security certificate:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cfm"):
                print(bcolors.HEADER + f"ColdFusion Markup file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cgi"):
                print(bcolors.HEADER + f"Perl script file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pl"):
                print(bcolors.HEADER + f"Perl script file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".css"):
                print(bcolors.HEADER + f"Cascading Style Sheet file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".htm"):
                print(bcolors.HEADER + f"HTML file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".html"):
                print(bcolors.HEADER + f"HTML file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".js"):
                print(bcolors.HEADER + f"JavaScript file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".jsp"):
                print(bcolors.HEADER + f"Java Server Page file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".part"):
                print(bcolors.HEADER + f"Partially downloaded file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".php"):
                print(bcolors.HEADER + f"PHP file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".py"):
                print(bcolors.HEADER + f"Python file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".rss"):
                print(bcolors.HEADER + f"RSS file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".xhtml"):
                print(bcolors.HEADER + f"XHTML file:{bcolors.OKBLUE} {self.dir}")

            # Presentation file extensions
            elif self.dir.endswith(".key"):
                print(bcolors.HEADER + f"Keynote presentation:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".odp"):
                print(bcolors.HEADER + f"OpenOffice Impress presentation file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pps"):
                print(bcolors.HEADER + f"PowerPoint slide show:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ppt"):
                print(bcolors.HEADER + f"PowerPoint presentation:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pptx"):
                print(bcolors.HEADER + f"PowerPoint Open XML presentation:{bcolors.OKBLUE} {self.dir}")

            # Programming file extensions
            elif self.dir.endswith(".c"):
                print(bcolors.HEADER + f"C and C++ source code file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".class"):
                print(bcolors.HEADER + f"Java class file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cpp"):
                print(bcolors.HEADER + f"C++ source code file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cs"):
                print(bcolors.HEADER + f"Visual C# source code file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".h"):
                print(bcolors.HEADER + f"C, C++, and Objective-C header file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".java"):
                print(bcolors.HEADER + f"Java Source code file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pl"):
                print(bcolors.HEADER + f"Perl script file.:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".sh"):
                print(bcolors.HEADER + f"Bash shell script:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".swift"):
                print(bcolors.HEADER + f"Swift source code file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".vb"):
                print(bcolors.HEADER + f"Visual Basic file:{bcolors.OKBLUE} {self.dir}")

            # Spreadsheet file formats
            elif self.dir.endswith(".ods"):
                print(bcolors.HEADER + f"OpenOffice Calc spreadsheet file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".xls"):
                print(bcolors.HEADER + f"Microsoft Excel file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".xlsm"):
                print(bcolors.HEADER + f"Microsoft Excel file with macros:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".xlsx"):
                print(bcolors.HEADER + f"Microsoft Excel Open XML spreadsheet file:{bcolors.OKBLUE} {self.dir}")

            # System file extensions
            elif self.dir.endswith(".bak"):
                print(bcolors.HEADER + f"Backup file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cab"):
                print(bcolors.HEADER + f"Windows Cabinet file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cfg"):
                print(bcolors.HEADER + f"Configuration file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cpl"):
                print(bcolors.HEADER + f"Windows Control panel file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".cur"):
                print(bcolors.HEADER + f"Windows cursor file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".dll"):
                print(bcolors.HEADER + f"DLL file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".dmp"):
                print(bcolors.HEADER + f"Dump file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".drv"):
                print(bcolors.HEADER + f"Device driver file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".icns"):
                print(bcolors.HEADER + f"macOS X icon resource file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ico"):
                print(bcolors.HEADER + f"Icon file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".ini"):
                print(bcolors.HEADER + f"Initialization file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".Ink"):
                print(bcolors.HEADER + f"Windows shortcut file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".msi"):
                print(bcolors.HEADER + f"Windows installer package:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".sys"):
                print(bcolors.HEADER + f"Windows system file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tmp"):
                print(bcolors.HEADER + f"Temporary file:{bcolors.OKBLUE} {self.dir}")

            # Video file extensions
            elif self.dir.endswith(".3g2"):
                print(bcolors.HEADER + f"3GPP2 multimedia file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".3gp"):
                print(bcolors.HEADER + f"3GPP multimedia file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".avi"):
                print(bcolors.HEADER + f"AVI file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".flv"):
                print(bcolors.HEADER + f"Adobe Flash file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".h264"):
                print(bcolors.HEADER + f"H.264 video file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".m4v"):
                print(bcolors.HEADER + f"Apple MP4 video file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mkv"):
                print(bcolors.HEADER + f"Matroska Multimedia Container:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mov"):
                print(bcolors.HEADER + f"Apple QuickTime movie file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mp4"):
                print(bcolors.HEADER + f"MPEG4 video file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mpg"):
                print(bcolors.HEADER + f"MPEG video file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".mpeg"):
                print(bcolors.HEADER + f"MPEG video file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".rm"):
                print(bcolors.HEADER + f"RealMedia file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".swf"):
                print(bcolors.HEADER + f"Shockwave flash file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".vob"):
                print(bcolors.HEADER + f"DVD Video Object:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wmv"):
                print(bcolors.HEADER + f"Windows Media Video file:{bcolors.OKBLUE} {self.dir}")

            # Text file extensions
            elif self.dir.endswith(".doc"):
                print(bcolors.HEADER + f"Microsoft Word file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".docx"):
                print(bcolors.HEADER + f"Microsoft Word file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".odt"):
                print(bcolors.HEADER + f"OpenOffice Writer document file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".pdf"):
                print(bcolors.HEADER + f"PDF file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".rtf"):
                print(bcolors.HEADER + f"Rich Text Format:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".tex"):
                print(bcolors.HEADER + f"A LaTeX document file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".txt"):
                print(bcolors.HEADER + f"Plain text file:{bcolors.OKBLUE} {self.dir}")

            elif self.dir.endswith(".wdp"):
                print(bcolors.HEADER + f"WordPerfect document:{bcolors.OKBLUE} {self.dir}")


if __name__ == "__main__":
    os.system("cls")
    colors = bcolors
    print(bcolors.OKGREEN)
    print(f.renderText('PjFileExplorer'))
    print(bcolors.ENDC)
    print(bcolors.OKBLUE + "Commands:\nopen_file 'Opens a supported file.'\n")
    display = displayDirs()
    display.print("C:\\")
    while True:
        print("\u001b[0m")
        dir = input(bcolors.ENDC + "What is the directory where you want to go to?: ")
        if dir == "open_file":
            dir = input(bcolors.ENDC + "What directory is the file in?: ")
            os.system("cls")
            print(bcolors.OKGREEN)
            print(f.renderText('PjFileExplorer'))
            print(bcolors.ENDC)
            display.printSupportedFiles(dir)
            exec = input(bcolors.ENDC + "What file do you want to open?: ")
            os.startfile(f"{dir}/{exec}")
        elif not dir.endswith("\\"):
            raise TypeError("Please provide a valid directory.")
        os.system("cls")
        print(bcolors.OKGREEN)
        print(f.renderText('PjFileExplorer'))
        print(bcolors.ENDC)
        display.print(path=dir)