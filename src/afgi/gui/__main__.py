
def main():
    app = wx.App(False)
    frame = my_frame.MyFrame(None, "AFGI")
    app.MainLoop()

if __name__ == "__main__":
    from gui import my_frame
    import wx
    main()