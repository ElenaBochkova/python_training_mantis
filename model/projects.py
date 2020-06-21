from sys import maxsize

class Project:

    def __init__(self, name=None, id=None, description=None, status=None):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.status}:{self.description}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and (
            self.description == other.description)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize