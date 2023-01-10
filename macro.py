import customtkinter as ctk
import macro_fonction as mf


class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.title("Easy Macro")
        self.geometry(f"{720}x{480}")
        self.minsize(480, 320)
        self.maxsize(1080, 720)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.title_frame = TitleFrame(master=self)
        self.title_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="nsew")



    def play(self):
        pass

    def create(self):
        pass

    def register(self):
        pass


class TitleFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(TitleFrame, self).__init__(*args, **kwargs)

        self.title_label = ctk.CTkLabel(self, text="Easy Macro", font=("Courrier", 40))
        self.title_label.pack(expand=True)


class ButtonFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(ButtonFrame, self).__init__(*args, **kwargs)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.play_button = ctk.CTkButton(self, text="Play Macro", font=("Courrier", 20), command=self.master.play)
        self.play_button.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        self.create_button = ctk.CTkButton(self, text="Create Macro", font=("Courrier", 20),
                                           command=self.master.create)
        self.create_button.grid(row=0, column=1, padx=(10, 20), pady=(20, 10), sticky="nsew")

        self.register_button = ctk.CTkButton(self, text="Register Macro", font=("Courrier", 20),
                                             command=self.master.register)
        self.register_button.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()