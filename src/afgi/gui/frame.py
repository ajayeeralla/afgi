#!/usr/bin/env python3
import wx;
import os;
import sys;
import itertools;

# Setting up the wildcard for the file dialog
wildcard = "Text (*.txt)|*.txt|" \
            "Python (*.py)|*.py|" \
            "Yaml (*.yaml)|*.yaml|" \
            "All files (*.*)|*.*"

# Redirect the output of the console to the text control
class RedirectText(object):
    """A class to redirect the output of the console to the text control
    
    Attributes: 
        awxTextCtrl (wx.TextCtrl): text control to which the output is redirected  
    """
    def __init__(self, aWxTextCtrl):
        """The constructor of the RedirectText class"""
        self.out = aWxTextCtrl

    def write(self, string):
        """A method to write the output to the text control 
        Args:
            string (str): output string
        """
        self.out.WriteText(string)

# MyPanel class is used to create a panel for each tab in the notebook
class MyPanel(wx.Panel): 
    """A class to create a panel for each tab in the notebook

    Attributes:
        parent (wx.Panel): parent panel
        content (str): content of the panel
        text (wx.TextCtrl): text control to display the content of the panel
    """
    def __init__(self, parent, content): 
      super(MyPanel, self).__init__(parent) 
      self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE, value = content, size = wx.Size(800,600)) 
       
    
