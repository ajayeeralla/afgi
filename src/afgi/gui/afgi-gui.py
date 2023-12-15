#!/usr/bin/env python

import wx;
import os;
import sys;

wildcard = "Text (*.txt)|*.txt|" \
            "Python (*.py)|*.py|" \
            "Yaml (*.yaml)|*.yaml|" \
            "All files (*.*)|*.*"

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

class MyPanel1(wx.Panel): 
   def __init__(self, parent, content): 
      super(MyPanel1, self).__init__(parent) 
      self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE, value = content, size = wx.Size(800,600)) 
       
    

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(800,600), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.SetIcon(wx.Icon('/Users/Ajay/afgi/src/afgi/gui/icons/title_bar_icon.ico', wx.BITMAP_TYPE_ANY))
        # self.SetBackgroundColour("gray")
        splitter = wx.SplitterWindow(self, -1)
        self.mainPanel = wx.Panel(splitter, -1, style=wx.DOUBLE_BORDER)
        self.mainPanel.SetBackgroundColour("white")
        self.nb = wx.Notebook(self.mainPanel, size=wx.Size(800,600))
        self.nb_changed = False
        self.panel2 = wx.Panel(splitter, -1, style=wx.DOUBLE_BORDER)
        self.panel2.SetBackgroundColour("cream")
        splitter.SplitVertically(self.mainPanel, self.panel2)

        #-----------------Default names-----------------#
        self.dirname = '.'
        self.filename = 'Untitled'
    

        # self.p = MyPanel1(self,"")
        # self.nb = wx.Notebook(self.p)
        # nb = wx.Notebook(self)
        # nb.AddPage(MyPanel1(nb),"Editor")
        # nb.AddPage(MyPanel1(nb),"RadioButtons")
        # self.Centre()
        # self.Show(True)
        # self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar(name="Status Bar") # A Statusbar in the bottom of the window
        # # Create a splitter window.
        # self.splitter = wx.SplitterWindow(self, 500, style=wx.SP_LIVE_UPDATE)

        # # Create the left panel.
        # self.leftPanel = wx.Panel(self.splitter, -1)
        # self.leftPanel.SetBackgroundColour("blue")

        #  # Create the right panel.
        # rightPanel = wx.Panel(self.splitter, -1, style=wx.SUNKEN_BORDER)
        # rightPanel.SetBackgroundColour('#79B4B7')

        # Creating the menubar.
        menu_bar = wx.MenuBar()

        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menu_bar)  

         # Setting up file menu.
        file_menu= wx.Menu()

        menu_bar.Append(file_menu,"&File") # Adding the "file_menu" to the MenuBar
        file_menu_item1 = wx.MenuItem(file_menu, wx.ID_NEW, "&New", "Create new file", wx.ITEM_NORMAL)
        file_menu.Append(file_menu_item1)

        file_menu_item2 = wx.MenuItem(file_menu, wx.ID_OPEN, "&Open", "Open existing file", wx.ITEM_NORMAL)
        file_menu.Append(file_menu_item2)

        file_menu_item3 = wx.MenuItem(file_menu, wx.ID_SAVE, "&Save", "Save the current file", wx.ITEM_NORMAL)
        file_menu.Append(file_menu_item3)

        file_menu_item4 = wx.MenuItem(file_menu, wx.ID_SAVEAS, "&Save As", "Save the file with a different name", wx.ITEM_NORMAL)
        file_menu.Append(file_menu_item4)

        file_menu_item5 = wx.MenuItem(file_menu, wx.ID_EXIT, "&Exit", "Exit the application", wx.ITEM_NORMAL)
        file_menu.Append(file_menu_item5)


        # Setting up Edit menu.
        edit_menu= wx.Menu()
        menu_bar.Append(edit_menu,"&Edit") # Adding the "edit_menu" to the MenuBar

        edit_menu_item1 = wx.MenuItem(edit_menu, wx.ID_UNDO, "&Undo", "To undo the last action", wx.ITEM_NORMAL)    
        edit_menu.Append(edit_menu_item1)

        edit_menu_item2 = wx.MenuItem(edit_menu, wx.ID_REDO, "&Redo", "To redo the last action", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item2)

        edit_menu_item3 = wx.MenuItem(edit_menu, wx.ID_CUT, "&Cut", "To cut the selected text", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item3)

        edit_menu_item4 = wx.MenuItem(edit_menu, wx.ID_COPY, "&Copy", "To copy the selected text", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item4)

        edit_menu_item5 = wx.MenuItem(edit_menu, wx.ID_PASTE, "&Paste", "To paste the copied text", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item5)

        edit_menu_item6 = wx.MenuItem(edit_menu, wx.ID_DELETE, "&Delete", "To delete the selected text", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item6)

        edit_menu_item7 = wx.MenuItem(edit_menu, wx.ID_SELECTALL, "&Select All", "To select all the text", wx.ITEM_NORMAL)
        edit_menu.Append(edit_menu_item7)

        # Setting up View menu.
        view_menu= wx.Menu()
        menu_bar.Append(view_menu,"&View") # Adding the "view_menu" to the MenuBar

        # view_menu_item1 = wx.MenuItem(view_menu, wx.ID_VIEW_DETAILS, "&Details", "To view the details", wx.ITEM_NORMAL)
        # view_menu.Append(view_menu_item1)

        # view_menu_item2 = wx.MenuItem(view_menu, wx.ID_VIEW_LARGEICONS, "&Large Icons", "To view the large icons", wx.ITEM_NORMAL)
        # view_menu.Append(view_menu_item2)

        # view_menu_item3 = wx.MenuItem(view_menu, wx.ID_VIEW_SMALLICONS, "&Small Icons", "To view the small icons", wx.ITEM_NORMAL)
        # view_menu.Append(view_menu_item3)

        # view_menu_item4 = wx.MenuItem(view_menu, wx.ID_VIEW_LIST, "&List", "To view the list", wx.ITEM_NORMAL)
        # view_menu.Append(view_menu_item4)

        # Setting up Run menu.
        run_menu= wx.Menu()
        menu_bar.Append(run_menu,"&Run") # Adding the "run_menu" to the MenuBar

        run_menu_item1 = wx.MenuItem(run_menu, wx.ID_ANY, "&VCF", "To run VCF", wx.ITEM_NORMAL)
        run_menu.Append(run_menu_item1)

        run_menu_item2 = wx.MenuItem(run_menu, wx.ID_ANY, "&JG", "To run JG", wx.ITEM_NORMAL)
        run_menu.Append(run_menu_item2)

        # Setting up Terminal menu.
        terminal_menu= wx.Menu()
        menu_bar.Append(terminal_menu,"&Terminal")

        terminal_menu_item1 = wx.MenuItem(terminal_menu, wx.ID_ANY, "&New Terminal", "To open a new terminal", wx.ITEM_NORMAL)
        terminal_menu.Append(terminal_menu_item1)

        terminal_menu_item2 = wx.MenuItem(terminal_menu, wx.ID_CLOSE, "&Close Terminal", "To close the terminal", wx.ITEM_NORMAL)
        terminal_menu.Append(terminal_menu_item2)

        # Setting up Help menu.
        help_menu= wx.Menu()
        menu_bar.Append(help_menu,"&Help") # Adding the "help_menu" to the MenuBar

        help_menu_item1 = wx.MenuItem(help_menu, wx.ID_ABOUT, "&About", "To know about the application", wx.ITEM_NORMAL)
        help_menu.Append(help_menu_item1)

        # Setting up the status bar.
        self.CreateStatusBar()
        self.SetStatusText("Welcome to AFGI: Augmented Formal Graphical Interface!")

        # Setting up the tb.
        tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
        
        self.SetToolBar(tb)
        # tb.AddTool( 101, wx.Bitmap("new.png"))
        tb.AddTool(1, "New", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/new.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'New', "Long help for 'New'.", None)
        tb.AddTool(2, "Open", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/open.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Open', "Long help for 'Open'.", None)
        tb.AddTool(3, "Save", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/save.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Save', "Long help for 'Save'.", None)
        tb.AddSeparator()
        tb.AddTool(4, "undo", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/undo.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Undo', "Long help for 'Undo'.", None)
        tb.AddTool(5, "redo", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/redo.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Redo', "Long help for 'Redo'.", None)
        tb.AddSeparator()
        combo = wx.ComboBox(tb, choices=["FPV", "FRV", "Etc"])
        tb.AddControl(combo)
        tb.AddSeparator()
        tb.AddTool(6, "Exit", wx.Image('/Users/Ajay/afgi/src/afgi/gui/bitmaps/exit.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Exit', "Long help for 'Exit'.", None)
        tb.AddSeparator()

        tb.Realize()
        self.log = wx.TextCtrl(self.panel2, -1, size=(800, 600), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir
        # Set File menu item events.
        self.Bind(wx.EVT_MENU, self.OnNew, file_menu_item1)
        self.Bind(wx.EVT_MENU, self.OnOpen, file_menu_item2)
        self.Bind(wx.EVT_MENU, self.OnSave, file_menu_item3)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, file_menu_item4)        
        self.Bind(wx.EVT_MENU, self.OnExit, file_menu_item5)

        # Set Toolbar events.
        self.Bind(wx.EVT_TOOL, self.OnNew, id=1)
        self.Bind(wx.EVT_TOOL, self.OnOpen, id=2)
        self.Bind(wx.EVT_TOOL, self.OnSave, id=3)
        self.Bind(wx.EVT_TOOL, self.OnUndo, id=4)
        self.Bind(wx.EVT_TOOL, self.OnRedo, id=5)
        self.Bind(wx.EVT_TOOL, self.OnExit, id=6)

        # Set Edit menu item events.
        self.Bind(wx.EVT_MENU, self.OnUndo, edit_menu_item1)
        self.Bind(wx.EVT_MENU, self.OnRedo, edit_menu_item2)
        self.Bind(wx.EVT_MENU, self.OnCut, edit_menu_item3)
        self.Bind(wx.EVT_MENU, self.OnCopy, edit_menu_item4)
        self.Bind(wx.EVT_MENU, self.OnPaste, edit_menu_item5)
        self.Bind(wx.EVT_MENU, self.OnDelete, edit_menu_item6)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, edit_menu_item7)

        # Set View menu item events.

        # Set Run menu item events.
        self.Bind(wx.EVT_MENU, self.OnVCF, run_menu_item1)
        self.Bind(wx.EVT_MENU, self.OnJG, run_menu_item2)

        # Set Terminal menu item events.
        self.Bind(wx.EVT_MENU, self.OnNewTerminal, terminal_menu_item1)
        self.Bind(wx.EVT_MENU, self.OnCloseTerminal, terminal_menu_item2)
        # Set Help menu item events.
        self.Bind(wx.EVT_MENU, self.OnAbout, help_menu_item1)
        self.Show(True)

        # Shortcuts for menu items
        entry1 = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('N'), file_menu_item1.GetId())
        file_menu_item1.SetAccel(entry1)
        entry2 = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('O'), file_menu_item2.GetId())
        file_menu_item2.SetAccel(entry2)
        entry3 = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('S'), file_menu_item3.GetId())
        file_menu_item3.SetAccel(entry3)
        entry4 = wx.AcceleratorEntry(wx.ACCEL_ALT, ord('S'), file_menu_item4.GetId())
        file_menu_item4.SetAccel(entry4)
        entry5 = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Q'), file_menu_item5.GetId())
        file_menu_item5.SetAccel(entry5)

        # Create Tool 
        
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    def OnPageChanged(self, event):
          old = event.GetOldSelection()
          new = event.GetSelection()
          sel = self.nb.GetSelection()
          print ('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
          event.Skip()
    def OnPageChanging(self, event):
          old = event.GetOldSelection()
          new = event.GetSelection()
          sel = self.nb.GetSelection()
          print ('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
          event.Skip()

   # TODO: Fix this to change selection to new page
    
    def MyFileDialog(self, text, style, mode):
        dlg = wx.FileDialog(self, "Give a file name", self.dirname, self.filename, wildcard, style)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            if mode == "new":
                f = open(os.path.join(self.dirname, self.filename), 'w')
                self.tab = MyPanel1(self.nb, "")
                self.nb.AddPage(self.tab, self.filename, True)
                self.PushStatusText(text)
                f.close()
            elif mode == "open":
                f = open(os.path.join(self.dirname, self.filename), 'r')
                content = f.read()
                self.tab = MyPanel1(self.nb, content)
                self.nb.AddPage(self.tab, self.filename, True)
                f.close()
                self.PushStatusText(text)
            elif mode == "write":
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.nb.GetCurrentPage().text.GetValue())
                f.close()
                self.PushStatusText(text)
            else:
                pass
        dlg.Destroy()


    def SaveCurrentFile(self):
        return wx.MessageBox("Do you want to save the file?", "Please confirm", 
                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.YES
        


    #file menu item event handlers.
    # OnNew method is used to create a new file.
    def OnNew(self, e):
        """ Create a new file"""
        if self.nb.GetCurrentPage() is not None:
            if self.nb.GetCurrentPage().text.IsModified():
                if self.SaveCurrentFile():
                    self.OnSave(e)
        self.MyFileDialog("New file Created!", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "new")
      

    def OnOpen(self, e):
        """ Open a file"""
        if self.nb.GetCurrentPage() is not None: 
            if self.nb.GetCurrentPage().text.IsModified():
                if self.SaveCurrentFile():
                    self.OnSave(e)
        self.MyFileDialog("File opened!", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, "open")

    def OnSave(self, e):
        """ Save file"""
        if self.nb.GetCurrentPage() is not None:
            if self.nb.GetCurrentPage().text.IsModified():
                index = self.nb.GetSelection()
                f = open(os.path.join(os.getcwd(), self.nb.GetPageText(index)), 'w')
                f.write(self.nb.GetCurrentPage().text.GetValue())
                self.nb_changed = False
                self.PushStatusText("File saved!")
                f.close()

    def OnSaveAs(self, e):
        """ Save a file with a different name"""
        self.MyFileDialog("File saved!", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "write")

    def OnExit(self, e):
            self.Close(True)  # Close the frame.

    # edit menu item event handlers        
    def OnUndo(self, e):
        self.nb.GetCurrentPage().text.Undo()

    def OnRedo(self, e):
        self.nb.GetCurrentPage().text.Redo()

    def OnCut(self, e):
        self.nb.GetCurrentPage().text.Cut()

    def OnCopy(self, e):
        self.nb.GetCurrentPage().text.Copy()

    def OnPaste(self, e):
        self.nb.GetCurrentPage().text.Paste()
    def OnDelete(self, e):
        self.nb.GetCurrentPage().text.Clear()
    def OnSelectAll(self, e):
        self.nb.GetCurrentPage().text.SelectAll()

    # run menu item event handlers
    def OnVCF(self, e):
        frame = wx.Frame(None, -1, 'win.py')
        frame.Show()

    def OnJG(self, e):
        frame = wx.Frame(None, -1, 'win.py')
        frame.Show()


    # terminal menu item event handlers
    def OnNewTerminal(self, e):
        frame = wx.Frame(None, -1, 'win.py')
        frame.Show()

    def OnCloseTerminal(self, e):
        self.Close(True)

    # help menu item event handlers
    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "AFGI: Augmented Formal Graphical Interface\nVersion 0.0.1", "About AFGI", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.



app = wx.App(False)
frame = MyFrame(None, "AFGI")
app.MainLoop()
