# import random
# import time
# import os
# from colorama import Fore, Style, init  # For colorized text
# import click
# from obfuscator.python_ob import *  # Python obfuscation logic
# from tqdm import tqdm
# import subprocess

# init(autoreset=True)


# def display_banner():
#     """Display a random ASCII banner"""
#     banners = [
#         Fore.YELLOW + r"""
#    __              __     _____        __              
#   /  )     /      / ')/    /  '       /  )    _/_      
#  /   __ __/ _    /  //__,-/-,. . _   /   __.  /  __ __ 
# (__/(_)(_/_</_  (__//_)(_/  (_/_/_)_(__/(_/|_<__(_)/ (_)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                                       
#     🧠 ->   Creator: Vishal(Bloodhowl)
#     📅 ->   Date: 2025-01-28
#     🔧 ->   Version: 1.0.0
#     🚀 ->   Tool: Code Obfuscator
#     📚 ->   Supported Languages:
#                     1. 🐍 Python
#                     2. 💻 JavaScript
#                     3. 🖥️ C (Coming Soon)
#                     4. 💎 Ruby (Coming Soon)
#                     5. ☕ Java (Coming Soon)
#                     6. ⚙️ C++ (Coming Soon)
#                     7. 🔤 TypeScript (Coming Soon)

#     ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
#         ✔ Variable Renaming
#         ✔ String Encoding
#         ✔ Code Flattening
#         ✔ Function Obfuscation
#         ✔ Class Obfuscation
#         ✔ Dynamic Language Support (AI Integration Coming Soon)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                   
#      """,
#         Fore.CYAN + r"""
#  _______  _____  ______  _______       _____  ______  _______ _     _ _______ _______ _______ _______  _____   ______
#  |       |     | |     \ |______      |     | |_____] |______ |     | |______ |       |_____|    |    |     | |_____/ 
#  |_____  |_____| |_____/ |______      |_____| |_____] |       |_____| ______| |_____  |     |    |    |_____| |    \_

# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#     🧠 ->   Creator: Vishal(Bloodhowl)
#     📅 ->   Date: 2025-01-28
#     🔧 ->   Version: 1.0.0
#     🚀 ->   Tool: Code Obfuscator
#     📚 ->   Supported Languages:
#                     1. 🐍 Python
#                     2. 💻 JavaScript
#                     3. 🖥️ C (Coming Soon) 
#                     4. 💎 Ruby (Coming Soon)
#                     5. ☕ Java (Coming Soon)
#                     6. ⚙️ C++ (Coming Soon)
#                     7. 🔤 TypeScript (Coming Soon)

#     ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
#         ✔ Variable Renaming
#         ✔ String Encoding
#         ✔ Code Flattening
#         ✔ Function Obfuscation
#         ✔ Class Obfuscation
#         ✔ Dynamic Language Support (AI Integration Coming Soon)

# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                                                                                                                 
#     """,
#         Fore.RED + r"""
                                           
#  .-     .      .-..  .--     .-    .       
# (  .-..-| .-,  | ||-.|-. ..-(  .-.-|-.-..-.
#  `-`-'`-'-`'-  `-'`-'' '-'-' `-`-`-'-`-''  

# ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~

#     🧠 ->   Creator: Vishal(Bloodhowl)
#     📅 ->   Date: 2025-01-27
#     🔧 ->   Version: 1.0.0
#     🚀 ->   Tool: Code Obfuscator
#     📚 ->   Supported Languages:
#                     1. 🐍 Python
#                     2. 💻 JavaScript
#                     3. 🖥️ C (Coming Soon)
#                     4. 💎 Ruby (Coming Soon)
#                     5. ☕ Java (Coming Soon)
#                     6. ⚙️ C++ (Coming Soon)
#                     7. 🔤 TypeScript (Coming Soon)

#     ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
#         ✔ Variable Renaming
#         ✔ String Encoding
#         ✔ Code Flattening
#         ✔ Function Obfuscation
#         ✔ Class Obfuscation
#         ✔ Dynamic Language Support (AI Integration Coming Soon)


# ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~                                        
#    """
#     ]

#     banner = random.choice(banners)
#     click.echo(banner)


# def detect_language(file_path):
#     """Detect the language based on file extension"""
#     file_extension = os.path.splitext(file_path)[1].lower()
#     supported_languages = {'.py': 'Python', '.js': 'JavaScript'}
#     return supported_languages.get(file_extension, None)  # Default to None if not found



# def simulate_obfuscation_progress(analysis, flags):
#     """Simulate the obfuscation process with a loading bar and colored output"""
#     steps = [
#         (Fore.YELLOW, f"Analyzing {analysis['file']}"),
#         (Fore.CYAN, f"Functions: {', '.join(analysis['functions']) or 'None'}"),
#         (Fore.CYAN, f"Classes: {', '.join(analysis['classes']) or 'None'}"),
#         (Fore.CYAN, f"Variables: {', '.join(analysis['variables']) or 'None'}"),
#     ]
#     steps += [
#         (Fore.YELLOW, "Obfuscating Functions..." if flags['obfuscate_functions'] else "Skipping Function Obfuscation"),
#         (Fore.YELLOW, "Obfuscating Variables..." if flags['obfuscate_variables'] else "Skipping Variable Obfuscation"),
#     ]

#     with tqdm(total=len(steps), desc="Obfuscation", ncols=100, unit="step") as progress_bar:
#         for color, message in steps:
#             tqdm.write(color + message + Style.RESET_ALL)
#             time.sleep(0.5)
#             progress_bar.update(1)


# def simulate_js_obfuscation_progress(analysis, flags):
#     """Simulate the obfuscation process with a detailed step-by-step loading bar and colored output for JS"""
    
#     # Steps for analysis
#     steps = [
#         (Fore.CYAN, f"Analyzing Functions..."),
#         # (Fore.CYAN, f"Functions: {', '.join(analysis['functions']) or 'None'}"),
#         (Fore.YELLOW, f"Analyzing Classes..."),
#         # (Fore.CYAN, f"Classes: {', '.join(analysis['classes']) or 'None'}"),
#         (Fore.RED, f"Analyzing Variables..."),
#         # (Fore.CYAN, f"Variables: {', '.join(analysis['variables']) or 'None'}"),
#     ]
    
#     # Step after analysis is complete
#     steps.append((Fore.GREEN, "Analysis complete. Starting obfuscation..."))

#     # Simulate progress
#     with tqdm(total=len(steps), desc="Obfuscation", ncols=100, unit="step") as progress_bar:
#         for color, message in steps:
#             tqdm.write(color + message)  # Output each step
#             time.sleep(0.5)  # Simulate time for each step
#             progress_bar.update(1)

# def obfuscate_js_code(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables):
#     """Simulate JavaScript obfuscation"""
#     try:
#         analysis = {"file": file, "functions": [], "classes": [], "variables": []}
#         flags = {
#             'rename': rename, 
#             'encode': encode, 
#             'flatten': flatten, 
#             'whitespace': whitespace,
#             'obfuscate_functions': obfuscate_functions,
#             'obfuscate_variables': obfuscate_variables
#         }

#         simulate_obfuscation_progress(analysis, flags)
        
#         obfuscator_path = os.path.join("obfuscator", "javascript_ob.js")
#         output_js = f"{output}.js"
#         js_flags = []

#         if rename:
#             js_flags.append("--rename")
#         if encode:
#             js_flags.append("--encode")
#         if flatten:
#             js_flags.append("--flatten")
#         if whitespace:
#             js_flags.append("--whitespace")
        
#         subprocess.run(["node", obfuscator_path, file, output_js] + js_flags, check=True)
#         click.echo(Fore.GREEN + f"JavaScript code obfuscated and saved to {output_js}")
    
#     except FileNotFoundError:
#         click.echo(Fore.RED + "Error: Node.js or the JavaScript obfuscator script was not found.")
#     except subprocess.CalledProcessError:
#         click.echo(Fore.RED + "Error: JavaScript obfuscation failed.")


