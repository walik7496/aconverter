# Download ffmpeg.exe!
import tkinter as tk
from tkinter import filedialog
import subprocess
from threading import Thread

class AudioConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Audio Converter")

        self.label = tk.Label(master, text="Select the input audio file and output format:")
        self.label.pack()

        self.input_button = tk.Button(master, text="Select input file", command=self.get_input_file)
        self.input_button.pack()

        self.format_label = tk.Label(master, text="Output audio format:")
        self.format_label.pack()

        self.format_entry = tk.Entry(master)
        self.format_entry.pack()

        self.progress = tk.DoubleVar()
        self.progress_bar = tk.Scale(master, variable=self.progress, orient="horizontal", from_=0, to=100, showvalue=False)
        self.progress_bar.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_audio)
        self.convert_button.pack()

        self.output = tk.Text(master, height=10, width=50)
        self.output.pack()

    def get_input_file(self):
        self.input_file = filedialog.askopenfilename()

    def convert_audio(self):
        output_format = self.format_entry.get()

        if not self.input_file:
            self.show_error_message("Please select an input audio file.")
            return

        if not output_format:
            self.show_error_message("Please enter the output audio format.")
            return

        input_filename = self.input_file.split('/')[-1].split('.')[0]
        output_file = f"{input_filename}_converted.{output_format}"

        ffmpeg_command = f'ffmpeg -i "{self.input_file}" -vn "{output_file}"'
        self.process = subprocess.Popen(ffmpeg_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)

        Thread(target=self.read_output).start()

    def read_output(self):
        while True:
            output = self.process.stderr.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                self.output.insert(tk.END, output.strip() + '\n')
                self.output.see(tk.END)

                if "Duration" in output:
                    duration = output.split("Duration: ")[1].split(",")[0]
                    duration_parts = duration.split(":")
                    total_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + float(duration_parts[2])
                elif "time=" in output:
                    time_position = output.split("time=")[1].split()[0]
                    time_position_parts = time_position.split(":")
                    current_seconds = int(time_position_parts[0]) * 3600 + int(time_position_parts[1]) * 60 + float(time_position_parts[2])
                    progress = (current_seconds / total_seconds) * 100
                    self.progress.set(progress)

    def show_error_message(self, message):
        error_message = tk.Toplevel(self.master)
        error_label = tk.Label(error_message, text=message)
        error_label.pack()
        ok_button = tk.Button(error_message, text="OK", command=error_message.destroy)
        ok_button.pack()

root = tk.Tk()
app = AudioConverterApp(root)
root.mainloop()
