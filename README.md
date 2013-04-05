#EditREPL
EditREPL is a port of Giles Bowkett's
[InteractiveEditor](http://utilitybelt.rubyforge.org/svn/lib/utility_belt/interactive_editor.rb)
component from his ruby gem [Utility Belt](http://utilitybelt.rubyforge.org/).

EditREPL allows you to run a terminal based editor inside your REPL session to
interactively edit code.

![video preview](https://raw.github.com/philipbjorge/EditREPL/master/preview.gif)

[Video](http://ascii.io/a/2496)

##Installation
Installation is easy using either pip or easy_install.

    easy_install EditREPL
    pip install EditREPL

##Supported Environments
EditREPL is Python2 and Python3 compatible with the default interactive shell.

##Basic Usage
To include it in your session, import the module and call the editor function:

    import editrepl
    vim()

After you save, the buffer will be executed in the current REPL context.

##Advanced Usage
###Can I edit any file?
Yes, just call the editor function with the filename you want to edit.

    vim("myfile.py")

###How does EditREPL choose your editor?
By default it uses the editor defined as your EDITOR environment variable, but
if that isn't defined it tries the following editors in order:

    ["vim", "vi", "emacs", "nano", "pico", "ed"]

###Can I change my editor?
To manually set your editor after initialization, supply the name or full path
to the executable as follows:

    ER.editor = "cli-textmate"

This will create a binding to the function cli-textmate for you to call.

###What REPLs does it work with?
Only the default python interpreter. iPython and bPython are confirmed to not work.

##How does it work?
Check out the literate code [here](http://htmlpreview.github.com/?https://github.com/philipbjorge/EditREPL/blob/master/docs/doc.html) or 
clone the repo and checkout out the docs folder.

##Etc
By [Philip Bjorge](http://philipbjorge.com)

**Contributors**

* rpk512

Released under BSD License

https://github.com/philipbjorge/EditREPL
