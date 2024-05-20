class State:
    id: int
    name: str
    tags: list[str]
    neighbours: list[dict]
    url: str

    def __init__(self, id, name, tags=None, neighbours=None, url=''):
        if neighbours is None:
            neighbours = dict()
        if tags is None:
            tags = []
        self.id = id
        self.name = name
        self.tags = tags
        self.neighbours = neighbours
        self.url = url

    def __repr__(self):
        return f"State id: {self.id}; Name: {self.name}; Tags: {self.tags}; Neighbours: {self.neighbours}"