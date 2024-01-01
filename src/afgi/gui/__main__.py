#!/usr/bin/env python3
"""
Main module for AFGI GUI and entry point for the application.
Example:
    $ python3 -m afgi.gui
"""
def main():
    """Main entry point for the application."""
    app = wx.App(False)
    frame = frame.MyFrame(None, "AFGI")
    app.MainLoop()

if __name__ == "__main__":
    from afgi.gui import frame
    import wx
    main()