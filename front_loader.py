import tkinter as tk
import threading
import time

class LoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading...")
        self.root.geometry("300x120")

        self.progress_label = tk.Label(self.root, text="Aguarde o carregamento dos dados:")
        self.progress_label.pack()

        self.percent_label = tk.Label(self.root, text="0")
        self.percent_label.pack()

        self.canvas = tk.Canvas(self.root, bg="lightgray", width=300, height=20)
        self.canvas.pack(padx=5, pady=5)

        self.close_button = tk.Button(self.root, text="Concluir", state="disabled")
        self.close_button.pack(pady=5)

        self.running = False
        self.start_loading()

    def start_loading(self):
        if not self.running:
            self.running = True
            self.load_thread = threading.Thread(target=self.load_file)
            self.load_thread.start()

    def load_file(self):
        while self.running:
            try:
                with open("front_loader.txt", "r") as file:
                    percentage = int(file.read().strip())
                    print(percentage)
                    self.percent_label.config(text=percentage)
                    self.canvas.create_rectangle(0, 0, percentage * 3, 20, fill="lightblue", tags="progress")
                    if percentage == 100:
                        self.running = False
                        self.progress_label.config(text="Dados carregados com sucesso!")
                        self.close_button.config(state="normal")
                        break
            except FileNotFoundError:
                print("Arquivo 'loader.txt' não encontrado.")
            except ValueError:
                print("Valor inválido encontrado no arquivo 'loader.txt'.")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoaderApp(root)
    root.mainloop()

