
class Uci(object):
    def batch(self):
        raise NotImplementedError()

    def commit(self):
        raise NotImplementedError()

    def changes(self):
        raise NotImplementedError()

    def import_tree(self, tree, merge=False):
        raise NotImplementedError()

    def export_tree(self, tree):
        raise NotImplementedError()

    def add(self, config_type):
        raise NotImplementedError()

    def set(self, path, value):
        raise NotImplementedError()

    def get(self, path):
        raise NotImplementedError()

    def add_list(self, path, value):
        raise NotImplementedError()

    def del_list(self, path):
        raise NotImplementedError()

    def delete(self, path):
        raise NotImplementedError()

    def rename(self, path, name):
        raise NotImplementedError()

    def revert(self, path=""):
        raise NotImplementedError()

    def reorder(self, path, pos):
        raise NotImplementedError()

class UciCli(Uci):
    """
    use of Uci with a execute_call
    """
    def __init__(self, execute_call):
        """
        execute_call rtype [stdout, stderr]
        """
        self._exe = execute_call

    def batch(self):
        self._exe("uci batch")

    def commit(self):
        self._exe("uci commit")

    def changes(self):
        return self._exe("uci changes")

    def import_tree(self, tree, merge=False):
        raise NotImplementedError()

    def export_tree(self, tree):
        raise NotImplementedError()

    def add(self, config_type):
        raise NotImplementedError()

    def set(self, path, value):
        raise NotImplementedError()

    def get(self, path):
        raise NotImplementedError()

    def add_list(self, path, value):
        raise NotImplementedError()

    def del_list(self, path):
        raise NotImplementedError()

    def delete(self, path):
        raise NotImplementedError()

    def rename(self, path, name):
        raise NotImplementedError()

    def revert(self, path=""):
        raise NotImplementedError()

    def reorder(self, path, pos):
        raise NotImplementedError()
