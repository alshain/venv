import sys

class vEnv(object):
    def __init__(self):
        self._mappings = []

    def map(self, virtual, actual):
        """Redirect a module import."""
        self._mappings.insert(0, (virtual, actual))
        self._sort()

    def _sort(self):
        """
        Sort mappings by length of virtual, descending.
        
        Mappings must be ordered in this fastion because
        we want the best match (most identifiers)
        to be used.
        
        Consider these mappings:
        
        plugins.johndoe.database -> johndoe
        plugins -> plugins
        
        Python code:
        import plugins.johndoe.database
        
        If it was odered the other way around,
        the import would be redirected to plugins
        which is clearly not the goal here.
        Hence we sort by the length, descending
        of the virtual module path.
        
        """
        get_key = lambda map: len(map[0])
        return sorted(self._mappings, key = get_key, reverse = True)

    def find_module(self, module_name, package_path):
        """PEP 302: Module Loader"""
        for virtual, actual in self._mappings:
            if module_name.startswith(virtual):
                print module_name
                print package_path
                return self
        return

    def load_module(self, fullname):
        print "Attempting to load: %s" % fullname
        pass



vEnv = vEnv()


def map(virtual, actual):
    """Redirect import."""
    vEnv.map(virtual, actual)

sys.meta_path.insert(0, vEnv)
