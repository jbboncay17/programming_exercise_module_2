class GWAof20Students:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_highest(self):
        highest_name = ""
        highest_gwa = float('inf')

        with open(self.file_name, 'r') as file:
            for line in file:
                name, gwa = line.strip().split(',')
                gwa = float(gwa)

                if gwa < highest_gwa:
                    highest_gwa = gwa
                    highest_name = name

        return highest_name, highest_gwa

