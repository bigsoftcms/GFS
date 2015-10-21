import pickle


class FilesTagsAssociation:

    def __init__(self):
        self._files = {}

    def serialize(self):
        return pickle.dumps(self._files)

    def deserialize(self, value):
        # FIXME Could expose to code injection: see http://docs.python.org/library/pickle.html
        data = pickle.loads(value)
        if isinstance(data, dict):
            self._files = value
        else:
            raise ValueError('Serialized data is not valid')

    def add_file(self, filename, tags = set()):
        if filename in self._files:
            raise ValueError('File name already exists within the namespace')

        self._files[filename] = tags

    def remove_file(self, filename):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        del self._files[filename]

    def assign_tag(self, filename, tag):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        self._files[filename].add(tag)

    def assign_tags(self, filename, tags):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        self._files[filename].update(tags)

    def discard_tag(self, filename, tag):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        self._files[filename].discard(tag)

    def discard_tags(self, filename, tags):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        self._files[filename].difference_update(tags)

    def has_tag(self, filename, tag):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        return tag in self._files[filename]

    def has_tags(self, filename, tags):
        if filename not in self._files:
            raise ValueError('File name doesn\'t exists within the namespace')

        return self._files[filename].issuperset(tags)

    def tagged_files(self, tags):
        lst = []
        for filename, filetags in self._files:
            if filetags.issuperset(tags):
                lst.append(filename)
        return lst

