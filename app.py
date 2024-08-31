from tkinter import *# Ensure PIL is imported for handling images
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # Create database and API objects
        self.dbo = Database()
        self.apio = API()

        # Initialize the main window
        self.root = Tk()
        self.root.title('NLPApp')
        self.set_icon('resources/apple-icon.png')  # Set the window icon using the corrected method
        self.root.geometry('350x600')
        self.root.configure(bg='pink')

        # Load the login GUI
        self.login_gui()

        # Start the main event loop
        self.root.mainloop()

    def set_icon(self, file_path):
        """Sets the window icon from a PNG file."""
        try:
            img = Image.open(file_path)  # Open the PNG file
            photo = ImageTk.PhotoImage(img)  # Convert it to a Tkinter-compatible photo image
            self.root.iconphoto(False, photo)  # Set the iconphoto using the converted image
        except Exception as e:
            print(f"Failed to set icon: {e}")  # Print error if the icon cannot be set

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # Clear the existing GUI
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perform_registration(self):
        # Fetch data from the GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text='Welcome to NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=2, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=2, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=2, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        # Add GUI components for sentiment analysis
        pass

    def ner_gui(self):
        # Add GUI components for named entity recognition
        pass

    def emotion_gui(self):
        # Add GUI components for emotion prediction
        pass

# Initialize the app
nlp = NLPApp()
