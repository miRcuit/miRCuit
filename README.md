# miRCuit : A Regulatory Circuit Analysis Tool 

miRCuit is a circuit analysis program designed to construct regulatory circuits based on Python. The program is developed as a .py (Python) file and can be executed in an environment such as Visual Studio Code.

## Features
- The program can be utilized by transferring the .py file to an appropriate execution environment, such as VS Code, Jupyter Notebook, etc.
- It is accessible to researchers across various fields and operates by loading files containing expression values of mRNA, miRNA, lncRNA, and TF molecules into the system
- As a result, it offers users different types of regulatory circuits related to their research topics.

## Requirements
### To run this program, you will need the following software and libraries:
    - Python 3.x
    - pandas (version 2.2.2)
    - PyQt5 (version 5.15.11)
    - gseapy (version 1.1.3)
    - scipy (version 1.14.0)
    - matplotlib (version 3.9.1)
    - networkx (version 3.3)

## Installation Steps
1. Download and Install Python
   - Download the latest version of Python from the https://www.python.org/downloads/
   - Run the downloaded file to install Python. Make sure to check the "Add Python to PATH" option during installation.
2. Chose an IDE or Text Editor
   - Select and install an IDE or text editor, such as Visual Studio Code, PyCharm, or Jupyter Notebook.
   - Example: Download Visual Studio Code from https://code.visualstudio.com
3. Install Required Libraries
   - Open the terminal or command prompt.
   - Navigate to your project directory (e.g., cd your_project).
   - Use the following command to install the required libraries (The requirement.txt file is available):
     pip install -r requirements.txt
   - If you are unable to perform this operation, please download each of the libraries mentioned above using the following command through the VS Code terminal.
     pip install <library_name>
4. Download the Program File
   - Download the .py file of the program or clone the source code.
5. Run the Program:
   - Run the code using Visual Studio Code or another IDE.
6. Load Data Files
   - Upload the necessary data files containing mRNA, miRNA, lncRNA, and TF molecules for the program to function.
  
_Check the 'Program Usage Steps' section to learn about the required formats of these files and how to upload them._

## Program Usage Steps
1. Start the _miRCuit_ program in Visual Studio Code (or another IDE such as PyCharm, Jupyter Notebook, etc.).
2.  Upload your mRNA, miRNA, lncRNA, and TF files that you want to analyze to the opened user interface.
### _Important Notes:_ 
* The files you upload must be in #CSV format# and consist of two columns. The first column should contain the names of your molecules under the heading "#Annotation#," and the second column should include the fold changes under the heading "#log2FoldChange#." Before uploading your files, please review the "Example Files" under the _miRCuit_ repository or check the "Examine the example file format" section in the interface (The p-value column is not required). 
* Please ensure that the capitalization and spacing match the example exactly.