# @click.command()
# @click.option('--file', prompt='Path to your code file', help='The file to analyze.')
# @click.option('--output', default='obfuscated_code', help='Output file for obfuscated code.')
# @click.option('--rename', is_flag=True, help='Enable variable renaming.')
# @click.option('--encode', is_flag=True, help='Enable string encoding.')
# @click.option('--flatten', is_flag=True, help='Flatten code to fewer lines.')
# @click.option('--whitespace', is_flag=True, help='Remove unnecessary whitespace.')
# @click.option('--obfuscate-functions', is_flag=True, help='Obfuscate function names.')
# @click.option('--obfuscate-variables', is_flag=True, help='Obfuscate variable names.')
# def obfuscate(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables):
#     """CLI Tool for Code Obfuscation"""
#     # display_banner()

#     # Detect the language of the file
#     lang = detect_language(file)

#     if not lang:
#         click.echo(Fore.RED + "This language is not yet supported.")
#         return

#     click.echo(Fore.GREEN + f"Detected language: {lang.upper()}")


#     flags = {
#     'rename': rename,
#     'encode': encode,
#     'flatten': flatten,
#     'whitespace': whitespace,
#     'obfuscate_functions': obfuscate_functions,
#     'obfuscate_variables': obfuscate_variables
#     }

#     if lang == 'Python':
#         with open(file, 'r') as f:
#             code = f.read()
        
#         analysis = analyze_code(code)
#         analysis['file'] = file

#         simulate_obfuscation_progress(analysis, flags)

#         if rename:
#             code = rename_variables(code)
#         if encode:
#             code = encode_strings(code)
#         if flatten:
#             code = flatten_code(code)
#         if whitespace:
#             code = remove_whitespace(code)

#         with open(f"{output}.py", 'w') as f:
#             f.write(code)

#         click.echo(Fore.GREEN + f"Python code obfuscated and saved to {output}.py")
    
#     elif lang == 'JavaScript':
#         obfuscate_js_code(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables)



# if __name__ == '__main__':
#     display_banner()
#     obfuscate()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random
import time
import os
from colorama import Fore, Style, init  # For colorized text
import click
from obfuscator.python_ob import *  # Python obfuscation logic
from tqdm import tqdm
import subprocess

init(autoreset=True)


def display_banner():
    """Display a random ASCII banner"""
    banners = [
        Fore.YELLOW + r"""
   __              __     _____        __              
  /  )     /      / ')/    /  '       /  )    _/_      
 /   __ __/ _    /  //__,-/-,. . _   /   __.  /  __ __ 
(__/(_)(_/_</_  (__//_)(_/  (_/_/_)_(__/(_/|_<__(_)/ (_)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                                       
    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Coming Soon)
                    4. 💎 Ruby (Coming Soon)
                    5. ☕ Java (Coming Soon)
                    6. ⚙️ C++ (Coming Soon)
                    7. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Code Flattening
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Coming Soon)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                   
     """,
        Fore.CYAN + r"""
 _______  _____  ______  _______       _____  ______  _______ _     _ _______ _______ _______ _______  _____   ______
 |       |     | |     \ |______      |     | |_____] |______ |     | |______ |       |_____|    |    |     | |_____/ 
 |_____  |_____| |_____/ |______      |_____| |_____] |       |_____| ______| |_____  |     |    |    |_____| |    \_

══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Coming Soon) 
                    4. 💎 Ruby (Coming Soon)
                    5. ☕ Java (Coming Soon)
                    6. ⚙️ C++ (Coming Soon)
                    7. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Code Flattening
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Coming Soon)

══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                                                                                                                 
    """,
        Fore.RED + r"""
                                           
 .-     .      .-..  .--     .-    .       
(  .-..-| .-,  | ||-.|-. ..-(  .-.-|-.-..-.
 `-`-'`-'-`'-  `-'`-'' '-'-' `-`-`-'-`-''  

~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~

    🧠 ->   Creator: Vishal(Bloodhowl)
    📅 ->   Date: 2025-01-27
    🔧 ->   Version: 1.0.0
    🚀 ->   Tool: Code Obfuscator
    📚 ->   Supported Languages:
                    1. 🐍 Python
                    2. 💻 JavaScript
                    3. 🖥️ C (Coming Soon)
                    4. 💎 Ruby (Coming Soon)
                    5. ☕ Java (Coming Soon)
                    6. ⚙️ C++ (Coming Soon)
                    7. 🔤 TypeScript (Coming Soon)

    ~~~~~~~~~~~~~~~~~~~~~~~~ Features ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ✔ Variable Renaming
        ✔ String Encoding
        ✔ Code Flattening
        ✔ Function Obfuscation
        ✔ Class Obfuscation
        ✔ Dynamic Language Support (AI Integration Coming Soon)


~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~                                        
   """
    ]

    banner = random.choice(banners)
    click.echo(banner)

