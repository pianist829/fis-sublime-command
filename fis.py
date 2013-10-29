import sublime, sublime_plugin, os

s = None
workDir = None

def plugin_loaded():
	global s
	s = sublime.load_settings("fis.sublime-settings")

# 
def is_fis_buffer(view):
	global workDir 
	fName = view.file_name();  
	isFisFile = False; 
	whileFlag = True;
	path = os.path.dirname(fName);
	while not isFisFile and whileFlag:
		tmp = path;
		fisConfPath = path + "/fis-conf.js";
		isFisFile = os.path.exists(fisConfPath); 
		path = os.path.dirname(path);
		workDir = tmp
		if tmp == path : 
			whileFlag = False;
			
	if isFisFile :  
		print fName + " is fis project file!"
	else :
		print fName + " is not fis project file!"

	return isFisFile; 
	   
plugin_loaded();

class AfterSaveFormatListner(sublime_plugin.EventListener):
	"""Event listener to run fis-release during the presave event"""
	def on_post_save(self, view):
		if(s.get("fis_on_save") == True and is_fis_buffer(view)):
			view.run_command("fis")

class FisCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cmd = s.get('cmd');
		print cmd;
		if workDir == None:
			is_fis_buffer(self.view)
			
		if sublime.platform() == 'windows':
			cmd.insert(0, '/c')
			cmd.insert(0, 'cmd.exe')

		self.view.window().run_command("exec", {"cmd" : cmd, "working_dir" :workDir});

	def is_visible(self):
		return is_fis_buffer(self.view)