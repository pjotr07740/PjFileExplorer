import os
import shutil
from pyfiglet import Figlet
from update_check import isUpToDate


dir_path = os.path.dirname(os.path.realpath("main.py"))

if isUpToDate(f"{dir_path}/main.py", "https://raw.githubusercontent.com/pjotr07740/PjFileExplorer/master/src/main.py") == False:
   update(f"{dir_path}/main.py", "https://raw.githubusercontent.com/pjotr07740/PjFileExplorer/master/src/main.py")

f = Figlet(font='slant')


class ConsoleColors:
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


class DisplayDirs:

    def print(self, path):
        try:
            dirs = os.listdir(path=path)
        except Exception as e:
            print(f"Exception: {e}")

        for dir in dirs:
            if os.path.isdir(f"{path}{dir}"):
                print(ConsoleColors.HEADER + f"Folder:{ConsoleColors.OKBLUE} {path}{dir}\\")
            else:
                print(ConsoleColors.HEADER + f"File:{ConsoleColors.OKBLUE} {path}{dir}")

    def print_dirs(self, path):
        path = path
        try:
            dirs = os.listdir(path=path)
        except Exception as e:
            print(f"Exception: {e}")

        for dir in dirs:
            if os.path.isdir(f"{path}/{dir}"):
                print(ConsoleColors.HEADER + f"Folder:{ConsoleColors.OKBLUE} {dir}")

    def print_supported_files(self, path):
        path = path
        try:
            dirs = os.listdir(path=path)
        except Exception as e:
            print(f"Exception: {e}")

        for dir in dirs:
            # Audio files
            if dir.endswith(".aif"):
                print(ConsoleColors.HEADER + f"AIF audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cda"):
                print(ConsoleColors.HEADER + f"CD audio track file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mid"):
                print(ConsoleColors.HEADER + f"MIDI audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".midi"):
                print(ConsoleColors.HEADER + f"MIDI audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mp3"):
                print(ConsoleColors.HEADER + f"MP3 audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mpa"):
                print(ConsoleColors.HEADER + f"MPEG-2 audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ogg"):
                print(ConsoleColors.HEADER + f"Ogg Vorbis audio file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wav"):
                print(ConsoleColors.HEADER + f"WAV file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wma"):
                print(ConsoleColors.HEADER + f"WMA audio file :{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wpl"):
                print(ConsoleColors.HEADER + f"Windows Media Player playlist:{ConsoleColors.OKBLUE} {dir}")

            # Compressed files
            elif dir.endswith(".7z"):
                print(ConsoleColors.HEADER + f"7-Zip compressed file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".arj"):
                print(ConsoleColors.HEADER + f"ARJ compressed file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".deb"):
                print(ConsoleColors.HEADER + f"Debian software package file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pkg"):
                print(ConsoleColors.HEADER + f"Package file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".rar"):
                print(ConsoleColors.HEADER + f"RAR file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".rpm"):
                print(ConsoleColors.HEADER + f"Red Hat Package Manager:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tar.gz"):
                print(ConsoleColors.HEADER + f"Tarball compressed file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".z"):
                print(ConsoleColors.HEADER + f"Z compressed file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".zip"):
                print(ConsoleColors.HEADER + f"Zip compressed file:{ConsoleColors.OKBLUE} {dir}")

            # Disc and media files
            elif dir.endswith(".bin"):
                print(ConsoleColors.HEADER + f"Binary disc image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".dmg"):
                print(ConsoleColors.HEADER + f"macOS X disk image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".iso"):
                print(ConsoleColors.HEADER + f"ISO disc image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".toast"):
                print(ConsoleColors.HEADER + f"Toast disc image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".vcd"):
                print(ConsoleColors.HEADER + f"Virtual CD:{ConsoleColors.OKBLUE} {dir}")

            # Data and database files
            elif dir.endswith(".csv"):
                print(ConsoleColors.HEADER + f"Comma separated value file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".dat"):
                print(ConsoleColors.HEADER + f"Data file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".db"):
                print(ConsoleColors.HEADER + f"Database file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".dbf"):
                print(ConsoleColors.HEADER + f"Database file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".log"):
                print(ConsoleColors.HEADER + f"Log file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mdb"):
                print(ConsoleColors.HEADER + f"Microsoft Access database file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".sav"):
                print(ConsoleColors.HEADER + f"Save file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".sql"):
                print(ConsoleColors.HEADER + f"SQL database file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tar"):
                print(ConsoleColors.HEADER + f"Linux / Unix tarball file archive:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".xml"):
                print(ConsoleColors.HEADER + f"XML file:{ConsoleColors.OKBLUE} {dir}")

            # Email File extensions
            elif dir.endswith(".email"):
                print(ConsoleColors.HEADER + f"Outlook Express e-mail message file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".eml"):
                print(ConsoleColors.HEADER + f"E-mail message file from multiple e-mail clients, including Gmail:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".emlx"):
                print(ConsoleColors.HEADER + f"Apple Mail e-mail file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".msg"):
                print(ConsoleColors.HEADER + f"Microsoft Outlook e-mail message file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".oft"):
                print(ConsoleColors.HEADER + f"Microsoft Outlook e-mail template file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ost"):
                print(ConsoleColors.HEADER + f"Microsoft Outlook offline e-mail storage file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pst"):
                print(ConsoleColors.HEADER + f"Microsoft Outlook e-mail storage file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".vcf"):
                print(ConsoleColors.HEADER + f"E-mail contact file:{ConsoleColors.OKBLUE} {dir}")

            # Executable file extensions
            elif dir.endswith(".apk"):
                print(ConsoleColors.HEADER + f"Android package file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".bat"):
                print(ConsoleColors.HEADER + f"Batch file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cgi"):
                print(ConsoleColors.HEADER + f"Perl script file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".com"):
                print(ConsoleColors.HEADER + f"MS-DOS command file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".exe"):
                print(ConsoleColors.HEADER + f"Executable file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".gadget"):
                print(ConsoleColors.HEADER + f"Windows gadget:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".jar"):
                print(ConsoleColors.HEADER + f"Java Archive file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pl"):
                print(ConsoleColors.HEADER + f"Perl script file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".msi"):
                print(ConsoleColors.HEADER + f"Windows installer package:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".py"):
                print(ConsoleColors.HEADER + f"Python file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wsf"):
                print(ConsoleColors.HEADER + f"Windows Script File:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".bin"):
                print(ConsoleColors.HEADER + f"Binary file:{ConsoleColors.OKBLUE} {dir}")

            # Font file extensions
            elif dir.endswith(".fnt"):
                print(ConsoleColors.HEADER + f"Windows font file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".fon"):
                print(ConsoleColors.HEADER + f"Generic font file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".otf"):
                print(ConsoleColors.HEADER + f"Open type font file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ttf"):
                print(ConsoleColors.HEADER + f"TrueType font file:{ConsoleColors.OKBLUE} {dir}")

            # Image file extensions
            elif dir.endswith(".ai"):
                print(ConsoleColors.HEADER + f"Adobe Illustrator file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".bmp"):
                print(ConsoleColors.HEADER + f"Bitmap image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".gif"):
                print(ConsoleColors.HEADER + f"GIF image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ico"):
                print(ConsoleColors.HEADER + f"Icon file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".jpeg"):
                print(ConsoleColors.HEADER + f"JPEG image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".jpg"):
                print(ConsoleColors.HEADER + f"JPEG image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".png"):
                print(ConsoleColors.HEADER + f"PNG image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ps"):
                print(ConsoleColors.HEADER + f"PostScript file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".psd"):
                print(ConsoleColors.HEADER + f"PSD image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".svg"):
                print(ConsoleColors.HEADER + f"Scalable Vector Graphics file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tif"):
                print(ConsoleColors.HEADER + f"TIFF image:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tiff"):
                print(ConsoleColors.HEADER + f"TIFF image:{ConsoleColors.OKBLUE} {dir}")

            # Internet file extensions
            elif dir.endswith(".asp"):
                print(ConsoleColors.HEADER + f"Active Server Page file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".aspx"):
                print(ConsoleColors.HEADER + f"Active Server Page file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cer"):
                print(ConsoleColors.HEADER + f"Internet security certificate:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cfm"):
                print(ConsoleColors.HEADER + f"ColdFusion Markup file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cgi"):
                print(ConsoleColors.HEADER + f"Perl script file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pl"):
                print(ConsoleColors.HEADER + f"Perl script file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".css"):
                print(ConsoleColors.HEADER + f"Cascading Style Sheet file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".htm"):
                print(ConsoleColors.HEADER + f"HTML file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".html"):
                print(ConsoleColors.HEADER + f"HTML file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".js"):
                print(ConsoleColors.HEADER + f"JavaScript file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".jsp"):
                print(ConsoleColors.HEADER + f"Java Server Page file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".part"):
                print(ConsoleColors.HEADER + f"Partially downloaded file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".php"):
                print(ConsoleColors.HEADER + f"PHP file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".py"):
                print(ConsoleColors.HEADER + f"Python file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".rss"):
                print(ConsoleColors.HEADER + f"RSS file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".xhtml"):
                print(ConsoleColors.HEADER + f"XHTML file:{ConsoleColors.OKBLUE} {dir}")

            # Presentation file extensions
            elif dir.endswith(".key"):
                print(ConsoleColors.HEADER + f"Keynote presentation:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".odp"):
                print(ConsoleColors.HEADER + f"OpenOffice Impress presentation file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pps"):
                print(ConsoleColors.HEADER + f"PowerPoint slide show:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ppt"):
                print(ConsoleColors.HEADER + f"PowerPoint presentation:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pptx"):
                print(ConsoleColors.HEADER + f"PowerPoint Open XML presentation:{ConsoleColors.OKBLUE} {dir}")

            # Programming file extensions
            elif dir.endswith(".c"):
                print(ConsoleColors.HEADER + f"C and C++ source code file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".class"):
                print(ConsoleColors.HEADER + f"Java class file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cpp"):
                print(ConsoleColors.HEADER + f"C++ source code file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cs"):
                print(ConsoleColors.HEADER + f"Visual C# source code file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".h"):
                print(ConsoleColors.HEADER + f"C, C++, and Objective-C header file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".java"):
                print(ConsoleColors.HEADER + f"Java Source code file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pl"):
                print(ConsoleColors.HEADER + f"Perl script file.:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".sh"):
                print(ConsoleColors.HEADER + f"Bash shell script:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".swift"):
                print(ConsoleColors.HEADER + f"Swift source code file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".vb"):
                print(ConsoleColors.HEADER + f"Visual Basic file:{ConsoleColors.OKBLUE} {dir}")

            # Spreadsheet file formats
            elif dir.endswith(".ods"):
                print(ConsoleColors.HEADER + f"OpenOffice Calc spreadsheet file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".xls"):
                print(ConsoleColors.HEADER + f"Microsoft Excel file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".xlsm"):
                print(ConsoleColors.HEADER + f"Microsoft Excel file with macros:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".xlsx"):
                print(ConsoleColors.HEADER + f"Microsoft Excel Open XML spreadsheet file:{ConsoleColors.OKBLUE} {dir}")

            # System file extensions
            elif dir.endswith(".bak"):
                print(ConsoleColors.HEADER + f"Backup file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cab"):
                print(ConsoleColors.HEADER + f"Windows Cabinet file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cfg"):
                print(ConsoleColors.HEADER + f"Configuration file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cpl"):
                print(ConsoleColors.HEADER + f"Windows Control panel file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".cur"):
                print(ConsoleColors.HEADER + f"Windows cursor file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".dll"):
                print(ConsoleColors.HEADER + f"DLL file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".dmp"):
                print(ConsoleColors.HEADER + f"Dump file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".drv"):
                print(ConsoleColors.HEADER + f"Device driver file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".icns"):
                print(ConsoleColors.HEADER + f"macOS X icon resource file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ico"):
                print(ConsoleColors.HEADER + f"Icon file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".ini"):
                print(ConsoleColors.HEADER + f"Initialization file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".Ink"):
                print(ConsoleColors.HEADER + f"Windows shortcut file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".msi"):
                print(ConsoleColors.HEADER + f"Windows installer package:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".sys"):
                print(ConsoleColors.HEADER + f"Windows system file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tmp"):
                print(ConsoleColors.HEADER + f"Temporary file:{ConsoleColors.OKBLUE} {dir}")

            # Video file extensions
            elif dir.endswith(".3g2"):
                print(ConsoleColors.HEADER + f"3GPP2 multimedia file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".3gp"):
                print(ConsoleColors.HEADER + f"3GPP multimedia file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".avi"):
                print(ConsoleColors.HEADER + f"AVI file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".flv"):
                print(ConsoleColors.HEADER + f"Adobe Flash file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".h264"):
                print(ConsoleColors.HEADER + f"H.264 video file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".m4v"):
                print(ConsoleColors.HEADER + f"Apple MP4 video file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mkv"):
                print(ConsoleColors.HEADER + f"Matroska Multimedia Container:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mov"):
                print(ConsoleColors.HEADER + f"Apple QuickTime movie file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mp4"):
                print(ConsoleColors.HEADER + f"MPEG4 video file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mpg"):
                print(ConsoleColors.HEADER + f"MPEG video file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".mpeg"):
                print(ConsoleColors.HEADER + f"MPEG video file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".rm"):
                print(ConsoleColors.HEADER + f"RealMedia file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".swf"):
                print(ConsoleColors.HEADER + f"Shockwave flash file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".vob"):
                print(ConsoleColors.HEADER + f"DVD Video Object:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wmv"):
                print(ConsoleColors.HEADER + f"Windows Media Video file:{ConsoleColors.OKBLUE} {dir}")

            # Text file extensions
            elif dir.endswith(".doc"):
                print(ConsoleColors.HEADER + f"Microsoft Word file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".docx"):
                print(ConsoleColors.HEADER + f"Microsoft Word file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".odt"):
                print(ConsoleColors.HEADER + f"OpenOffice Writer document file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".pdf"):
                print(ConsoleColors.HEADER + f"PDF file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".rtf"):
                print(ConsoleColors.HEADER + f"Rich Text Format:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".tex"):
                print(ConsoleColors.HEADER + f"A LaTeX document file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".txt"):
                print(ConsoleColors.HEADER + f"Plain text file:{ConsoleColors.OKBLUE} {dir}")

            elif dir.endswith(".wdp"):
                print(ConsoleColors.HEADER + f"WordPerfect document:{ConsoleColors.OKBLUE} {dir}")


if __name__ == "__main__":
    os.system("cls")
    colors = ConsoleColors
    print(ConsoleColors.OKGREEN)
    print(f.renderText('PjFileExplorer'))
    print(ConsoleColors.ENDC)
    print(ConsoleColors.OKBLUE + "Commands:\nopen_file 'Opens a supported file.'\nremove_file 'Deletes a file.'\nremove_dir_safe 'Removes a directory in safe mode this means it won't delete directories with files left in it.'\nremove_dir_unsafe 'Exactly previous command but then it doesn't care if there are still files left.'\n")
    display = DisplayDirs()
    display.print("C:\\")
    while True:
        print("\u001b[0m")
        dir = input(ConsoleColors.ENDC + "What is the directory where you want to go to?: ")
        if dir == "open_file":
            dir = input(ConsoleColors.ENDC + "What directory is the file in?: ")
            os.system("cls")
            print(ConsoleColors.OKGREEN)
            print(f.renderText('PjFileExplorer'))
            print(ConsoleColors.ENDC)
            display.print_supported_files(dir)
            exec = input(ConsoleColors.ENDC + "What file do you want to open?: ")
            os.startfile(f"{dir}/{exec}")
        elif dir == "remove_file":
            dir = input("What directory is the file in?: ")
            os.system("cls")
            print(ConsoleColors.OKGREEN)
            print(f.renderText('PjFileExplorer'))
            print(ConsoleColors.ENDC)
            display.print_supported_files(dir)
            exec = input(ConsoleColors.ENDC + "What file do you want to delete?: ")
            os.remove(f"{dir}/{exec}")
        elif dir == "remove_dir_safe":
            dir = input("Where is the directory you want to remove?: ")
            os.system("cls")
            print(ConsoleColors.OKGREEN)
            print(f.renderText('PjFileExplorer'))
            print(ConsoleColors.ENDC)
            display.print_dirs(dir)
            exec = input(ConsoleColors.ENDC + "What directory do you want to delete?: ")
            os.rmdir(f"{dir}/{exec}")
        elif dir == "remove_dir_unsafe":
            dir = input("Where is the directory you want to remove?: ")
            os.system("cls")
            print(ConsoleColors.OKGREEN)
            print(f.renderText('PjFileExplorer'))
            print(ConsoleColors.ENDC)
            display.print_dirs(dir)
            exec = input(ConsoleColors.ENDC + "What directory do you want to delete?: ")
            shutil.rmtree(f"{dir}/{exec}")
        elif not dir.endswith("\\"):
            raise TypeError("Please provide a valid directory.")
        os.system("cls")
        print(ConsoleColors.OKGREEN)
        print(f.renderText('PjFileExplorer'))
        print(ConsoleColors.ENDC)
        display.print(path=dir)