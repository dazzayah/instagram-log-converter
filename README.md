# Instagram JSON Parser 📄📊  

Welcome to my **Instagram Message Log Parser** script, intended for processing the JSON log files given by Instagram when requested. 

This Python script is designed those files, specifically those related to messages. It converts the message history into a readable format and saves it as a plain text file.  

## Features 🚀  
- Reads JSON files exported from Instagram.  
- Processes messages in correct chronological order.  
- Replaces special characters and supports common encodings (latin1 and UTF-8).  
- Identifies and marks messages with multimedia content.  
- Generates a formatted text file containing the message history.  

## Requirements 📋  
- **Python 3.6 or later**  
- Required modules:
  - `json` (bundled with Python by default)  
  - `Utils` (containing the `ReplaceChar` function. Ensure you have this module or implement it yourself).  

## Installation 🔧  

1. Clone this repository to your local machine:  
   ```bash
   git clone https://github.com/dazzayah/instagram-json-parser.git
   cd instagram-json-parser
   ```  

2. Ensure all dependencies are installed (if `Utils` is not available, add its implementation).  

3. Place the exported JSON message file from Instagram in the `JSON_Content` folder, following the directory structure defined in the script.  

## Usage 🛠️  

1. Ensure that the JSON file is located at `JSON_Content/john-doe/message_1.json`.  
   - If, for whatever reason, you're using a different file path or name, update the `MAINPATH` variable in the script:  
     ```python
     MAINPATH = r"PATH/TO/YOUR/FILE.json"
     ```  

2. Run the script:  
   ```bash
   python script.py
   ```  

3. The processed message history will be saved in a file named `Output.txt` in the same directory.  

## Project Structure 🗂️  
```
instagram-json-parser/  
├── JSON_Content/  
│   └── john-doe/  
│       └── message_1.json  # Example JSON file.  
├── script.py              # Main script.  
├── Output.txt             # Processed output (generated after running the script).  
├── Utils.py               # Module for `ReplaceChar` (implement this if not available).  
└── README.md              # This file.  
```  

## Example Output 📜  
The `Output.txt` file will have a format similar to this:  
```
User1: Hello!  
User2: How are you?  
User1: ~Multimedia~  
User2: I'm good, thanks.  
```  

## Contributions 🤝  
Contributions are welcome! Feel free to open an [issue](https://github.com/yourusername/instagram-json-parser/issues) or submit a pull request.  

## License 📝  
This project is licensed under the [MIT License](LICENSE).  
