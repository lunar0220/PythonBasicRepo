class FileManager:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def write(self, text: str) -> None:
        self.file.write(text)

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        if self.file:
            self.file.close()


with FileManager('test.txt') as fm:
    fm.write("Hello, World")