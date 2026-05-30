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

        self.setup_ui()

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

        tk.Label(input_frame, text="Değişken İsmini Girin:", font=self.label_font, bg="#f4f7f6").pack()

        self.entry = tk.Entry(
            input_frame, font=("Calibri", 13), width=30,
            relief="flat", highlightthickness=1, highlightbackground="#bdc3c7"
        )
        self.entry.pack(pady=10, ipady=5)

        # Analiz Butonu
        self.btn_analyze = tk.Button(
            self.root, text="ANALYZE", command=self.handle_analysis,
            bg="#3498db", fg="white", font=("Calibri", 11, "bold"),
            width=15, relief="flat", cursor="hand2", activebackground="#2980b9"
        )
        self.btn_analyze.pack(pady=20)

        # Alt Bilgi (Hocanın istediği Ad-Soyad görünürlüğü)
        footer = tk.Label(
            self.root, text="HAMIDREZA TOUTOUNCHI- BLG306 Projesi",
            font=("Calibri", 9), bg="#f4f7f6", fg="#95a5a6"
        )
        footer.pack(side="bottom", pady=10)

    def handle_analysis(self):
        val = self.entry.get().strip()
        is_valid, msg = self.analyzer.check_variable(val)

        if is_valid:
            messagebox.showinfo("Sonuç", f"✅ {msg}")
        else:
            messagebox.showerror("Hata", f"❌ {msg}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalGui(root)
    root.mainloop()