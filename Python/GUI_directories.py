import wx
import sys
import io

from folder_sorter import sort_files_by_year

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 500))

        # Panel and Layout
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Directory 1 Input
        self.dir1_label = wx.StaticText(panel, label="Directory 1:")
        self.dir1_text = wx.TextCtrl(panel, size=(400, 30))
        vbox.Add(self.dir1_label, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(self.dir1_text, flag=wx.EXPAND | wx.ALL, border=10)

        # Directory 2 Input
        self.dir2_label = wx.StaticText(panel, label="Directory 2:")
        self.dir2_text = wx.TextCtrl(panel, size=(400, 30))
        vbox.Add(self.dir2_label, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(self.dir2_text, flag=wx.EXPAND | wx.ALL, border=10)

        # Output Text Box
        self.output_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(400, 150))
        vbox.Add(self.output_text, flag=wx.EXPAND | wx.ALL, border=10)

        # Button to Trigger Processing
        self.process_button = wx.Button(panel, label="Process")
        vbox.Add(self.process_button, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        # Event binding
        self.process_button.Bind(wx.EVT_BUTTON, self.on_process)

        # Redirect stdout to the output text box
        self.old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.Show()

    def on_process(self, event):
        # Get the directory paths from the text boxes
        dir1 = self.dir1_text.GetValue()
        dir2 = self.dir2_text.GetValue()

        # Convert to raw string if needed (just in case)
        dir1 = dir1.replace("\\", "/")  # Optionally replace backslashes with forward slashes
        dir2 = dir2.replace("\\", "/")  # Same for second directory path

        # Call the imported function from 'other_module.py'
        sort_files_by_year(dir1, dir2)

        # Redirect print output to the text box
        output = sys.stdout.getvalue()
        self.output_text.SetValue(output)

        # Reset the stdout back to normal
        sys.stdout = self.old_stdout

# Run the app
app = wx.App(False)
frame = MyFrame(None, title="Directory Paths GUI")
app.MainLoop()