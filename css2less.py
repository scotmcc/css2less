import sublime, sublime_plugin, subprocess
import sys

class CssToLessCommand(sublime_plugin.TextCommand):
    """
        This plugin assumes you have installed libcss2less
        which can be found here:
         - https://github.com/thomaspierson/libcss2less
         - http://rubydoc.info/gems/css2less/frames
    """
    def run(self, edit):
        self.fetch_position()
        self.convert_css(edit)
        self.reset_position()

    def fetch_position(self):
        self.curpos = self.view.viewport_position()
        self.selection = self.view.sel()[0]

    def convert_css(self, edit):
        region = sublime.Region(0, self.view.size())
        output = subprocess.check_output(["css2less", self.view.file_name()]).decode("utf-8")
        if len(output) == 1:
            print('Apparently there is no discernable CSS here...')
            return
        self.view.replace(edit, region, output)

    def reset_position(self):
        self.view.sel().clear()
        self.view.sel().add(self.selection)
        self.view.set_viewport_position(self.curpos, False)
