import click
import subprocess
import os
import random
import time
from colorama import Fore, Style, init
from obfuscator.python_ob import *
from obfuscator.c_obfuscator import process_file as c_process_file
from obfuscator.cpp_obfuscator import process_file as cpp_process_file
import tkinter as tk
from tkinter import scrolledtext
import requests
import random

# Initialize colorama with autoreset enabled
init(autoreset=True)

def display_banner():
    """Display a random ASCII banner"""
    banners = [
        Fore.YELLOW + r"""
   __              __     _____        __              
  /  )     /      / ')/    /  '       /  )    _/_      
 /   __ __/ _    /  //__,-/-,. . _   /   __.  /  __ __ 
(__/(_)(_/_</_  (__//_)(_/  (_/_/_)_(__/(_/|_<__(_)/ (_)_ver_1.0

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                                       
    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Under Implementation)
                    4. ⚙️ C++ (Under Implementation) 
                    5. 💎 Ruby (Coming Soon)
                    6. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Under Implementation)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                   
     """,
        Fore.CYAN + r"""
 _______  _____  ______  _______       _____  ______  _______ _     _ _______ _______ _______ _______  _____   ______
 |       |     | |     \ |______      |     | |_____] |______ |     | |______ |       |_____|    |    |     | |_____/ 
 |_____  |_____| |_____/ |______      |_____| |_____] |       |_____| ______| |_____  |     |    |    |_____| |    \_ ver_1.0

══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Under Implementation)
                    4. ⚙️ C++ (Under Implementation) 
                    5. 💎 Ruby (Coming Soon)
                    6. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Under Implementation)

══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                                                                                                                 
    """,
        Fore.RED + r"""
                                           
 .-     .      .-..  .--     .-    .       
(  .-..-| .-,  | ||-.|-. ..-(  .-.-|-.-..-.
 `-`-'`-'-`'-  `-'`-'' '-'-' `-`-`-'-`-''  _ver_1.0

~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~

    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Under Implementation)
                    4. ⚙️ C++ (Under Implementation) 
                    5. 💎 Ruby (Coming Soon)
                    6. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Under Implementation)

~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~                                        
   """
    ]

    banner = random.choice(banners)
    click.echo(banner)

