# Code Obfuscator CLI Tool

## Overview
This is a command-line interface (CLI) tool designed to obfuscate code in multiple programming languages, making it harder to reverse-engineer while preserving functionality. The tool also integrates AI-based analysis to verify the correctness of the obfuscated code by comparing it with the original code.

**Creator**: Vishal (Bloodhowl)  
**Date**: 2025-01-27  
**Version**: 1.0.0  

## Supported Languages
The tool supports obfuscation for the following languages:
1. 🐍 **Python** (.py) - Full support with variable renaming, string encoding, function, and class obfuscation.
2. 💻 **JavaScript** (.js) - Full support with password-protected obfuscation.
3. 🖥️ **C** (.c) - Basic support (variable renaming, comment removal; no OOP obfuscation).
4. ⚙️ **C++** (.cpp) - Basic support (variable renaming, comment removal; no OOP obfuscation).
5. 🦀 **Rust** (.rs) - Under implementation (basic support, no advanced features like macros or traits).
6. 🛠️ **Go** - Coming soon.

## Features
- **Variable Renaming**: Randomizes variable names to obscure code readability.
- **String Encoding**: Encodes strings to make them harder to interpret.
- **Function Obfuscation**: Obfuscates function names and structures in supported languages.
- **Class Obfuscation**: Obfuscates class names and structures (Python only).
- **AI Integration**: Uses AI to analyze and verify that the obfuscated code preserves the original logic and functionality.
- **Dynamic Language Support**: Extensible framework for adding new languages.
- **Interactive CLI**: User-friendly interface with progress bars and colorful output.

## Prerequisites
To use this tool, ensure you have the following installed:
- **Python 3.8+**
- **Node.js** (for JavaScript obfuscation)
- **Rust** (for Rust obfuscation, if applicable)
- Required Python packages:
  ```bash
  pip install click colorama
  ```
- A Rust obfuscator executable (`rust_obfuscator.exe`) for Rust support (if applicable).
- Tkinter for the AI results GUI (usually included with Python).

## Installation
1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   cd code-obfuscator
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Create a `requirements.txt` file with `click` and `colorama` if not already present.
3. Ensure Node.js is installed for JavaScript obfuscation:
   ```bash
   node --version
   ```
4. (Optional) Compile the Rust obfuscator if supporting Rust files:
   ```bash
   cd obfuscator
   cargo build --release
   ```

## Usage
Run the CLI tool using the following command:
```bash
python obfuscate.py --input_file <input_file> --output_file <output_file> [--password <password>]
```

### Options
- `--input_file` (required): Path to the source code file to obfuscate.
- `--output_file` (required): Path to save the obfuscated code.
- `--password` (optional): Password for Python and JavaScript obfuscation (required for these languages).

### Example
To obfuscate a Python file:
```bash
python obfuscate.py --input_file example.py --output_file obfuscated_example.py --password mysecretpassword
```

To obfuscate a C file (no password required):
```bash
python obfuscate.py --input_file example.c --output_file obfuscated_example.c
```

After obfuscation, the tool prompts for the original and obfuscated file paths to perform an AI-based analysis, displaying the results in a Tkinter GUI with animated visualizations.

## Notes
- **C and C++ Limitations**: These languages only support basic obfuscation (variable renaming, comment removal). Object-oriented programming (OOP) obfuscation is not supported.
- **Rust Limitations**: Currently under implementation, with limited support for advanced features like macros or trait implementations.
- **AI Integration**: The AI analysis feature (currently commented out) requires a Hugging Face API key and a compatible model (e.g., `bigcode/starcoder`). Uncomment and configure the API key in the code to enable this feature.
- **GUI Features**: The AI results are displayed in a Tkinter window with a moving bar graph animation and a glowing text effect for better user experience.

## Directory Structure
```
code-obfuscator/
├── obfuscate.py                # Main CLI script
├── obfuscator/
│   ├── python_ob.py            # Python obfuscation logic
│   ├── c_obfuscator.py         # C obfuscation logic
│   ├── cpp_obfuscator.py       # C++ obfuscation logic
│   ├── javascript_ob.js        # JavaScript obfuscation script
│   ├── target/release/
│   │   └── rust_obfuscator.exe # Rust obfuscator executable (optional)
├── ai_analyzer/
│   ├── ai.py                   # AI analysis logic
└── README.md                   # This file
```

## AI Analysis
The tool includes an AI-powered feature to compare the original and obfuscated code, ensuring functional equivalence. To enable this:
1. Uncomment the Hugging Face API code in `obfuscate.py`.
2. Set your Hugging Face API key in the `API_KEY` variable.
3. Ensure internet connectivity for API requests.

The AI results are displayed in a Tkinter GUI with:
- Original and obfuscated code side-by-side.
- AI suggestions for ensuring functional equivalence.
- Animated bar graph and glowing text effects for a modern UI.

## Future Improvements
- Add support for Go obfuscation.
- Enhance C, C++, and Rust obfuscation with advanced techniques.
- Improve AI integration with local models to avoid API dependency.
- Add batch processing for multiple files.
- Support additional languages like Java and PHP.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For issues or suggestions, contact Vishal (Bloodhowl) via email or open an issue on the repository.