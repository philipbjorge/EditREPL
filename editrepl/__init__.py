class EditREPL(object):
    # imports are being done inside the class to avoid polluting the global
    # namespace any more then necessary.
    import os

    _editor = None
    _tmp_file = None
    _candidates = ["vim", "vi", "emacs", "nano", "pico", "ed"]

    def __init__(self, default_editor=os.environ.get('EDITOR')):
        import tempfile
        self._editor = default_editor or self._determine_editor()
        self._tmp_file = tempfile.NamedTemporaryFile(suffix=".py")

    def install_hooks(self, old_editor=None):
        import inspect

        # Grab the outermost stack frame so we have the REPL's scope
        # This trickery needs to be done because using globals()/locals()
        # as default arguments meant they only get executed once on function
        # definition. We need it updated on each invocation.
        outermost_frame = inspect.getouterframes(inspect.currentframe())[-1][0]

        # Unbind the old editor method
        if old_editor:
            if old_editor in outermost_frame.f_locals:
                del outermost_frame.f_locals[old_editor]
            if old_editor in outermost_frame.f_globals:
                del outermost_frame.f_globals[old_editor]

        # Bind the new editor method
        print("Binding editor to %s." % ER.editor)
        outermost_frame.f_locals[ER.editor] = ER.exec_editor
        outermost_frame.f_globals[ER.editor] = ER.exec_editor

    def exec_editor(self, f=None):
        if f is None:
            f = self._tmp_file.name

        import subprocess
        # make sure you use self._editor because self.editor removes any path information.
        subprocess.call([self._editor, f])

        # reload repl using the outermost stack frame as its environment.
        import inspect
        outermost_frame = inspect.getouterframes(inspect.currentframe())[-1][0]
        exec(compile(open(f).read(), f, 'exec'),
                 outermost_frame.f_globals, outermost_frame.f_locals)

    def _determine_editor(self):
        # return the first editor from our candidates list that exists.
        from distutils.spawn import find_executable
        for e in self._candidates:
            if find_executable(e):
                return find_executable(e)

    @property
    def editor(self):
        # returns the editor with preceding path removed.
        from os.path import split
        return split(self._editor)[1]

    @editor.setter
    def editor(self, value):
        old_editor = self.editor
        self._editor = value
        self.install_hooks(old_editor)


ER = EditREPL()
ER.install_hooks()
