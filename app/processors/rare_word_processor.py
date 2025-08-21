class RareWordProcessor:
    def find_rare_word(self, text):
        words = text.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        rare_word = min(freq, key=freq.get) if freq else None
        return rare_word