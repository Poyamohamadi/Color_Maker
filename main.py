import customtkinter as ctk 

class MyApp(ctk.CTk):
    def __init__(self):
        super(MyApp,self).__init__()
        # Define window
        self.title('Color Maker')
        self.geometry('520x520')
        self.resizable(0,0)

        # Define layout
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(fill='both',expand=True, padx=5, pady=1)

        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.pack(fill='both',expand=True, padx=5, pady=1.5)

        # Create widjets for Input frame:
            # R 
        red_label = ctk.CTkLabel(self.input_frame, text="R")
        red_label.grid(row=0, column=0, sticky='n')
        self.red_slider = ctk.CTkSlider(self.input_frame, from_=0, to=255,orientation='vertical',command=self.get_red)
        self.red_slider.grid(row=1, column=0, sticky='n')
        # Red
        red_button = ctk.CTkButton(self.input_frame, text="Red",width=100,command=lambda:self.set_color(255,0,0))
        red_button.grid(row=2, column=0, padx=1, pady=1)
            # G
        green_label = ctk.CTkLabel(self.input_frame, text="G")
        green_label.grid(row=0, column=1, sticky='n')
        self.green_slider = ctk.CTkSlider(self.input_frame, from_=0, to=255,orientation='vertical',command=self.get_green)
        self.green_slider.grid(row=1, column=1, sticky='n')
        # Green
        green_button = ctk.CTkButton(self.input_frame, text="Green",width=100,command=lambda:self.set_color(0,255,0))
        green_button.grid(row=2, column=1, padx=1, pady=1)
            # B
        blue_label = ctk.CTkLabel(self.input_frame, text="B")
        blue_label.grid(row=0, column=2, sticky='n')
        self.blue_slider = ctk.CTkSlider(self.input_frame, from_=0, to=255,orientation='vertical',command=self.get_blue)
        self.blue_slider.grid(row=1, column=2, sticky='n')
        # Blue 
        blue_button = ctk.CTkButton(self.input_frame, text="Blue",width=100,command=lambda:self.set_color(0,0,255))
        blue_button.grid(row=2, column=2, padx=1, pady=1)
        # Yellow
        yellow_button = ctk.CTkButton(self.input_frame, text="Yellow",width=100,command=lambda:self.set_color(255,255,0))
        yellow_button.grid(row=3, column=0, padx=1, pady=1)
        # Cyan
        cyan_button = ctk.CTkButton(self.input_frame, text="Cyan",width=100,command=lambda:self.set_color(0,255,255))
        cyan_button.grid(row=3, column=1, padx=1, pady=1)
        # Magenta
        magenta_button = ctk.CTkButton(self.input_frame, text="Magenta",width=100,command=lambda:self.set_color(255,0,255))
        magenta_button.grid(row=3, column=2, padx=1, pady=1)
        
        store_button = ctk.CTkButton(self.input_frame, text="Store Color",command=self.store_color)
        store_button.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky="we")

        color_box = ctk.CTkLabel(self.input_frame, bg_color='black', height=100, width=100,text='')
        color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
        self.color_tuple = ctk.CTkLabel(self.input_frame, text='(0), (0), (0)')
        self.color_tuple.grid(row=2, column=3, columnspan=2)
        self.color_hex = ctk.CTkLabel(self.input_frame, text='#000000')
        self.color_hex.grid(row=3, column=3, columnspan=2)
        save_button = ctk.CTkButton(self.input_frame, text="Save",width=100,command=self.save_colors)
        save_button.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
        quit_button = ctk.CTkButton(self.input_frame, text="Quit",width=100,command=self.destroy)
        quit_button.grid(row=4, column=4, padx=1, pady=1, sticky="WE")

        # Create widjets for Output frame:
        self.stored_colors = {}
        self.stored_color = ctk.IntVar()
        for row in range(6):
            radio = ctk.CTkRadioButton(self.output_frame,text='',variable=self.stored_color, value=row,
            width=1)
            radio.grid(row=row, column=0, sticky='w')

            recall_button = ctk.CTkButton(self.output_frame, text="Recall Color", state='bisabled')
            recall_button.grid(row=row, column=1, padx=10,pady=2)

            new_color_tuple = ctk.CTkLabel(self.output_frame, text="(255), (255), (255)")
            new_color_tuple.grid(row=row, column=2, padx=20)

            new_color_hex = ctk.CTkLabel(self.output_frame, text="#ffffff",anchor='w')
            new_color_hex.grid(row=row, column=3,ipadx=10, padx=25,sticky='nsew')

            new_color_black_box = ctk.CTkLabel(self.output_frame, bg_color="black", width=60, height=10,text='')
            new_color_black_box.grid(row=row, column=4, pady=2, ipadx=5, ipady=5,sticky='w')

            new_color_box = ctk.CTkLabel(self.output_frame, bg_color='white', width=60, height=10,text='')
            new_color_box.grid(row=row, column=4,padx=3,sticky='w')

            self.stored_colors[self.stored_color.get()] = [new_color_tuple.cget('text'),new_color_hex.cget('text')]
        
        self.red_slider.set(0)
        self.green_slider.set(0)
        self.blue_slider.set(0)

        self.red_value = "00"
        self.green_value = "00"
        self.blue_value = "00"

        #Run the window's main loop
        self.mainloop()
    
    def update_color(self):
        color_box = ctk.CTkLabel(self.input_frame,text='',bg_color="#" + self.red_value + self.green_value + self.blue_value, height=100, width=100)
        color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10)

        self.color_tuple.configure(text=f'({self.red_slider.get():.2f}),' + f'({self.green_slider.get():.2f}),' + f'({self.blue_slider.get():.2f})')
        self.color_hex.configure(text="#" + self.red_value + self.green_value + self.blue_value)

    
    def get_red(self,slider_value):
        self.red_value = hex(int(slider_value))
        self.red_value = self.red_value.lstrip("0x")
        while len(self.red_value) < 2:
            self.red_value = "0" + str(self.red_value)
        self.update_color()

    def get_green(self,slider_value):
        self.green_value = hex(int(slider_value))
        self.green_value = self.green_value.lstrip("0x")
        while len(self.green_value) < 2:
            self.green_value = "0" + str(self.green_value)
        self.update_color()

    def get_blue(self,slider_value):
        self.blue_value = hex(int(slider_value))
        self.blue_value = self.blue_value.lstrip("0x")
        while len(self.blue_value) < 2:
            self.blue_value = "0" + str(self.blue_value)
        self.update_color()
    
    def set_color(self,r,g,b):
        self.red_slider.set(r);self.get_red(r)
        self.green_slider.set(g);self.get_green(g)
        self.blue_slider.set(b);self.get_blue(b)
    
    def store_color(self):
        red = str(self.red_slider.get())
        while len(red) < 3:
            red = "0" + red
        green = str(self.green_slider.get())
        while len(green) < 3:
            green = "0" + green
        blue = str(self.blue_slider.get())
        while len(blue) < 3:
            blue = "0" + blue
        
        stored_red = self.red_slider.get()
        stored_green = self.green_slider.get()
        stored_blue = self.blue_slider.get()

        recall_button = ctk.CTkButton(self.output_frame, text="Recall Color",command=lambda:self.set_color(stored_red, stored_green, stored_blue))
        recall_button.grid(row=self.stored_color.get(), column=1, padx=10,pady=2)

        new_color_tuple = ctk.CTkLabel(self.output_frame, text='('+ red[0:3] +'), ' + '('+ green[0:3] +'), ' + '('+ blue[0:3] +')')
        new_color_tuple.grid(row=self.stored_color.get(), column=2, padx=20)

        new_color_hex = ctk.CTkLabel(self.output_frame, text='#' + self.red_value + self.green_value +self.blue_value,anchor='w')
        new_color_hex.grid(row=self.stored_color.get(), column=3,ipadx=1, padx=25,sticky='nsew')

        new_color_black_box = ctk.CTkLabel(self.output_frame, bg_color='black', width=60, height=10,text='')
        new_color_black_box.grid(row=self.stored_color.get(), column=4, pady=2, ipadx=5, ipady=5,sticky='w')
        
        new_color_box = ctk.CTkLabel(self.output_frame, bg_color="#"+ self.red_value + self.green_value + self.blue_value, width=60, height=10, text='')
        new_color_box.grid(row=self.stored_color.get(), column=4,padx=3,sticky='w')

        self.stored_colors[self.stored_color.get()] = [new_color_tuple.cget("text"),new_color_hex.cget("text")]
        if self.stored_color.get() < 5:
            self.stored_color.set(self.stored_color.get() + 1)

    def save_colors(self):
        file_name = ctk.filedialog.asksaveasfilename(initialdir='./', title='Save Colors', filetypes=(('Text', '.txt'),('All Files', '*.*')))
        with open(file_name, "w") as f:
            f.write("Color Maker:\n")
            for saved_entry in self.stored_colors.values():
                f.write(saved_entry[0] + "\n" + saved_entry[1] + "\n\n")

if __name__ == "__main__":
    MyApp()