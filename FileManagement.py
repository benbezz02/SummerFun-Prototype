
class FileManagement:

    def __init__(self, file):
        self.file = file

    def fileDelete(self):

        self.file = None

    def fileView(self):

        if self.file is None:
            print("No file to view.")
            return

        print(self.file)
