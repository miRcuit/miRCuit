# miRCuit : A Regulatory Circuit Analysis Tool 

miRCuit is a circuit analysis program designed to construct regulatory circuits. It presents a comprehensive framework for analyzing regulatory networks, specifically presenting a holistic approach to mRNA-miRNA-lncRNA-TF quadruple circuits. miRCuit has strategies that define all binary interactions to construct circuits, thereby presenting all relationships to users as intermediate outputs, thus providing them with different circuit types ranging from Type 1 to Type 8. Additionally, miRCuit offers users two special regulatory circuits: miRNA-dependent lncRNA regulatory circuits and TF-dependent lncRNA regulatory circuits. Throughout this process, it utilizes data obtained from 11 different databases (**_miRcode, DIANA TarBase, LncCeRBase, LncTarD, miRDB, miRTarBase, TFLink, TRRUST, RNA Interactome Database, TargetScan and TransmiR_**) to provide a comprehensive analysis.

## Features
- miRCuit is a circuit analysis program designed to construct regulatory circuits using Python. Developed as a .py file, it can be executed in environments, such as Visual Studio Code, Jupyter Notebook, etc. 
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
2. Upload your mRNA, miRNA, lncRNA, and TF expression files that you want to analyze to the opened user interface (Please refer to the section titled "Important Notes About Uploaded File Formats").
3. Determine a fold change value for each expression file you upload (mRNA, miRNA, lncRNA, and TF). This value represents the minimum fold change you wish to observe between the two groups you are comparing in your research (tumor/normal, treated/untreated).
4. If you want to perform enrichment analysis (GSEA) on the genes resulting from the analysis, you must check this option. By default, the program is set to "Do not perform GSEA".
5. Make sure all the boxes are checked, then click the "Start Analysis" button.

### _Important Notes About Uploaded File Formats:_ 
* The files you upload must be in #CSV format# and consist of two columns. The first column should contain the names of your molecules under the heading "**Annotation**," and the second column should include the fold changes under the heading "**log2FoldChange**."
* Before uploading your files, please review the "_Example_Files_" under the miRCuit repository or check the "_Examine the example file format_" section in the interface (The p-value column is not required). 
* Please ensure that the capitalization and spacing match the example exactly.

### Analysis Outputs
As a result of your analysis, you will receive three outputs: Circuits, molecular interactions, and GSEA results.
* Circuits: This section provides all the circuits obtained from your analysis. It includes _the eight different types of mRNA, miRNA, lncRNA, and TF regulatory circuits_ mentioned above, as well as _miRNA-dependent lncRNA regulatory circuits_ and _TF-dependent lncRNA regulatory circuits_, all organized in separate folders. Additionally, the outputs are provided in a visualized TXT format.
* Molecular interactions: The molecular interactions provided in visualized TXT format are presented in a tabular format in CSV, ready for further analysis.
* GSEA Results: This section provides a tabular format of the most enriched pathways resulting from the Gene Enrichment Analysis (GSEA). Additionally, it includes dot plots and network visuals of the pathways.

## Contributing
If you would like to contribute to the project or have suggestions, please send an email to begumkaraoglu93@gmail.com.

## License
This project is licensed under the GPL-3.0 license - see the [LICENSE](./LICENSE) file for details.