# MyFrame class is used to create the main window of the application
class MyFrame(wx.Frame):
    """A class to create the main window of the application

    Attributes:
        parent (wx.Frame): parent frame
        title (str): title of the frame 
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(800,600), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons/tool_icon.png')
        self.SetIcon(wx.Icon(filename, wx.BITMAP_TYPE_ANY))

        # Setting up the splitter window.
        splitter = wx.SplitterWindow(self, -1)
        self.mainPanel = wx.Panel(splitter, -1, style=wx.DOUBLE_BORDER)
        self.mainPanel.SetBackgroundColour("white")
        self.nb = wx.Notebook(self.mainPanel, size=wx.Size(800,600))
        self.nb_changed = False
        self.panel2 = wx.Panel(splitter, -1, style=wx.DOUBLE_BORDER)
        self.panel2.SetBackgroundColour("cream")
        splitter.SplitVertically(self.mainPanel, self.panel2)
        self.log = wx.TextCtrl(self.panel2, -1, size=(800, 600), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.redir = RedirectText(self.log)
        #-----------------Default names-----------------#
        self.dirname = '.'
        self.filename = 'Untitled'
        #------------------------------------------------#

        # Creating the menubar.
        menu_bar = wx.MenuBar()
        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menu_bar)  
        # Setting up file menu.
        file_menu= wx.Menu()
        menu_bar.Append(file_menu, "&File") # Adding the "file_menu" to the MenuBar
        # Create and add menu items to the file menu
        file_menu_labels = ["&New\tCtrl+N", "&Open\tCtrl+O", "&Save\tCtrl+S", "&Save As\tAlt+S", "&Exit\tCtrl+Q"]  
        file_menu_item_ids = [wx.ID_NEW, wx.ID_OPEN, wx.ID_SAVE, wx.ID_SAVEAS, wx.ID_EXIT]
        file_menu_descs = ["Create new file", "Open existing file", "Save the current file", "Save the file with a different name", "Exit the application"]
        file_menu_items = []
        for id, label, desc in itertools.zip_longest(file_menu_item_ids, file_menu_labels, file_menu_descs):
            file_menu_item = wx.MenuItem(file_menu, id, label, desc, wx.ITEM_NORMAL)
            file_menu_items.append(file_menu_item)
            file_menu.Append(file_menu_item)           
        # Setting up event handlers for the file menu items.
        file_menu_events = ['OnNew', 'OnOpen', 'OnSave', 'OnSaveAs', 'OnExit']
        for e, item in zip(file_menu_events, file_menu_items):
            event = getattr(self, e)
            self.Bind(wx.EVT_MENU, event, item)     
        # Setting up Edit menu.
        edit_menu= wx.Menu()
        menu_bar.Append(edit_menu,"&Edit") # Adding the "edit_menu" to the MenuBar
        # create and add menu items to the edit menu
        edit_menu_labels = ["&Undo\tCtrl+Z", "&Redo\tCtrl+Y", "&Cut\tCtrl+X", "&Copy\tCtrl+C", "&Paste\tCtrl+V", "&Delete\tDel", "&Select All\tCtrl+A"]
        edit_menu_item_ids = [wx.ID_UNDO, wx.ID_REDO, wx.ID_CUT, wx.ID_COPY, wx.ID_PASTE, wx.ID_DELETE, wx.ID_SELECTALL]
        edit_menu_descs = ["To undo the last action", "To redo the last action", "To cut the selected text", "To copy the selected text", "To paste the copied text", "To delete the selected text", "To select all the text"]
        edit_menu_items = []
        for id, label, desc in itertools.zip_longest(edit_menu_item_ids, edit_menu_labels, edit_menu_descs):
            edit_menu_item = wx.MenuItem(edit_menu, id, label, desc, wx.ITEM_NORMAL)
            edit_menu_items.append(edit_menu_item)
            edit_menu.Append(edit_menu_item)
        # Setting up event handlers for the edit menu items.
        edit_menu_events = ['OnUndo', 'OnRedo', 'OnCut', 'OnCopy', 'OnPaste', 'OnDelete', 'OnSelectAll']
        for e, item in zip(edit_menu_events, edit_menu_items):
            event = getattr(self, e)
            self.Bind(wx.EVT_MENU, event, item)
        # Setting up View menu.
        view_menu= wx.Menu()
        menu_bar.Append(view_menu,"&View") # Adding the "view_menu" to the MenuBar
        # view_menu_labels = ["&Zoom In\tCtrl++", "&Zoom Out\tCtrl+-", "&Reset Zoom\tCtrl+0", "&View TCL\tCtrl+T"]
        view_menu_labels = ["&View TCL\tCtrl+T"]
        # view_menu_item_ids = [wx.ID_ZOOM_IN, wx.ID_ZOOM_OUT, wx.ID_ZOOM_100, wx.ID_PREVIEW]
        view_menu_item_ids = [wx.ID_PREVIEW]
        # view_menu_descs = ["To zoom in the text", "To zoom out the text", "To reset the zoom", "Generate and view the TCL file"]
        view_menu_descs = ["Generate and view the TCL file"]
        view_menu_items = []
        for id, label, desc in itertools.zip_longest(view_menu_item_ids, view_menu_labels, view_menu_descs):
            view_menu_item = wx.MenuItem(view_menu, id, label, desc, wx.ITEM_NORMAL)
            view_menu_items.append(view_menu_item)
            view_menu.Append(view_menu_item)
        # Setting up event handlers for the view menu items.
        # view_menu_events = ['OnZoomIn', 'OnZoomOut', 'OnResetZoom', 'OnTranslate']
        view_menu_events = ['OnTranslate']
        for e, item in zip(view_menu_events, view_menu_items):
            event = getattr(self, e)
            self.Bind(wx.EVT_MENU, event, item)
        # Setting up Run menu.
        run_menu= wx.Menu()
        menu_bar.Append(run_menu,"&Run") # Adding the "run_menu" to the MenuBar
        # create and add menu items to the run menu
        run_id = wx.ID_ANY
        # run_jg_id = wx.ID_ANY
        run_menu_labels = ["&Run\tCtrl+R"]
        run_menu_item_ids = [run_id]
        run_menu_descs = ["Run the selected tool on the given script"]
        run_menu_items = []
        for id, label, desc in itertools.zip_longest(run_menu_item_ids, run_menu_labels, run_menu_descs):
            run_menu_item = wx.MenuItem(run_menu, id, label, desc, wx.ITEM_NORMAL)
            run_menu.Append(run_menu_item)  
            run_menu_items.append(run_menu_item)
        self.Bind(wx.EVT_MENU, self.OnRun, run_menu_items[0])
        

        # # Setting up Console menu.
        console_menu= wx.Menu()
        menu_bar.Append(console_menu,"&Console")
        console_menu_labels = ["&Clear\tCtrl+L", "&Close Console\tCtrl+K"]
        console_menu_item_ids = [wx.ID_ANY, wx.ID_ANY]
        console_menu_descs = ["To clear the console", "To close the console"]
        console_menu_items = []
        for id, label, desc in itertools.zip_longest(console_menu_item_ids, console_menu_labels, console_menu_descs):
            console_menu_item = wx.MenuItem(console_menu, id, label, desc, wx.ITEM_NORMAL)
            console_menu.Append(console_menu_item)  
            console_menu_items.append(console_menu_item)
        # Setting up event handlers for the console menu items.
        console_menu_events = ['OnClear', 'OnCloseConsole']
        for e, item in zip(console_menu_events, console_menu_items):
            event = getattr(self, e)
            self.Bind(wx.EVT_MENU, event, item)
        # Setting up Help menu.
        help_menu= wx.Menu()
        menu_bar.Append(help_menu,"&Help") # Adding the "help_menu" to the MenuBar

        help_menu_item1 = wx.MenuItem(help_menu, wx.ID_ABOUT, "&About", "To know about the application", wx.ITEM_NORMAL)
        help_menu.Append(help_menu_item1)

         # Set Help menu item events.
        self.Bind(wx.EVT_MENU, self.OnAbout, help_menu_item1)
        self.Show(True)

        # Setting up the status bar.
        self.CreateStatusBar()
        self.SetStatusText("Welcome to AFGI: Augmented Formal Graphical Interface!")

        # Setting up the tb.
        tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
        self.SetToolBar(tb)

        dirname = os.path.dirname(__file__)
        tool_img_dir = os.path.join(dirname, 'bitmaps' )

        tb.AddTool(1, "New", wx.Image(tool_img_dir+'/new.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'New', "Long help for 'New'.", None)
        tb.AddTool(2, "Open", wx.Image(tool_img_dir+'/open.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Open', "Long help for 'Open'.", None)
        tb.AddTool(3, "Save", wx.Image(tool_img_dir+'/save.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Save', "Long help for 'Save'.", None)
        tb.AddSeparator()
        tb.AddTool(4, "undo", wx.Image(tool_img_dir+'/undo.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Undo', "Long help for 'Undo'.", None)
        tb.AddTool(5, "redo", wx.Image(tool_img_dir+'/redo.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Redo', "Long help for 'Redo'.", None)
        tb.AddSeparator()
        tb.AddTool(8, "Translate", wx.Image(tool_img_dir+'/convert.png',
                wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                wx.NullBitmap, wx.ITEM_NORMAL, 'Translate', "Translate to TCL", None)
        self.Bind(wx.EVT_TOOL, self.OnTranslate, id=8)
        self.tools_combo = wx.ComboBox(tb, choices=["VCF", "JG"])
        tb.AddControl(self.tools_combo)
        self.apps_combo = wx.ComboBox(tb, choices=["FPV", "FRV", "Etc"])
        tb.AddControl(self.apps_combo)
        self.mode_combo = wx.ComboBox(tb, choices=["GUI", "Batch"] )
        tb.AddControl(self.mode_combo)
        tb.AddTool(7, "Run", wx.Image(tool_img_dir+'/run_button.png',
                wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                wx.NullBitmap, wx.ITEM_NORMAL, 'Run', "Long help for 'Run'.", None)
        self.Bind(wx.EVT_TOOL, self.OnRun, id=7)
        tb.AddSeparator()
        tb.AddTool(6, "Exit", wx.Image(tool_img_dir+'/exit.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                        wx.NullBitmap, wx.ITEM_NORMAL, 'Exit', "Long help for 'Exit'.", None)
        tb.AddSeparator()
        tb.Realize()
        # Redirect the output of the console to the text control
        self.log = wx.TextCtrl(self.panel2, -1, size=(800, 600), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir

        # Set Toolbar events.
        tool_bar_items = ['OnNew', 'OnOpen', 'OnSave', 'OnUndo', 'OnRedo', 'OnExit']
        for item, i in zip(tool_bar_items, range(6)):
            item = getattr(self, item)
            self.Bind(wx.EVT_TOOL, item, id=i+1)

        # Set Run menu item events.
        self.Bind(wx.EVT_MENU, self.OnRun, run_menu_items[0])

        # # Set Console menu item events.
        # self.Bind(wx.EVT_MENU, self.OnNewTerminal, terminal_menu_item1)
        # self.Bind(wx.EVT_MENU, self.OnCloseTerminal, terminal_menu_item2)
       
        # Shortcuts for menu items
        key_shortcuts = ["N", "O", "S", "P", "Q"]
        for key, id, item in itertools.zip_longest(key_shortcuts, file_menu_item_ids, file_menu_items):
          tmp = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord(key), id)
          item.SetAccel(tmp)

        # Create Tool 
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    # Run event handlers
    def OnRun(self, event):
        """ A method to run a tool on the given script with the given arguments"""
        # Get the selected choice
        params = [self.apps_combo.GetValue(), self.mode_combo.GetValue()]
        idx = self.nb.GetSelection()
        script = self.nb.GetPageText(idx)
        if script.endswith(".yaml"):
            import afgi.yaml_to_tcl.tcl_gen as TclGen
            TclGen.TclGen(script, script.replace(".yaml", ".tcl"))
            script = script.replace(".yaml", ".tcl")
        tool = self.tools_combo.GetValue().lower()
        from afgi.run_tools import RunTool
        run_obj = RunTool(tool, script, params)
        try:
            err = run_obj.run()
        except:
            pass
        RedirectText(self.log).write(f"$ {tool} {script} {' '.join(['-'+x.lower() for x in params])}\n")


    # On clear console
    def OnClear(self, event):
        """ A method to clear the console"""
        self.log.Clear()

    # Translate event handlers
    def OnTranslate(self, event):
        """ A method to translate a yaml file to tcl and open it in a new tab"""
        # Get the selected choice
        idx = self.nb.GetSelection()
        script = self.nb.GetPageText(idx)
        tcl_file = script.replace(".yaml", ".tcl")
        if os.path.isfile(tcl_file):
            wx.MessageBox(f"TCL file {tcl_file} already exists!", "Please confirm", 
                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.YES
            RedirectText(self.log).write(f"$ Openining the existing {tcl_file}!\n")
        else:
            import afgi.yaml_to_tcl.tcl_gen as TclGen
            TclGen.TclGen(script, tcl_file)
            RedirectText(self.log).write(f"$ Generating and opening {tcl_file}!\n")
        f = open(tcl_file, 'r')
        content = f.read()
        self.tab = MyPanel(self.nb, content)
        self.nb.AddPage(self.tab, tcl_file, True)
        f.close()
       
      
    def OnPageChanged(self, event):
          """ A method to handle the page changed event"""
          old = event.GetOldSelection()
          new = event.GetSelection()
          sel = self.nb.GetSelection()
        #   print ('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
          event.Skip()

    def OnPageChanging(self, event):
          """ A method to handle the page changing event"""
          old = event.GetOldSelection()
          new = event.GetSelection()
          sel = self.nb.GetSelection()
        #   print ('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
          event.Skip()
    # File menu item event handlers
    def MyFileDialog(self, text, style, mode):
        """ A method to create a file dialog box
        Args:
            text (str): text to be displayed in the status bar
            style (int): style of the file dialog box
            mode (str): set the file mode: read, write, append, etc.
        """
        dlg = wx.FileDialog(self, "Give a file name", self.dirname, self.filename, wildcard, style)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            if mode == "new":
                f = open(os.path.join(self.dirname, self.filename), 'w')
                self.tab = MyPanel(self.nb, "")
                self.nb.AddPage(self.tab, self.filename, True)
                self.PushStatusText(text)
                f.close()
            elif mode == "open":
                f = open(os.path.join(self.dirname, self.filename), 'r')
                content = f.read()
                self.tab = MyPanel(self.nb, content)
                self.nb.AddPage(self.tab, self.filename, True)
                f.close()
                self.PushStatusText(text)
            elif mode == "write":
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.nb.GetCurrentPage().text.GetValue())
                self.tab = MyPanel(self.nb, self.nb.GetCurrentPage().text.GetValue())
                self.nb.AddPage(self.tab, self.filename, True)
                f.close()
                self.PushStatusText(text)
            else:
                pass
        dlg.Destroy()

    def SaveCurrentFile(self):
        """ A method to display a message box to save the current file"""
        return wx.MessageBox("Do you want to save the file?", "Please confirm", 
                      wx.ICON_QUESTION | wx.YES_NO, self) == wx.YES
        
    def OnNew(self, event):
        """ A method to create a new file"""
        if self.nb.GetCurrentPage() is not None:
            if self.nb.GetCurrentPage().text.IsModified():
                if self.SaveCurrentFile():
                    self.OnSave(event)
        self.MyFileDialog("New file Created!", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "new")
      
    def OnOpen(self, event):
        """ A method to open a file"""
        if self.nb.GetCurrentPage() is not None: 
            if self.nb.GetCurrentPage().text.IsModified():
                if self.SaveCurrentFile():
                    self.OnSave(event)
        self.MyFileDialog("File opened!", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, "open")

    def OnSave(self, event):
        """ A method to handle the save event"""
        if self.nb.GetCurrentPage() is not None:
            if self.nb.GetCurrentPage().text.IsModified():
                index = self.nb.GetSelection()
                f = open(os.path.join(os.getcwd(), self.nb.GetPageText(index)), 'w')
                f.write(self.nb.GetCurrentPage().text.GetValue())
                self.nb_changed = False
                self.PushStatusText("File saved!")
                f.close()

    def OnSaveAs(self, event):
        """ A method to handle the "save as" event"""
        self.MyFileDialog("File saved!", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, "write")

    def OnExit(self, event):
        """ A method to handle the exit event"""
        self.Close(True)  # Close the frame.

    # edit menu item event handlers        
    def OnUndo(self, event):
        """ A method to handle the undo event"""
        self.nb.GetCurrentPage().text.Undo()

    def OnRedo(self, event):
        """ A method to handle the redo event"""
        self.nb.GetCurrentPage().text.Redo()

    def OnCut(self, event):
        """ A method to handle the cut event"""
        self.nb.GetCurrentPage().text.Cut()

    def OnCopy(self, event):
        """ A method to handle the copy event"""
        self.nb.GetCurrentPage().text.Copy()

    def OnPaste(self, event):
        """ A method to handle the paste event"""
        self.nb.GetCurrentPage().text.Paste()

    def OnDelete(self, event):
        """ A method to handle the delete event"""
        self.nb.GetCurrentPage().text.Clear()

    def OnSelectAll(self, event):
        """ A method to handle the select all event"""
        self.nb.GetCurrentPage().text.SelectAll()

    # Console menu item event handlers
    def OnClearConsole(self, event):
        """ A method to clear the console"""
        self.log.Clear()
    def OnCloseConsole(self, event):
        """ A method to close the console"""
        self.panel2.Destroy()

    # Help menu item event handlers
    def OnAbout(self, event):
        """ A method to display the about dialog box"""
        dlg = wx.MessageDialog( self, "AFGI: Augmented Formal Graphical Interface\nVersion 0.0.1", "About AFGI", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

