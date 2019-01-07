import sublime
import sublime_plugin
from collections import OrderedDict


class RemoveDuplicateCharactersCommand(sublime_plugin.TextCommand):
    
    def ReplaceAll(edit, view, exp, tar):
        regions = view.find_all(exp)
        regions.reverse()
        for region in regions:
            view.replace(edit, region, tar)
            
    def run(self, edit):
        view = self.view
        all_sel_empty = True
        for sel in view.sel():
            if sel.empty():
                continue
            all_sel_empty = False
            self.remove_chars(edit, sel)
        if all_sel_empty:
            self.remove_chars(edit, sublime.Region(0, view.size()))
            
    def remove_chars(self, edit, region):
        view = self.view
        content = "".join(OrderedDict.fromkeys(view.substr(region)))
        view.replace(edit, region, content)
