# Samsung Remote

Python implementation of an IP remote for Samsung smart TVs. Uses Gtk for GUI

## How to use

After checking out this repo you will need to modify the `remote.desktop` file
so that it will point to your correct directories and then create a symlink for
it in your ~/.local/share/applications folder. This will allow you to use
Launcher to launch the app.

You will also need to edit the `util.py` file and change the IP addresses to
reflect your actual IP addresses.
