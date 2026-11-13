class Bid:
    __slots__ = ('text', 'content', 'status_history')

    def __init__(self, text: str, content: dict[str, str], status_history: dict[str, int]):
        self.text = text
        self.content = content
        self.status_history = status_history

    @property
    def status(self) -> int:
        return list(self.status_history.values())[-1]
