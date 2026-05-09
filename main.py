import tkinter as tk
from tkinter import messagebox, font
from analyzer import LexicalAnalyzer


class LexicalGui:
    def __init__(self, root):
        self.analyzer = LexicalAnalyzer()
        self.root = root
        self.root.title("Rumeli Üniv. - Lexical Analyzer")
        self.root.geometry("500x350")
        self.root.configure(bg="#f4f7f6")  # Soft arka plan

        # Fontlar (Hocanın istediği Calibri tarzı)
        self.title_font = font.Font(family="Calibri", size=16, weight="bold")
        self.label_font = font.Font(family="Calibri", size=12)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    def setup_ui(self):
        # Başlık
        title_label = tk.Label(
            self.root,
            text="Sözcüksel Çözümleyici (Değişken Denetimi)",
            font=self.title_font, bg="#f4f7f6", fg="#2c3e50"
        )
        title_label.pack(pady=20)

        # Giriş Alanı Çerçevesi
        input_frame = tk.Frame(self.root, bg="#f4f7f6")
        input_frame.pack(pady=10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
