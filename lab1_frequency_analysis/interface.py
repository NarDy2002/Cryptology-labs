import json

class WordsDict(dict):  

    def fill_from_file(self, filename:str) -> None:
        if not isinstance(filename,str):
            raise TypeError("Bad type of filename")

        with open(filename, 'r',encoding="utf-8") as f:
            text = f.read()
            self.fill_from_str(text)


    def fill_from_str(self, text:str) -> None:
    
        self.clear()
        overall_length = 0
        
        for word in text.split():
            for letter in word:
                if letter.isalpha:
                    self[letter] = self.get(letter, 0) + 1
                    overall_length+=1

        for letter in self.keys():
            self[letter] = self[letter] / overall_length   

    def write_to_file(self,filename:str) -> None:
        if not isinstance(filename,str):
            raise TypeError("Bad type of filename")

        with open(filename, 'w' ,encoding="utf-8") as f:
            json.dump(self, f, indent = 2) 


def main():
    words = WordsDict()
    words.fill_from_file("words.txt")
    print(words)
    words.write_to_file("frequency_dict.json")
    


if __name__ == "__main__":
    main()