"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...

    def __init__ (self, filename): 
        """Initializes word finder with a file"""
        self.filename = filename
        self.words = self.load_words()

    def load_words(self): 
        """Loads the words from the provided file and returns a list of words"""
        with open(self.filename, 'r') as file:
            words = [word.strip() for word in file]
        print(f"{len(words)} words read")
        return words
        
    def random(self): 
        """Return a random word from the loaded list of words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    
    def parse (self, dict_file): 
        valid_words = []
        for word in dict_file:
            word = word.strip()
            if word and not word.startswith("#"): 
                valid_words.append(word)
        return valid_words