class LexicalAnalyzer:
    def __init__(self):
        self.keywords = [
            "int", "for", "while", "class", "return", "if", "else",
            "break", "continue", "def", "import", "from", "True", "False",
            "None", "and", "or", "not", "in", "is", "try", "except",
            "finally", "with", "as", "pass", "raise", "del", "global", "lambda"
        ]

    def is_letter(self, char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def is_digit(self, char):
        return '0' <= char <= '9'

    def is_underscore(self, char):
        return char == '_'

    def is_space(self, char):
        return char == ' '

    def check_variable(self, s):
        if not s:
            return False, "Input boş olamaz."

        if s in self.keywords:
            return False, f"'{s}' bir anahtar kelimedir, değişken olamaz."

        if not self.is_letter(s[0]):
            return False, "Değişken ismi harf ile başlamalıdır."

        for char in s:
            if self.is_space(char):
                return False, "Değişken ismi boşluk içeremez."
            if not (self.is_letter(char) or self.is_digit(char) or self.is_underscore(char)):
                return False, f"'{char}' geçersiz bir karakterdir. Özel karakter kullanılamaz."

        return True, "Geçerli bir değişken ismidir."