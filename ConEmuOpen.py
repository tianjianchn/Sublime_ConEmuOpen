import os, sublime, sublime_plugin

class ConEmuOpenCommand():
    def get_project(self):
        if self.window.project_file_name(): # try project file name first
            project_dir, project_name = os.path.split(self.window.project_file_name())
            project_name, ext = os.path.splitext('st:' + project_name)
            project_dir = self.window.folders()[0]
        elif self.window.folders(): # if no project, use the top folder
            project_dir = self.window.folders()[0]
            project_name = project_dir
        elif self.window.active_view().file_name(): # if no folder, use current file's folder
            project_dir, _ = os.path.split(self.window.active_view().file_name())
            project_name = project_dir
        else: #then exit
            return (None, None)
        return (project_name, project_dir)

    def open_conemu(self, dirname, title):
        command= "start conemu.exe /Single /Dir "+dirname+" /cmdlist cmd -new_console:t:\""+title+"\""
        os.system(command)
        
# open project folder
class ProjectCommand(sublime_plugin.WindowCommand, ConEmuOpenCommand):
    def run(self):
        project_name, project_dir = self.get_project()
        if not project_name:
            return
            
        self.open_conemu(project_dir, project_name)
        
# open "here" folder
class HereCommand(sublime_plugin.WindowCommand, ConEmuOpenCommand):
    def run(self, paths=[]):
        project_name, project_dir = self.get_project()
        if not project_name:
            return
        
        if paths:
            heredir = paths[0]
            if os.path.isfile(heredir):
                heredir = os.path.dirname(heredir)
        elif self.window.active_view().file_name(): 
            heredir, _ = os.path.split(self.window.active_view().file_name())
        else: # if no active file open, then try to open project folder
            heredir = project_dir
        
        # get the relative path from the project dir
        rel_path = os.path.relpath(heredir, project_dir)
        if rel_path == '.':
            title = project_name
        else: 
            title = project_name + ': ' + rel_path
        
        self.open_conemu(heredir, title)