def detect_language(file_path):
    """Detect the language based on file extension"""
    file_extension = os.path.splitext(file_path)[1].lower()
    supported_languages = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.c': 'C'
    }
    return supported_languages.get(file_extension, None)


def show_loading_c(message, duration=3):
    """Simulate a loading effect with a progress bar."""
    click.echo(Fore.YELLOW + f"\n{message}...\n")
    for i in range(1, duration * 10 + 1):
        bar = "█" * (i // 2) + "-" * ((duration * 5) - (i // 2))
        click.echo(f"\r[{bar}] {i * 10 // duration}%", nl=False)
        time.sleep(0.1)
    click.echo(Fore.GREEN + " ✅" + Style.RESET_ALL)



def obfuscate_c_code(file, output):
    """Automatically compile the C obfuscator and provide the execution command with animations."""
    obfuscator_source = "obfuscator/c_obfuscator.c"
    obfuscator_exe = "obfuscator/c_obfuscator.exe"

    click.echo(Fore.BLUE + "\n🔍 Analyzing the code structure...")
    show_loading_c("🔄 Scanning syntax", 2)
    show_loading_c("🛠 Identifying obfuscation patterns", 2)
    show_loading_c("📊 Preparing the obfuscator", 2)

    try:
        if not os.path.exists(obfuscator_exe):
            click.echo(Fore.YELLOW + "\n⚙ Compiling the C obfuscator...\n")
            subprocess.run(["gcc", obfuscator_source, "-o", obfuscator_exe], check=True)

        click.echo(Fore.GREEN + "\n✅ C obfuscator compiled successfully!")
        time.sleep(1)
        click.echo(Fore.YELLOW + "\n🚀 Ready to obfuscate! Run the following command:\n")
        click.echo(Fore.CYAN + f"./{obfuscator_exe} path/to/the/code/to/obfuscate obfuscated_example.c\n")
        

    except FileNotFoundError:
        click.echo(Fore.RED + "❌ Error: GCC compiler not found. Please install GCC and try again.")
    except subprocess.CalledProcessError:
        click.echo(Fore.RED + "❌ Error: C obfuscation compilation failed.")





def show_loading(message, duration=2):
    """Simulate a loading effect with a progress bar."""
    click.echo(Fore.YELLOW + f"\n{message}...\n")
    for i in range(1, duration * 10 + 1):
        bar = "█" * (i // 2) + "-" * ((duration * 5) - (i // 2))
        click.echo(f"\r[{bar}] {i * 10 // duration}%", nl=False)
        time.sleep(0.1)
    click.echo(Fore.GREEN + " ✅" + Style.RESET_ALL)



def simulate_obfuscation_progress(analysis, flags):
    """Simulate the obfuscation process with a loading bar and colored output"""
    steps = [
        (Fore.YELLOW, f"📂 Analyzing {analysis['file']}..."),
        (Fore.CYAN, "🔍 Analyzing for Functions..."),
        (Fore.YELLOW, "🔍 Analyzing for Classes..."),
        (Fore.RED, "🔍 Analyzing for Variables..."),
        (Fore.GREEN, "✅ Analysis Complete. Preparing obfuscation..."),
        (Fore.YELLOW, "🛠 Obfuscating Functions..." if flags['obfuscate_functions'] else "⏭ Skipping Function Obfuscation"),
        (Fore.YELLOW, "🛠 Obfuscating Variables..." if flags['obfuscate_variables'] else "⏭ Skipping Variable Obfuscation"),
    ]

    click.echo(Fore.YELLOW + "\n🚀 Starting Obfuscation...\n" + Style.RESET_ALL)

    for color, message in steps:
        show_loading(message, 2)

    click.echo(Fore.GREEN + f"\n🎉 Obfuscation Complete! Obfuscated code saved to {analysis['output_file']}\n" + Style.RESET_ALL)



def simulate_js_obfuscation_progress(analysis, flags):
    """Simulate the obfuscation process with a detailed step-by-step loading bar and colored output for JS"""
    steps = [
        (Fore.YELLOW, f"📂 Analyzing {analysis['file']}..."),
        (Fore.CYAN, "🔍 Analyzing for Functions..."),
        (Fore.YELLOW, "🔍 Analyzing for Classes..."),
        (Fore.RED, "🔍 Analyzing for Variables..."),
        (Fore.GREEN, "✅ Analysis Complete. Preparing obfuscation...")
    ]

    click.echo(Fore.YELLOW + "\n🚀 Starting JavaScript Obfuscation...\n" + Style.RESET_ALL)

    for color, message in steps:
        show_loading(message, 2)

   

def obfuscate_js_code(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables):
    """Simulate JavaScript obfuscation"""
    try:
        analysis = {"file": file, "functions": [], "classes": [], "variables": [], "output_file": f"{output}.js"}
        flags = {
            'rename': rename, 
            'encode': encode, 
            'flatten': flatten, 
            'whitespace': whitespace,
            'obfuscate_functions': obfuscate_functions,
            'obfuscate_variables': obfuscate_variables
        }

        simulate_js_obfuscation_progress(analysis, flags)
        
        obfuscator_path = os.path.join("obfuscator", "javascript_ob.js")
        output_js = f"{output}.js"
        js_flags = []

        if rename:
            js_flags.append("--rename")
        if encode:
            js_flags.append("--encode")
        if flatten:
            js_flags.append("--flatten")
        if whitespace:
            js_flags.append("--whitespace")
        
        subprocess.run(["node", obfuscator_path, file, output_js] + js_flags, check=True)
    
    except FileNotFoundError:
        click.echo(Fore.RED + "Error: Node.js or the JavaScript obfuscator script was not found.")
    except subprocess.CalledProcessError:
        click.echo(Fore.RED + "Error: JavaScript obfuscation failed.")


@click.command()
@click.option('--file', prompt='Path to your code file', help='The file to analyze.')
@click.option('--output', default='obfuscated_code', help='Output file for obfuscated code.')
@click.option('--rename', is_flag=True, help='Enable variable renaming.')
@click.option('--encode', is_flag=True, help='Enable string encoding.')
@click.option('--flatten', is_flag=True, help='Flatten code to fewer lines.')
@click.option('--whitespace', is_flag=True, help='Remove unnecessary whitespace.')
@click.option('--obfuscate-functions', is_flag=True, help='Obfuscate function names.')
@click.option('--obfuscate-variables', is_flag=True, help='Obfuscate variable names.')
def obfuscate(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables):
    """CLI Tool for Code Obfuscation"""
   

    lang = detect_language(file)

    if not lang:
        click.echo(Fore.RED + "This language is not yet supported.")
        return

    click.echo(Fore.GREEN + f"Detected language: {lang.upper()}")


    flags = {
    'rename': rename,
    'encode': encode,
    'flatten': flatten,
    'whitespace': whitespace,
    'obfuscate_functions': obfuscate_functions,
    'obfuscate_variables': obfuscate_variables
    }

    if lang == 'Python':
        with open(file, 'r') as f:
            code = f.read()
        
        analysis = analyze_code(code)
        analysis['file'] = file
        analysis['output_file'] = f"{output}.py" 

        simulate_obfuscation_progress(analysis, flags)

        if rename:
            code = rename_variables(code)
        if encode:
            code = encode_strings(code)
        if flatten:
            code = flatten_code(code)
        if whitespace:
            code = remove_whitespace(code)

        with open(f"{output}.py", 'w') as f:
            f.write(code)

        click.echo(Fore.GREEN + f"Python code obfuscated and saved to {output}.py")
    
    elif lang == 'JavaScript':
        obfuscate_js_code(file, output, rename, encode, flatten, whitespace, obfuscate_functions, obfuscate_variables)

    elif lang == 'C':
        obfuscate_c_code(file, output)


if __name__ == '__main__':
    display_banner()
    obfuscate()