def show_loading_c(message, duration=3):
    """Simulate a loading effect with a progress bar."""
    click.echo(Fore.YELLOW + f"\n{message}...\n")
    for i in range(1, duration * 10 + 1):
        bar = "█" * (i // 2) + "-" * ((duration * 5) - (i // 2))
        click.echo(f"\r[{bar}] {i * 10 // duration}%", nl=False)
        time.sleep(0.1)
    click.echo(Fore.GREEN + " ✅" + Style.RESET_ALL)


#-------------------------------------------------AI _ INTEGRATION--------------------------------------------------------------------------------------------------------

# Hugging Face API key and URL
API_KEY = "add your api key here"  # Replace with your actual Hugging Face API key
API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"  # Model URL (can be changed to another model)
headers = {"Authorization": f"Bearer {API_KEY}"}

# Function to query the AI model
def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying the AI model: {e}")
        return None

# Function to perform deobfuscation check
def deobfuscation_check(original_code: str, obfuscated_code: str) -> str:
    prompt = f"""
I have two versions of a piece of code.

Original code:
-------------------
{original_code}
-------------------

Obfuscated code:
-------------------
{obfuscated_code}
-------------------

Please analyze whether the obfuscated code preserves the same logic and functionality as the original code. If it does not, provide suggestions or code fixes to ensure the obfuscated version works as intended.
"""
    return query({"inputs": prompt})

# Function to clean up and format the AI response
def format_ai_response(response):
    if isinstance(response, list) and "generated_text" in response[0]:
        # Extract the actual suggestions or analysis
        ai_text = response[0]["generated_text"]

        # Clean up and format the text (e.g., removing unnecessary parts, shortening the explanation)
        ai_text = ai_text.replace("phyton", "python")  # Fix typos
        ai_text = ai_text.replace("\n\n", "\n")  # Remove extra newlines

        # Simplify the output and focus on the key suggestions
        cleaned_response = ai_text.split("\n#")  # Split at each new section of suggestion
        cleaned_response = "\n\n".join(cleaned_response[:5])  # Display only the first few meaningful lines

        return cleaned_response
    else:
        return "No suggestions provided."


# Function to create a moving bar graph effect
# def create_moving_bar_graph(canvas, width, height, num_bars=30):
#     # List to store the bar objects
#     bars = []

#     # Create initial bars with random heights
#     for i in range(num_bars):
#         x = i * (width // num_bars)  # Space bars evenly
#         height_value = random.randint(50, height - 50)  # Random height for each bar
#         bar = canvas.create_rectangle(x, height - height_value, x + (width // num_bars) - 5, height, fill="cyan")
#         bars.append((bar, height_value))
def create_moving_bar_graph(canvas, width, height, num_bars):
    bars = []

    def draw_bars():
        canvas.delete("all")  # Clear previous bars
        bars.clear()
        for i in range(num_bars):
            x = i * (width // num_bars)
            height_value = random.randint(50, height - 50)
            bar = canvas.create_rectangle(x, height - height_value, x + (width // num_bars) - 5, height, fill="cyan")
            bars.append((bar, height_value))

    def animate_bars():
        for i, (bar, _) in enumerate(bars):
            new_height = random.randint(50, height - 50)
            canvas.coords(bar, i * (width // num_bars), height - new_height, (i + 1) * (width // num_bars) - 5, height)
        canvas.after(100, animate_bars)

    draw_bars()
    animate_bars()

    # Function to animate the bars
    # def animate_bars():
    #     for i, (bar, current_height) in enumerate(bars):
    #         # Randomly change the height of each bar
    #         new_height = random.randint(50, height - 50)

    #         # Move the bar's top edge to simulate the rise and fall effect
    #         canvas.coords(bar, (i * (width // num_bars)), height - new_height, (i + 1) * (width // num_bars) - 5, height)

    #         # Update the height data
    #         bars[i] = (bar, new_height)

    #     canvas.after(100, animate_bars)  # Call animate_bars again after 100ms

    # animate_bars()

# Function to create a gradient effect
def create_gradient_effect(window):
    window.configure(bg="#0c0c0c")
    window.after(100, lambda: window.configure(bg="#141414"))

# Function to create a glowing effect on text
def create_glowing_text_effect(widget):
    def glow_text():
        current_fg = widget.cget("fg")
        new_fg = "cyan" if current_fg == "lightblue" else "lightblue"
        widget.config(fg=new_fg)
        widget.after(500, glow_text)
    glow_text()

# Function to create a typing effect
def typing_effect(widget, text, interval=1):
    def type_writer(index=0):
        if index < len(text):
            widget.insert(tk.END, text[index])
            widget.yview(tk.END)
            widget.after(interval, type_writer, index + 1)
    widget.delete(1.0, tk.END)
    type_writer()

# Function to read code from files and perform deobfuscation check
def deobfuscation_check_from_files(original_file_path: str, obfuscated_file_path: str) -> str:
    try:
        # Read the original and obfuscated code from the provided file paths
        with open(original_file_path, 'r') as original_file:
            original_code = original_file.read()
        
        with open(obfuscated_file_path, 'r') as obfuscated_file:
            obfuscated_code = obfuscated_file.read()

        # Run the deobfuscation check with the file contents
        ai_suggestions = deobfuscation_check(original_code, obfuscated_code)
        return ai_suggestions

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

# Function to show results in a Tkinter window
# def show_ai_results_from_files(original_file_path, obfuscated_file_path):
#     # Step 1: Run Deobfuscation Check with file paths
#     ai_suggestions = deobfuscation_check_from_files(original_file_path, obfuscated_file_path)

#     # Step 2: Format the AI response
#     if ai_suggestions:
#         formatted_suggestions = format_ai_response(ai_suggestions)
#     else:
#         formatted_suggestions = "No suggestions provided."

#     # Create the main window
#     window = tk.Tk()
#     window.title("AI Deobfuscation Check")

#     # Set the window size and background
#     window.geometry("700x600")  # Increased height for more space
#     window.configure(bg="#0c0c0c")
#     create_gradient_effect(window)

#     # Create a title label with glowing effect
#     title_label = tk.Label(window, text="AI Deobfuscation Results", font=("Courier", 18, "bold"), fg="cyan", bg="#0c0c0c")
#     title_label.pack(pady=20)
    
#     # Create a canvas for the moving bar graph effect
#     canvas = tk.Canvas(window, width=700, height=150, bg="#0c0c0c", bd=0, highlightthickness=0)
#     canvas.pack(pady=20)

#     # Start the moving bar graph effect with 30 bars
#     create_moving_bar_graph(canvas, 700, 150, num_bars=30)

#     # Create the scrolled text box for displaying the code and results (increased size)
#     text_box = scrolledtext.ScrolledText(window, width=90, height=15, wrap=tk.WORD, font=("Courier", 10), bg="#1e1e1e", fg="cyan", insertbackground="cyan")
#     text_box.pack(pady=20, padx=10)  # Added padding to make it look more spaced

#     # Prepare the output to be shown
#     result_text = f"Original Code:\n{open(original_file_path).read()}\n\nObfuscated Code:\n{open(obfuscated_file_path).read()}\n\nAI Suggestions:\n{formatted_suggestions}"

#     # Display the AI suggestions in the text box with typing effect
#     typing_effect(text_box, result_text, interval=50)

#     # Apply the glowing text effect to the text box content
#     create_glowing_text_effect(text_box)

def show_ai_results_from_files(original_file_path, obfuscated_file_path):
    # Step 1: Read files
    with open(original_file_path, 'r') as f:
        original_code = f.read()
    with open(obfuscated_file_path, 'r') as f:
        obfuscated_code = f.read()

    # # AI suggestions (Placeholder since AI call isn't included)
    # formatted_suggestions = "AI suggestions will be displayed here."
    ai_suggestions = deobfuscation_check_from_files(original_file_path, obfuscated_file_path)

       # Step 2: Format the AI response
    if ai_suggestions:
             formatted_suggestions = format_ai_response(ai_suggestions)
    else:
             formatted_suggestions = "No suggestions provided."

    # Create the main window
    window = tk.Tk()
    window.title("AI Obfuscation Analyser")
    window.geometry("800x600")  # Start at a normal size
    window.configure(bg="#0c0c0c")

    # Default number of bars for the initial window size
    num_bars = 30  

    # Title Label
    title_label = tk.Label(window, text="AI Obfuscation Analysis Results", font=("Courier", 18, "bold"), fg="cyan", bg="#0c0c0c")
    title_label.pack(pady=10)

    # Canvas for animation
    canvas = tk.Canvas(window, width=800, height=150, bg="#0c0c0c", bd=0, highlightthickness=0)
    canvas.pack(pady=10)

    # Create initial animation
    create_moving_bar_graph(canvas, 800, 150, num_bars)

    # Scrolled Text Box
    text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Courier", 10), bg="#1e1e1e", fg="cyan", insertbackground="cyan")
    text_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Display AI results with typing effect
    result_text = f"Original Code:\n{original_code}\n\nObfuscated Code:\n{obfuscated_code}\n\nAI Suggestions:\n{formatted_suggestions}"
    typing_effect(text_box, result_text, interval=50)
    create_glowing_text_effect(text_box)

    def on_window_resize(event=None):
        new_width = window.winfo_width()
        new_height = window.winfo_height()

        # Increase the number of bars dynamically based on width
        new_num_bars = max(30, new_width // 25)  

        # Update the canvas size and redraw bars
        canvas.config(width=new_width, height=150)
        create_moving_bar_graph(canvas, new_width, 150, new_num_bars)

        # Adjust text box size
        text_box.config(width=new_width // 10, height=new_height // 30)

    # Bind the resize event
    window.bind("<Configure>", on_window_resize)
    # Run the Tkinter window
    window.mainloop()
# Show the results in the Tkinter window

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@click.option("--input_file", required=True, help="Input source code file")
@click.option("--output_file", required=True, help="Output obfuscated file")
@click.option("--password", required=False, help="Password for Python and JavaScript obfuscation")
@click.command(help="""CLI Tool for Code Obfuscation and Multi-Language Support.
    
    Note:
    - C and C++ obfuscation does not support object-oriented programming (OOP) obfuscation.
    - Only basic obfuscation techniques such as variable renaming and comment removal are supported for C and C++.
""")
def obfuscate(input_file, output_file, password):

    # Detect language based on file extension
    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == ".py":
        language = "python"
    elif file_extension == ".js":
        language = "javascript"
    elif file_extension == ".c":
        language = "c"
    elif file_extension == ".cpp":
        language = "cpp"
    else:
        click.echo("Unsupported file type! Only Python (.py), JavaScript (.js), C (.c), and C++ (.cpp) are supported.")
        return

    click.echo(f"🌍:Detected language: {language.capitalize()}")

    if language == "python":
        # Obfuscate Python code
        if not password:
            click.echo("Error: Password is required for Python obfuscation.")
            return
        with open(input_file, "r", encoding="utf-8") as f:
            code = f.read()
        obfuscated_code = replac_8(code, password)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        click.echo(Fore.YELLOW + f"\nProcessing: {input_file}")
        show_loading_c("Processing Python file", 5)
        click.echo(Fore.GREEN + f"\n🔁:Python double obfuscation complete!🎭")
        show_loading_c("🔐:Saving Python Obfuscated file", 5)  # Call the progress bar here for 5 seconds    
        click.echo(Fore.GREEN + f"✅:Python obfuscation complete! Output saved to:📂 {output_file}")

    elif language == "javascript":
        # Obfuscate JavaScript code
        if not password:
            click.echo("Error: Password is required for JavaScript obfuscation.")
            return
        try:
            subprocess.run(["node", "obfuscator/javascript_ob.js", input_file, output_file, password], check=True)
            click.echo(Fore.YELLOW + f"\nProcessing: {input_file}")
            show_loading_c("Processing Javascript file", 5)  # Call the progress bar here for 5 seconds
            click.echo(Fore.GREEN + f"\n🔁:JavaScript double obfuscation complete!🎭")
            show_loading_c("🔐:Saving Javascript Obfuscated file", 5)
            click.echo(Fore.GREEN + f"\n✅:JavaScript obfuscation complete! Output saved to :📂 {output_file}")
        except subprocess.CalledProcessError as e:
            click.echo(f"Error during JavaScript obfuscation: {e}")
    elif language == "c":
        # Obfuscate C code (no password required)
        click.echo(Fore.CYAN + "\nNote: The C obfuscation process does not support object-oriented programming (OOP) obfuscation.")
        click.echo(Fore.YELLOW + f"\nProcessing: {input_file}")
        show_loading_c("Processing C file", 5)  # Call the progress bar here for 5 seconds
        
        # Use the user-specified output filename if provided, otherwise use a default name
        output_filename = output_file if output_file else f"obfuscated_{os.path.basename(input_file)}"
        
        c_process_file(input_file, output_filename)  # Call C obfuscation function
        click.echo(Fore.GREEN + f"\n✅:C obfuscation complete! Output saved to:📂 {output_filename}")

    elif language == "cpp":
        # Obfuscate C++ code (no password required)
        click.echo(Fore.CYAN + "\nNote: The C++ obfuscation process does not support object-oriented programming (OOP) obfuscation.")
        click.echo(Fore.YELLOW + f"\nProcessing: {input_file}")
        show_loading_c("Processing C++ file", 5)  # Call the progress bar here for 5 seconds
        
        # Use the user-specified output filename if provided, otherwise use a default name
        output_filename = output_file if output_file else f"obfuscated_{os.path.basename(input_file)}"
        
        cpp_process_file(input_file, output_filename)  # Call C++ obfuscation function
        click.echo(Fore.GREEN + f"\n✅:C++ obfuscation complete! Output saved to:📂 {output_filename}")


    if input_file and output_file:
        click.echo(Fore.GREEN + f"\n✅:Intailizing Ai Checking System")
        show_loading_c("Intializing....", 5)
        original_file_path = input(Fore.RED + "\n[::] 📂" + Fore.CYAN + "Please enter the Original full file path again: ")  # Replace with the actual file path of original code
        obfuscated_file_path = input(Fore.RED + "\n[::] 📂" + Fore.CYAN + "Please enter the Obfuscated full file path again: ")  # Replace with the actual file path of obfuscated code
        show_ai_results_from_files(original_file_path, obfuscated_file_path)
        
    

if __name__ == "__main__":
    display_banner()
    obfuscate()
