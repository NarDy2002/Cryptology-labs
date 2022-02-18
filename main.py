
class WordsDict(dict):

    def fill_from_file(self, filename:str) -> None:
        if not isinstance(filename,str):
            raise TypeError("Bad type of filename")

        with open(filename, 'r') as f:
            for line in f.readlines():
                for word in line.strip().split():
                    self[word] = self.get(word, 0) + 1

    def get_list_of_sorted_by_alphabet(self, asc: bool = True) -> list:
        return sorted(self.items(),reverse= asc)

    def get_list_of_sorted_by_occurence(self,asc: bool = True) -> list:
        return sorted(self.items(), key = lambda x:x[1], reverse= asc)




def main():
    words = WordsDict()
    words.fill_from_file("words.txt")
    print(words.get_list_of_sorted_by_occurence(asc=False))



if __name__ == "__main__":
    main()