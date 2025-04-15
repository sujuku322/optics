import customtkinter as ctk
from modules.convex_lens import simulate_convex_lens

# 在 self.button 裡加
self.button = ctk.CTkButton(self, text="模擬凸透鏡", command=simulate_and_plot_lens)

# 初始化 GUI
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class OpticsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("光學模擬工具")
        self.geometry("400x200")

        # 標題文字
        self.label = ctk.CTkLabel(self, text="凸透鏡模擬", font=("Arial", 20))
        self.label.pack(pady=20)

        # 模擬按鈕
        self.button = ctk.CTkButton(self, text="顯示模擬圖", command=self.run_simulation)
        self.button.pack(pady=10)

    def run_simulation(self):
        simulate_convex_lens()

# 執行程式
if __name__ == "__main__":
    app = OpticsApp()
    app.mainloop()
