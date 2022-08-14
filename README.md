# m3u8-converter
This is an application to solve Unicode issues when transfering music playlists from iTunes on macOS to [Rockbox](https://www.rockbox.org) on your iPod.

> macOS utilizes a different Unicode than Rockbox does.

Special characters like ä,ö,é etc.  in path or file name on macOS will cause skipping issues on Rockbox. 
This app solves this problem and additionally gives you the option to find and replace  within a playlist, so the paths will match with your Rockbox library.

Just drag and drop a folder with m3u8´s. Hit Convert and a new folder with your converted m3u8`s will be created.

Testet on macOS High Sierra, Mojave, Catalina.

[**_Download_**](https://github.com/h0fnar/m3u8-converter/releases/download/v1.0.1/M3U8-Converter-1.0.1.dmg)  the latest release as dmg.

![M3U8 Converter](/img/app.png)

# How to Fix:

### _"Program is damaged and can't be opened. You should eject the disk image."_

Install the app. Locate the app in the Finder and then open the Terminal application. In the Terminal type:
```
xattr -d com.apple.quarantine
```
followed by a single space. Then drag the app to the Terminal window, which should append its file path to the command, and press Enter to run the command.

> Why?
Apple requires applications to be signed before they can be run. However, code signing is a paid process (costing a $99/year subscription, and more if you also want to publish to the Mac App Store).
Independent developers may not have the time or budget required to sign their applications or upload them to the Mac App Store. Due to this, many open source applications can’t be run out of the box on macOS.

# Run from Source

### Install From Source
```
git clone https://github.com/h0fnar/m3u8-converter
```

### Install Dependencies
```
pip3 install pyqt5
```
> Testet with: PyQt5 Version: 5.15.6

### Start the app with:
```
cd /m3u8-converter
python3 main.py
```

# Compile Package

### Install From Source
```
git clone https://github.com/h0fnar/m3u8-converter
```

### Install Dependencies
```
pip3 install pyqt5
pip3 install PyInstaller
```
> Testet with: pyinstaller Version: 4.10, PyQt5 Version: 5.15.6

### Compile with pyinstaller
```
cd /m3u8-converter
python3 -m PyInstaller -n "M3U8 Converter" --icon "img/icon.icns" --windowed main.py
```

### Enable dark mode
> Add into info.plist in "/dict" (dist/M3U8 Converter.app "Show Package Contents")
```
<key>NSRequiresAquaSystemAppearance</key>
<string>False</string>
```
#

If you edit the Qt Designer files, you must recompile them before you compile the package.
```
cd /m3u8-converter
python3 -m PyQt5.uic.pyuic main_ui.ui -o main_ui.py
python3 -m PyQt5.uic.pyuic about_ui.ui -o about_ui.py
```
> You can download a small version of Qt Designer [here](https://build-system.fman.io/qt-designer-download).

If you make changes to the resources.qrc file, you also need to recompile it.
```
pyrcc5 resources.qrc -o resources_rc.py
```
