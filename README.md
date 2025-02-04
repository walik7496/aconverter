# Audio Converter App

A simple graphical user interface (GUI) to convert audio files to different formats using `ffmpeg`. This app allows users to select an audio file, specify the desired output format, and track the conversion progress.

## Features

- **Input File Selection**: Choose an audio file using a file dialog.
- **Output Format**: Specify the output audio format (e.g., `.mp3`, `.wav`).
- **Conversion Progress**: View the conversion progress with a progress bar.
- **Error Handling**: Displays error messages if the input file or format is not provided.

## Requirements

- **Python 3.x** (Tested on Python 3.7+)
- **FFmpeg**: Ensure `ffmpeg` is installed and available in your system's PATH. You can download it from [here](https://ffmpeg.org/download.html).

## Installation

1. Install Python 3.x: [Download Python](https://www.python.org/downloads/)
2. Install the required Python libraries using `pip`:

   ```bash
   pip install tkinter
   ```

## Download ffmpeg.exe

Download `ffmpeg.exe` from [FFmpeg Official Website](https://ffmpeg.org/download.html) and make sure it is accessible via your system's PATH. You can also place the `ffmpeg.exe` file in the same directory as this script.

## Usage

1. Run the `audio_converter.py` script.
2. In the GUI, click **Select input file** to choose an audio file.
3. Enter the desired output audio format (e.g., `.mp3`, `.wav`) in the **Output audio format** field.
4. Click **Convert** to start the conversion process.
5. The progress bar will update in real-time as the conversion takes place.
6. If the conversion encounters an issue, an error message will pop up with instructions on how to fix it.

## Code Explanation

- **File Dialog**: Used to select the input audio file.
- **Progress Bar**: Displays the conversion progress by reading the output from the `ffmpeg` command.
- **FFmpeg**: Handles the actual audio conversion process. The app calls `ffmpeg` with the selected input file and desired output format.
- **Error Handling**: Provides error messages if required fields (input file or output format) are not specified.

## Troubleshooting

- **Missing `ffmpeg`**: If `ffmpeg` is not installed or not accessible from the command line, you will see an error. Ensure `ffmpeg` is installed and added to your system's PATH.
- **Unsupported Formats**: If the selected audio format is not supported, you will receive an error message. Ensure the format you enter is a valid audio format (e.g., `.mp3`, `.wav`).
- **Progress Bar Not Updating**: Ensure that `ffmpeg` is outputting the progress information correctly. If the progress bar isn't updating, make sure your version of `ffmpeg` supports real-time conversion monitoring.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

If you have any questions or need further assistance, feel free to open an issue or reach out directly to the repository owner.
