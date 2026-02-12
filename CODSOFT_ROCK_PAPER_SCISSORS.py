import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, root):
        self.score = None
        self.result = None
        self.c_disp = None
        self.u_disp = None
        self.root = root
        self.root.title("🎮 Rock Paper Scissors")
        self.root.geometry("450x550")
        self.root.configure(bg='#f0f0f0')

        self.user = 0
        self.comp = 0
        self.draws = 0
        self.choices = {1: "🪨 Rock", 2: "📄 Paper", 3: "✂️ Scissors"}
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="🎮 Rock Paper Scissors 🎮",
                 font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=10)

        self.score = tk.Label(self.root,
                 text=f" 🏆 You {self.user} | 💻 Comp {self.comp} | 🤝 Draws {self.draws}",
                 font= ('Arial', 12), bg='#f0f0f0')
        self.score.pack(pady=10)

        f = tk.Frame(self.root, bg='#f0f0f0')
        f.pack(pady=20)
        colors = ['#3498db', '#2ecc71', '#e74c3c']

        for i, (choice, emoji) in enumerate([(1, "🪨"), (2, "📄"), (3, "✂️")]):
            tk.Button(f, text=emoji, font=('Arial', 14, 'bold'), width=8, height=2,
                      bg=colors[i], fg='white', command=lambda x=choice: self.play(x)
                      ).grid(row=0, column=i, padx=8)

        tk.Label(self.root, text="YOU ⚔️v/s⚔️ COMP", font=('Arial', 16, 'bold'),
                 bg='#f0f0f0', fg='#9b59b6').pack(pady=15)

        df = tk.LabelFrame(self.root, text="Current Round", font=('Arial, 11'),
                           bg='#f0f0f0', fg='#34495e')
        df.pack(pady=15, padx=20, fill=tk.BOTH)

        self.u_disp =tk.Label(df, text="🙍You : Waiting...", font=('Arial,12'),
                              bg='white', relief=tk.SUNKEN, width=25)
        self.u_disp.pack(pady=10, padx=10)

        self.c_disp = tk.Label(df, text="💻Computer: Waiting...", font=('Arial, 12'),
                               bg='white', relief=tk.SUNKEN, width=25)
        self.c_disp.pack(pady=10, padx=10)

        self.result = tk.Label(self.root, text="🎯 Make Your Move.!",
                               font=('Arial', 14, 'bold'), bg='#f0f0f0', height=2)
        self.result.pack(pady=15)

        cf = tk.Frame(self.root, bg='#f0f0f0')
        cf.pack(pady=15)

        tk.Button(cf, text="🔄️ Reset", font=('Arial', 10), bg='#f39c12', fg='white',
                  command=self.reset_game).grid(row=0, column=0, padx=8)
        tk.Button(cf, text="❓ Rules", font=('Arial', 10), bg='#3498db', fg='white',
                  command=self.show_rules).grid(row=0, column=1, padx=8)
        tk.Button(cf, text="❌ Exit", font=('Arial', 10), bg='#e74c3c', fg='white',
                  command=self.root.quit).grid(row=0, column=2, padx=8)

    def play(self, user):
        comp= random.randint(1,3)
        self.u_disp.config(text=f"🙍 You: {self.choices[user]}")
        self.c_disp.config(text=f"💻 Computer: {self.choices[comp]}")

        if user == comp:
            r, col, e = " It's a DRAW! 🤝 ", "#f39c12", "🤝"
            self.draws += 1
        elif (user, comp) in [(1,3), (2,1), (3,2)]:
            r, col, e = "YOU WIN! 🎉", "#2ecc71", "🎉"
            self.user += 1
        else:
            r, col, e = " Computer Wins! 💀", "#e74c3c", "💀"
            self.comp += 1

        self.result.config(text=f"{e} {r}", fg=col)
        self.score.config(
            text=f"🏆 You {self.user} | 💻 Comp {self.comp} | 🤝 draws {self.draws}"
        )
        self.root.after(100, lambda: messagebox.showinfo("Result", f"{e}\n{r}"))

    def reset_game(self):
        self.user = 0
        self.comp = 0
        self.draws = 0
        self.score.config(text="f 🏆You 0 | 💻 Comp 0 | 🤝 Draws 0")
        self.u_disp.config(text=" You: Waiting...")
        self.c_disp.config(text=f" Computer: Waiting...")
        self.result.config(text=" 🎯 Make Your Move!", fg='black')
        messagebox.showinfo("🔁 Game Reset", "Score reset! Let's play! 🎮")

    def show_rules(self):
        messagebox.showinfo("📃 Rules", """ 📜 ROCK PAPER SCISSORS RULES 📜

🪨 Rock beats ✂️ Scissors
📄Paper beats 🪨 Rock 
✂️Scissors beats 📄 Paper

⚔️Same choice = 🤝 Draw!
🎯First to 5 wins is champion! 🏆""")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()