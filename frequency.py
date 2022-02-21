

class WordsDict(dict):

    def fill_from_file(self, filename:str) -> None:
        if not isinstance(filename,str):
            raise TypeError("Bad type of filename")

        overall_length = 0

        with open(filename, 'r',encoding="utf-8") as f:
            for line in f.readlines():
                for word in line.strip().split():
                    for letter in word:
                        self[letter] = self.get(letter, 0) + 1
                        overall_length+=1
        
        for letter in self.keys():
            self[letter] = self[letter] / overall_length
        


def main():
    words = WordsDict()
    words.fill_from_file("words.txt")
    print(words)

    


if __name__ == "__main__":
    main()