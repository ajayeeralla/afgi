
def main():
    app = wx.App(False)
    frame = my_frame.MyFrame(None, "AFGI")
    app.MainLoop()

if __name__ == "__main__":
    import wx
    import my_frame
    main()