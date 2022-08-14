How to Fix:
"Program is damaged and can't be opened. You should eject the disk image."

Remove quarantine attributes:
Install the app.
Locate the app in the Finder and then open the Terminal application.
In the Terminal type:
xattr -d com.apple.quarantine
followed by a single space.
Then drag the app to the Terminal window, which should append its file path to the command, and press Enter to run the command.

Why?
Apple requires applications to be signed before they can be run. However, code signing is a paid process (costing a $99/year subscription, and more if you also want to publish to the Mac App Store).
Independent developers may not have the time or budget required to sign their applications or upload them to the Mac App Store. Due to this, many open source applications can’t be run out of the box on macOS.

h0fnar@protonmail.com