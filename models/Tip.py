class Tip:
    def __init__(self, text, date, tags=None):
        self.mark = -1
        self.text = text
        self.date = date
        if tags:
            self.tags = tags
        else:
            self.tags = []
