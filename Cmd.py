import os, sublime, sublime_plugin

class ProjectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path, _ = os.path.split(sublime.active_window().project_file_name())
        #os.chdir(path)
        command= "start conemu.exe /Single /Dir "+path+" /cmdlist cmd -new_console:t:\""+path+"\""
        os.system(command)
        

class HereCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path, _ = os.path.split(self.view.file_name())
        # os.chdir(path)
        command= "start conemu.exe /Single /Dir "+path+" /cmdlist cmd -new_console:t:\""+path+"\""
        os.system(command)