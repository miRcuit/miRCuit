import pandas as pd
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QComboBox, QFormLayout)
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QPixmap
import itertools
import gseapy as gp
from scipy.stats import ttest_ind
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
                             QComboBox, QFormLayout, QRadioButton, QButtonGroup,
                             QHBoxLayout, QButtonGroup, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QFont

class FileSelectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("miRcuit: A REGULATORY CIRCUIT ANALYSIS PROGRAM")
        self.setGeometry(100, 100, 600, 300)  # (x, y, genişlik, yükseklik)

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Program başlığı: Devre Analiz Programı
        self.program_title = QLabel("miRcuit: A Regulatory Circuit Analysis Program\n")
        self.program_title.setFont(QFont("Arial", 18, QFont.Bold))  # Daha büyük ve belirgin bir font ayarla
        self.program_title.setStyleSheet("color: #2F4F4F;")
        self.program_title.setAlignment(Qt.AlignCenter)  # Ortala
        self.main_layout.addWidget(self.program_title)


        # Başlıklar
        self.header_layout = QVBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        # Dosya Seçme Başlığının Üzerine Açıklama Yazısı
        self.file_selection_description = QLabel(
            """<p>miRCuit is a program designed to analyze the regulatory effects of miRNAs, lncRNAs, and transcription factors (TFs) on mRNAs. By comparing its analysis results with databases such as <b><i>miRcode, DIANA TarBase, LncCeRBase, LncTarD, miRDB, miRTarBase, TFLink, TRRUST, RNAInter, TargetScan, and TransmiR </i></b> miRCuit reveals the potential structure of molecular interactions, contributing to a deeper understanding of biological processes.</p>
            <p>Before running the program, you must select the necessary files for the analysis. Once the files are selected, the analysis will begin using the threshold values and other parameters you have specified. </p>"""
)       
        self.file_selection_description.setFont(QFont("Arial", 13))
        self.file_selection_description.setStyleSheet("color: #2F4F4F;")
        self.file_selection_description.setWordWrap(True)  # Uzun açıklamalar için satır kaydırma
        self.header_layout.addWidget(self.file_selection_description, alignment=Qt.AlignmentFlag.AlignTop)

        # Açıklamayı iki yana yasla
        self.file_selection_description.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.file_selection_description)

        # Ana başlık: Dosya Seçme
        self.file_selection_header = QLabel("\nFile Selection")
        self.file_selection_header.setFont(QFont("Arial", 14, QFont.Bold))
        self.file_selection_header.setStyleSheet("color: darkred;")
        self.header_layout.addWidget(self.file_selection_header)
   
        # Dosya Seçme Başlığının Altına Açıklama Yazısı
        self.file_selection_description = QLabel(
            "Please upload your research results for mRNA, miRNA, lncRNA, and TF expression files to the system in CSV format, ensuring that they include the <i>Gene Symbol</i> and <i>log2FoldChange</i> values.")
        self.file_selection_description.setOpenExternalLinks(True)
        self.file_selection_description.setFont(QFont("Arial", 13))
        self.file_selection_description.setStyleSheet("color: black;")
        self.file_selection_description.setWordWrap(True)  # Uzun açıklamalar için satır kaydırma
        self.header_layout.addWidget(self.file_selection_description, alignment=Qt.AlignmentFlag.AlignTop)

        # Dosya seçim başlıkları ve butonları
        self.file_selector_layout = QVBoxLayout()
        self.main_layout.addLayout(self.file_selector_layout)

        self.mrna_label = QLabel('<b>Please select the mRNA file.</b> <a href="file:/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/SS/mRNA.png">Click here </a> for the sample file format')
        self.mrna_label.setFont(QFont("Arial", 12))
        self.mrna_label.setStyleSheet("color: black")
        self.mrna_label.setOpenExternalLinks(True)
        self.file_selector_layout.addWidget(self.mrna_label)
        self.mrna_button = QPushButton("Select File")
        self.mrna_button.clicked.connect(self.select_mrna_file)
        self.file_selector_layout.addWidget(self.mrna_button)

        self.mirna_label = QLabel('<b>Please select the miRNA file.</b> <a href="file:/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/SS/miRNA.png">Click here </a> for the sample file format')
        self.mirna_label.setFont(QFont("Arial", 12))
        self.mirna_label.setStyleSheet("color: black")
        self.mirna_label.setOpenExternalLinks(True)
        self.file_selector_layout.addWidget(self.mirna_label)
        self.mirna_button = QPushButton("Select File")
        self.mirna_button.clicked.connect(self.select_mirna_file)
        self.file_selector_layout.addWidget(self.mirna_button)

        self.lncrna_label = QLabel('<b>Please select the lncRNA file.</b> <a href="file:/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/SS/lncRNA.png">Click here </a> for the sample file format')
        self.lncrna_label.setFont(QFont("Arial", 12))
        self.lncrna_label.setStyleSheet("color: black")
        self.lncrna_label.setOpenExternalLinks(True)
        self.file_selector_layout.addWidget(self.lncrna_label)
        self.lncrna_button = QPushButton("Select File")
        self.lncrna_button.clicked.connect(self.select_lncrna_file)
        self.file_selector_layout.addWidget(self.lncrna_button)

        self.tf_label = QLabel('<b>Please select the TF file.</b> <a href="file:/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/SS/TF.png">Click here </a> for the sample file format')
        self.tf_label.setFont(QFont("Arial", 12))
        self.tf_label.setStyleSheet("color: black")
        self.tf_label.setOpenExternalLinks(True)
        self.file_selector_layout.addWidget(self.tf_label)
        self.tf_button = QPushButton("Select File")
        self.tf_button.clicked.connect(self.select_tf_file)
        self.file_selector_layout.addWidget(self.tf_button)

        # Ana başlık: Threshold Belirleme
        self.threshold_header = QLabel("Threshold Setting")
        self.threshold_header.setFont(QFont("Arial", 14, QFont.Bold))
        self.threshold_header.setStyleSheet("color: darkred;")
        self.main_layout.addWidget(self.threshold_header)

        # Threshold Belirleme Başlığının Altına Açıklama Yazısı
        self.threshold_description = QLabel("Select the desired fold change threshold for all files to apply across your research groups.")
        self.threshold_description.setFont(QFont("Arial", 13))
        self.threshold_description.setStyleSheet("color: black;")
        self.threshold_description.setWordWrap(True)  # Uzun açıklamalar için satır kaydırma
        self.main_layout.addWidget(self.threshold_description)

        # Threshold değerleri için seçim kutuları
        self.threshold_layout = QFormLayout()
        self.main_layout.addLayout(self.threshold_layout)

        self.threshold_mrna = QComboBox()
        self.threshold_mrna.addItems(["","1.0", "1.5", "2.0", "2.5"])
        self.threshold_mrna.setFont(QFont("Arial", 13))
        self.threshold_layout.addRow(QLabel("mRNA Threshold:"), self.threshold_mrna)

        self.threshold_mirna = QComboBox()
        self.threshold_mirna.addItems(["","1.0", "1.5", "2.0", "2.5"])
        self.threshold_mirna.setFont(QFont("Arial", 13))        
        self.threshold_layout.addRow(QLabel("miRNA Threshold:"), self.threshold_mirna)

        self.threshold_lncrna = QComboBox()
        self.threshold_lncrna.addItems(["","1.0", "1.5", "2.0", "2.5"])
        self.threshold_lncrna.setFont(QFont("Arial", 13))        
        self.threshold_layout.addRow(QLabel("lncRNA Threshold:"), self.threshold_lncrna)

        self.threshold_tf = QComboBox()
        self.threshold_tf.addItems(["","1.0", "1.5", "2.0", "2.5"])
        self.threshold_tf.setFont(QFont("Arial", 13))        
        self.threshold_layout.addRow(QLabel("TF Threshold:"), self.threshold_tf)

        # Boşluk ekleme
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # GSEA Zenginleştirme Analizi başlığı
        self.gsea_header = QLabel("GSEA Enrichment Analysis")
        self.gsea_header.setFont(QFont("Arial", 14, QFont.Bold))
        self.gsea_header.setStyleSheet("color: darkred;")
        self.main_layout.addWidget(self.gsea_header)

        # GSEA Başlığının Altına Açıklama Yazısı
        self.gsea_description = QLabel("Please check the box to perform the GSEA enrichment analysis on your dataset using the MSigDB database.")
        self.gsea_description.setFont(QFont("Arial", 13))
        self.gsea_description.setStyleSheet("color: black;")
        self.gsea_description.setWordWrap(True)  # Uzun açıklamalar için satır kaydırma
        self.main_layout.addWidget(self.gsea_description)

        # GSEA analizi seçenekleri
        self.gsea_layout = QVBoxLayout()
        self.main_layout.addLayout(self.gsea_layout)

        self.gsea_option_group = QButtonGroup()
        self.gsea_yes = QRadioButton("Perform GSEA Enrichment Analysis")
        self.gsea_no = QRadioButton("Do not perform GSEA Enrichment Analysis")
        self.gsea_option_group.addButton(self.gsea_yes)
        self.gsea_option_group.addButton(self.gsea_no)

        self.gsea_layout.addWidget(self.gsea_yes)
        self.gsea_layout.addWidget(self.gsea_no)

        # Varsayılan olarak "GSEA zenginleştirme analizi yapılmasın" seçili
        self.gsea_no.setChecked(True)

        # Analiz başlatma butonu
        self.analyze_button = QPushButton("START ANALYSIS")
        self.analyze_button.setStyleSheet("color: darkred; font-size: 16px; font-weight: bold;")
        self.analyze_button.clicked.connect(self.start_analysis)
        self.main_layout.addWidget(self.analyze_button)

        # Uyarı etiketi
        self.warning_label = QLabel("")
        self.warning_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.warning_label.setStyleSheet("color: red;")
        self.main_layout.addWidget(self.warning_label)

        # Dosya yollarını saklamak için değişkenler
        self.mrna_file_path = ""
        self.mirna_file_path = ""
        self.lncrna_file_path = ""
        self.tf_file_path = ""

    def select_mrna_file(self):
        self.mrna_file_path, _ = QFileDialog.getOpenFileName(self, "Select mRNA File", "", "CSV Files (*.csv);;All Files (*)")
        if self.mrna_file_path:
            self.mrna_label.setText(f"<font color=#1E90FF>mRNA file selected: {self.mrna_file_path}</font>")
     

    def select_mirna_file(self):
        self.mirna_file_path, _ = QFileDialog.getOpenFileName(self, "Select miRNA File", "", "CSV Files (*.csv);;All Files (*)")
        if self.mirna_file_path:
            self.mirna_label.setText(f"<font color=#1E90FF>miRNA file selected: {self.mirna_file_path}</font>")
    

    def select_lncrna_file(self):
        self.lncrna_file_path, _ = QFileDialog.getOpenFileName(self, "Select lncRNA File", "", "CSV Files (*.csv);;All Files (*)")
        if self.lncrna_file_path:
            self.lncrna_label.setText(f"<font color=#1E90FF>lncRNA file selected: {self.lncrna_file_path}</font>")
   

    def select_tf_file(self):
        self.tf_file_path, _ = QFileDialog.getOpenFileName(self, "Select TF File", "", "CSV Files (*.csv);;All Files (*)")
        if self.tf_file_path:
            self.tf_label.setText(f"<font color=#1E90FF>TF file selected: {self.tf_file_path}</font>")



    def start_analysis(self):
        # Dosyaların tümü seçilmemişse uyarı ver
        if not all([self.mrna_file_path, self.mirna_file_path, self.lncrna_file_path, self.tf_file_path]):
            self.warning_label.setText("WARNING: Please select all files!")
            self.warning_label.setStyleSheet("color: #DC143C; font-size: 14px;")
            self.warning_label.setAlignment(Qt.AlignCenter)  # Merkezi hizala
            self.warning_label.setWordWrap(True)  # Kısıtlı alanlarda metni sar
            self.warning_label.setMinimumHeight(30)  # Uyarı etiketi için minimum yükseklik
            return
        
        # Threshold değerlerinin tümü girilmemişse uyarı ver
        if not all([self.threshold_mrna.currentText(), self.threshold_mirna.currentText(), self.threshold_lncrna.currentText(), self.threshold_tf.currentText()]):
            self.warning_label.setText("WARNING: Please enter all threshold values!")
            self.warning_label.setStyleSheet("color: #DC143C; font-size: 14px;")
            self.warning_label.setAlignment(Qt.AlignCenter)  # Merkezi hizala
            self.warning_label.setWordWrap(True)  # Kısıtlı alanlarda metni sar
            self.warning_label.setMinimumHeight(30)  # Uyarı etiketi için minimum yükseklik
            return


        if all([self.mrna_file_path, self.mirna_file_path, self.lncrna_file_path, self.tf_file_path]):
            self.warning_label.setText("The analysis has started; please wait...")
            self.warning_label.setStyleSheet("color: darkblue; font-style: italic; font-size: 14px;")
            self.warning_label.repaint() 
            QApplication.processEvents()  # UI'yi güncellemeye zorla
            thrs_mRNA = float(self.threshold_mrna.currentText())
            thrs_miRNA = float(self.threshold_mirna.currentText())
            thrs_lncRNA = float(self.threshold_lncrna.currentText())
            thrs_TF = float(self.threshold_tf.currentText())
            DevreAnalizProgramı(self.mrna_file_path, self.mirna_file_path, self.lncrna_file_path, self.tf_file_path, thrs_mRNA, thrs_miRNA, thrs_lncRNA, thrs_TF)
            self.warning_label.setText("The analysis is complete, and the files have been successfully generated!")
            self.warning_label.setStyleSheet("color: #6B8E23; font-style: bold; font-size: 16px;")
        else:
            self.warning_label.setText("WARNING: Please select all files and specify the threshold values.")
            self.warning_label.setStyleSheet("color: r#DC143C; font-style: bold; font-size: 16px;")

        # GSEA analizi seçeneğini kontrol etme
        if self.gsea_yes.isChecked():
            GSEA_Analiz(self.mrna_file_path, self.mirna_file_path, self.lncrna_file_path, self.tf_file_path, thrs_mRNA, thrs_miRNA, thrs_lncRNA, thrs_TF)

    def on_gsea_analysis_changed(self):
        # Eğer "GSEA zenginleştirme analizi yapılsın" seçiliyse, kısa alanı göster
        if self.gsea_yes_radio.isChecked():
            self.short_text_input.setVisible(True)
        else:
            self.short_text_input.setVisible(False)


def DevreAnalizProgramı(input_mRNA, input_miRNA, input_lncRNA, input_TF, thrs_mRNA, thrs_miRNA, thrs_lncRNA, thrs_TF):
    # Kütüphaneler
    lncRNA_miRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_miRNA_ikili_ilişkiler.csv").dropna()
    lncRNA_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    lncRNA_TF_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_TF_ikili_ilişkiler.csv", sep="\t").dropna()
    miRNA_lncRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_lncRNA_ikili_ilişkiler.csv").dropna()
    miRNA_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    miRNA_TF_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_TF_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_lncRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_lncRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_miRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_miRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()

    # Dosyaların oluşturulacağı dizinler
    folder_path_circuits_total = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/Total_analysis_circuits"
    os.makedirs(folder_path_circuits_total, exist_ok=True)
    folder_path_circuits_miRNA = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/miRNA_dependent_lncRNA_regulatory_circuits"
    os.makedirs(folder_path_circuits_miRNA, exist_ok=True)
    folder_path_circuits_TF = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/TF_dependent_lncRNA_regulatory_circuits"
    os.makedirs(folder_path_circuits_TF, exist_ok=True)
    folder_path_molecular_interaction_total = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/Total_analysis_interaction"
    os.makedirs(folder_path_molecular_interaction_total, exist_ok=True)
    folder_path_molecular_interaction_miRNA = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/miRNA_dependent_lncRNA_regulatory_interaction"
    os.makedirs(folder_path_molecular_interaction_miRNA, exist_ok=True)
    folder_path_molecular_interaction_TF = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/TF_dependent_lncRNA_regulatory_interaction"
    os.makedirs(folder_path_molecular_interaction_TF, exist_ok=True)

    # Dosyaların okunması
    raw_data_mRNA = pd.read_csv(input_mRNA, sep="\t").dropna()
    raw_data_miRNA = pd.read_csv(input_miRNA, sep="\t").dropna()
    raw_data_lncRNA = pd.read_csv(input_lncRNA).dropna()
    raw_data_TF = pd.read_csv(input_TF, sep="\t").dropna()

    # Belirlenen thrs değerine göre verilerin filtrelenmesi ve tek sütuna ("Annotation") indirgenmesi:
    mRNA_thrs = raw_data_mRNA[abs(raw_data_mRNA["log2FoldChange"]) >= thrs_mRNA]
    for index, row in mRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            mRNA_thrs.loc[index, "Regulation_mRNA"] = "+"
        else:
            mRNA_thrs.loc[index, "Regulation_mRNA"] = "-"
    mRNA_thrs = mRNA_thrs[["Annotation", "Regulation_mRNA"]]

    miRNA_thrs = raw_data_miRNA[abs(raw_data_miRNA["log2FoldChange"]) >= thrs_miRNA]
    for index, row in miRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            miRNA_thrs.loc[index, "Regulation_miRNA"] = "+"
        else:
            miRNA_thrs.loc[index, "Regulation_miRNA"] = "-"
    miRNA_thrs = miRNA_thrs[["Annotation", "Regulation_miRNA"]]

    lncRNA_thrs = raw_data_lncRNA[abs(raw_data_lncRNA["log2FoldChange"]) >= thrs_lncRNA]
    for index, row in lncRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            lncRNA_thrs.loc[index, "Regulation_lncRNA"] = "+"
        else:
            lncRNA_thrs.loc[index, "Regulation_lncRNA"] = "-"
    lncRNA_thrs = lncRNA_thrs[["Annotation", "Regulation_lncRNA"]]

    TF_thrs = raw_data_TF[abs(raw_data_TF["log2FoldChange"]) >= thrs_TF]
    for index, row in TF_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            TF_thrs.loc[index, "Regulation_TF"] = "+"
        else:
            TF_thrs.loc[index, "Regulation_TF"] = "-"
    TF_thrs = TF_thrs[["Annotation", "Regulation_TF"]]

    # Tüm hipotetik kombinasyonların belirlenmesi:
    ## miRNA-mRNA: 
    merge_miRNA_mRNA = (miRNA_thrs.merge(mRNA_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_mRNA = (merge_miRNA_mRNA[((merge_miRNA_mRNA["Regulation_miRNA"] == "+") & (merge_miRNA_mRNA["Regulation_mRNA"] == "-")) | ((merge_miRNA_mRNA["Regulation_miRNA"] == "-") & (merge_miRNA_mRNA["Regulation_mRNA"] == "+"))])
    filtered_miRNA_mRNA = filtered_miRNA_mRNA.iloc[:,[0, 2]]
    filtered_miRNA_mRNA.columns = ["miRNA", "mRNA"]  

    ## miRNA-lncRNA: 
    merge_miRNA_lncRNA = (miRNA_thrs.merge(lncRNA_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_lncRNA = (merge_miRNA_lncRNA[((merge_miRNA_lncRNA["Regulation_miRNA"] == "+") & (merge_miRNA_lncRNA["Regulation_lncRNA"] == "-")) | ((merge_miRNA_lncRNA["Regulation_miRNA"] == "-") & (merge_miRNA_lncRNA["Regulation_lncRNA"] == "+"))])
    filtered_miRNA_lncRNA = filtered_miRNA_lncRNA.iloc[:,[0, 2]]
    filtered_miRNA_lncRNA.columns = ["miRNA", "lncRNA"]  

    ## miRNA-TF: 
    merge_miRNA_TF = (miRNA_thrs.merge(TF_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_TF = (merge_miRNA_TF[((merge_miRNA_TF["Regulation_miRNA"] == "+") & (merge_miRNA_TF["Regulation_TF"] == "-")) | ((merge_miRNA_TF["Regulation_miRNA"] == "-") & (merge_miRNA_TF["Regulation_TF"] == "+"))])
    filtered_miRNA_TF = filtered_miRNA_TF.iloc[:,[0, 2]]
    filtered_miRNA_TF.columns = ["miRNA", "TF"]  

    ## lncRNA-miRNA: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = miRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_miRNA_df = ((pd.DataFrame(combinations, columns=["lncRNA", "miRNA"])).drop_duplicates())

    ## lncRNA-mRNA: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = mRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_mRNA_df = ((pd.DataFrame(combinations, columns=["lncRNA", "mRNA"])).drop_duplicates())

    ## lncRNA-TF: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = TF_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_TF_df = ((pd.DataFrame(combinations, columns=["lncRNA", "TF"])).drop_duplicates())

    ## TF-lncRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = lncRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_lncRNA_df = ((pd.DataFrame(combinations, columns=["TF", "lncRNA"])).drop_duplicates())

    ## TF-miRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = miRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_miRNA_df = ((pd.DataFrame(combinations, columns=["TF", "miRNA"])).drop_duplicates())

    ## TF-mRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = mRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_mRNA_df = ((pd.DataFrame(combinations, columns=["TF", "mRNA"])).drop_duplicates())

    # Gerçek listelerin elde edilmesi:
    miRNA_mRNA = pd.merge(miRNA_mRNA_library, filtered_miRNA_mRNA, on = ["miRNA", "mRNA"], how = "inner")
    miRNA_lncRNA = pd.merge(miRNA_lncRNA_library, filtered_miRNA_lncRNA, on = ["miRNA", "lncRNA"], how = "inner")
    miRNA_TF = pd.merge(miRNA_TF_library, filtered_miRNA_TF, on = ["miRNA", "TF"], how = "inner")
    lncRNA_miRNA = pd.merge(lncRNA_miRNA_library, lncRNA_miRNA_df, on = ["lncRNA", "miRNA"], how = "inner")
    lncRNA_mRNA = pd.merge(lncRNA_mRNA_library, lncRNA_mRNA_df, on = ["lncRNA", "mRNA"], how = "inner")
    lncRNA_TF = pd.merge(lncRNA_TF_library, lncRNA_TF_df, on = ["lncRNA", "TF"], how = "inner")
    TF_miRNA = pd.merge(TF_miRNA_library, TF_miRNA_df, on = ["TF", "miRNA"], how = "inner")
    TF_mRNA = pd.merge(TF_mRNA_library, TF_mRNA_df, on = ["TF", "mRNA"], how = "inner")
    TF_lncRNA = pd.merge(TF_lncRNA_library, TF_lncRNA_df, on = ["TF", "lncRNA"], how = "inner")

    # Devrelerin oluşturulması:
    # Devre 1:
    mRNA_miRNA_TF_tek_yön = (pd.merge(miRNA_mRNA, miRNA_TF, on = "miRNA", how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_tek_yön = mRNA_miRNA_TF_tek_yön[["TF", "miRNA", "mRNA"]]
    mRNA_miRNA_TF_tek_yön.to_csv("Output/Molecular_interactions/Total_analysis_interaction/1.TF_miRNA_mRNA_1.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/1.TF_miRNA_mRNA_1.txt", "w") as f:
        f.write(f"\tTF\t\t miRNA\t\t   mRNA\n\n")
        for index, row in mRNA_miRNA_TF_tek_yön.iterrows():
            f.write(f"\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\n")
    
    # Devre 2:
    mRNA_miRNA_TF_çift_yön_1 = (pd.merge(mRNA_miRNA_TF_tek_yön, TF_miRNA, on = ["TF", "miRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_çift_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/2.TF_miRNA_mRNA_2.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/2.TF_miRNA_mRNA_2.txt", "w") as f:
        f.write(f"\tTF\t\tmiRNA\t\tmRNA\n\n")
        for index, row in mRNA_miRNA_TF_çift_yön_1.iterrows():
            f.write(f"\n\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t   ------------->\n\n")
    
    # Devre 3:
    mRNA_miRNA_TF_çift_yön_2 = (pd.merge(mRNA_miRNA_TF_çift_yön_1, TF_mRNA, on = ["TF", "mRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_çift_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/3.TF_miRNA_mRNA_3.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/3.TF_miRNA_mRNA_3.txt", "w") as f:
        f.write(f"\tTF\t\tmiRNA\t\tmRNA\n\n")
        for index, row in mRNA_miRNA_TF_çift_yön_2.iterrows():
            f.write(f"\n\t  ------------------------------>\n\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t  ------------->\n\n")

    # Devre 4:
    mRNA_miRNA_TF_lncRNA_tek_yön_1 = (pd.merge(mRNA_miRNA_TF_çift_yön_2, TF_lncRNA, on = "TF", how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/4.lncRNA_TF_miRNA_mRNA_1.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/4.lncRNA_TF_miRNA_mRNA_1.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_1.iterrows():
            f.write(f"\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\n\n")

    # Devre 5:
    mRNA_miRNA_TF_lncRNA_tek_yön_2 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_1, miRNA_lncRNA, on = ["miRNA", "lncRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/5.lncRNA_TF_miRNA_mRNA_2.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/5.lncRNA_TF_miRNA_mRNA_2.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_2.iterrows():
            f.write(f"\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 6: 
    mRNA_miRNA_TF_lncRNA_tek_yön_3 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_2, lncRNA_mRNA, on = ["mRNA", "lncRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_3.to_csv("Output/Molecular_interactions/Total_analysis_interaction/6.lncRNA_TF_miRNA_mRNA_3.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/6.lncRNA_TF_miRNA_mRNA_3.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_3.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 7:
    mRNA_miRNA_TF_lncRNA_çift_yön_1 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_3, lncRNA_TF, on = ["lncRNA", "TF"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_çift_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/7.lncRNA_TF_miRNA_mRNA_4.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/7.lncRNA_TF_miRNA_mRNA_4.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_çift_yön_1.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - > {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 8:
    mRNA_miRNA_TF_lncRNA_çift_yön_2 = (pd.merge(mRNA_miRNA_TF_lncRNA_çift_yön_1, lncRNA_miRNA, on = ["lncRNA", "miRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_çift_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/8.lncRNA_TF_miRNA_mRNA_5.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/8.lncRNA_TF_miRNA_mRNA_4.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_çift_yön_2.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - > {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - >\n\n\n")

    ##### miRNA dependent lncRNA regulatory circuits

    lncRNA_miRNA_mRNA_tek_yön_1 = (pd.merge(miRNA_lncRNA, miRNA_mRNA, on = "miRNA", how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_tek_yön_2 = (pd.merge(lncRNA_miRNA_mRNA_tek_yön_1, lncRNA_miRNA, on = ["lncRNA", "miRNA"], how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_çift_yön = (pd.merge(lncRNA_miRNA_mRNA_tek_yön_2, lncRNA_mRNA, on = ["lncRNA", "mRNA"], how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_çift_yön = lncRNA_miRNA_mRNA_çift_yön[["lncRNA", "miRNA", "mRNA"]]
    lncRNA_miRNA_mRNA_çift_yön.to_csv("Output/Molecular_interactions/miRNA_dependent_lncRNA_regulatory_interaction/lncRNA_miRNA_mRNA.csv", sep = "\t", index = False)
    with open("Output/Circuits/miRNA_dependent_lncRNA_regulatory_circuits/lncRNA_miRNA_mRNA.txt", "w") as f:
        f.write(f"\tlncRNA\t\t   miRNA\t      mRNA\n\n")
        for index, row in lncRNA_miRNA_mRNA_çift_yön.iterrows():
            f.write(f"\n\t    - - - - - - - - - >\n\t{row['lncRNA']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t    - - - - - - - - - - - - - - - - - >\n\n")

    ##### TF dependent lncRNA regulation circuits
    
    lncRNA_TF_mRNA_tek_yön_1 = (pd.merge(TF_lncRNA, TF_mRNA, on = "TF", how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_tek_yön_2 = (pd.merge(lncRNA_TF_mRNA_tek_yön_1, lncRNA_TF, on = ["lncRNA", "TF"], how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_çift_yön = (pd.merge(lncRNA_TF_mRNA_tek_yön_2, lncRNA_mRNA, on = ["lncRNA", "mRNA"], how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_çift_yön = lncRNA_TF_mRNA_çift_yön[["lncRNA", "TF", "mRNA"]]
    lncRNA_TF_mRNA_çift_yön.to_csv("Output/Molecular_interactions/TF_dependent_lncRNA_regulatory_interaction/lncRNA_TF_mRNA.csv", sep = "\t", index = False)
    with open("Output/Circuits/TF_dependent_lncRNA_regulatory_circuits/lncRNA_TF_mRNA.txt", "w") as f:
        f.write(f"\tlncRNA\t\tTF\t\tmRNA\n\n")
        for index, row in lncRNA_TF_mRNA_çift_yön.iterrows():
            f.write(f"\n\t    - - - - - - - - >\n\t{row['lncRNA']} <------- {row['TF']} -------> {row['mRNA']}\n\t    - - - - - - - - - - - - - - - >\n\n")

def GSEA_Analiz(input_mRNA, input_miRNA, input_lncRNA, input_TF, thrs_mRNA, thrs_miRNA, thrs_lncRNA, thrs_TF):
    # Kütüphaneler
    lncRNA_miRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_miRNA_ikili_ilişkiler.csv").dropna()
    lncRNA_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    lncRNA_TF_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/lncRNA_TF_ikili_ilişkiler.csv", sep="\t").dropna()
    miRNA_lncRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_lncRNA_ikili_ilişkiler.csv").dropna()
    miRNA_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    miRNA_TF_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/miRNA_TF_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_lncRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_lncRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_miRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_miRNA_ikili_ilişkiler.csv", sep="\t").dropna()
    TF_mRNA_library = pd.read_csv("/Users/begumkaraoglu/Desktop/2.Optimizasyon/Kütüphaneler/TF_mRNA_ikili_ilişkiler.csv", sep="\t").dropna()

    # Dosyaların oluşturulacağı dizinler
    folder_path_circuits_total = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/Total_analysis_circuits"
    os.makedirs(folder_path_circuits_total, exist_ok=True)
    folder_path_circuits_miRNA = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/miRNA_dependent_lncRNA_regulatory_circuits"
    os.makedirs(folder_path_circuits_miRNA, exist_ok=True)
    folder_path_circuits_TF = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Circuits/TF_dependent_lncRNA_regulatory_circuits"
    os.makedirs(folder_path_circuits_TF, exist_ok=True)
    folder_path_molecular_interaction_total = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/Total_analysis_interaction"
    os.makedirs(folder_path_molecular_interaction_total, exist_ok=True)
    folder_path_molecular_interaction_miRNA = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/miRNA_dependent_lncRNA_regulatory_interaction"
    os.makedirs(folder_path_molecular_interaction_miRNA, exist_ok=True)
    folder_path_molecular_interaction_TF = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/Molecular_interactions/TF_dependent_lncRNA_regulatory_interaction"
    os.makedirs(folder_path_molecular_interaction_TF, exist_ok=True)
    folder_path_plots = "/Users/begumkaraoglu/Desktop/Devre_Analiz_Programı/Output/GSEA_Results/GSEA_Plots"
    os.makedirs(folder_path_plots, exist_ok=True)

    # Dosyaların okunması
    raw_data_mRNA = pd.read_csv(input_mRNA, sep="\t").dropna()
    raw_data_miRNA = pd.read_csv(input_miRNA, sep="\t").dropna()
    raw_data_lncRNA = pd.read_csv(input_lncRNA).dropna()
    raw_data_TF = pd.read_csv(input_TF, sep="\t").dropna()

    # Belirlenen thrs değerine göre verilerin filtrelenmesi ve tek sütuna ("Annotation") indirgenmesi:
    mRNA_thrs = raw_data_mRNA[abs(raw_data_mRNA["log2FoldChange"]) >= thrs_mRNA]
    for index, row in mRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            mRNA_thrs.loc[index, "Regulation_mRNA"] = "+"
        else:
            mRNA_thrs.loc[index, "Regulation_mRNA"] = "-"
    mRNA_thrs = mRNA_thrs[["Annotation", "Regulation_mRNA"]]

    miRNA_thrs = raw_data_miRNA[abs(raw_data_miRNA["log2FoldChange"]) >= thrs_miRNA]
    for index, row in miRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            miRNA_thrs.loc[index, "Regulation_miRNA"] = "+"
        else:
            miRNA_thrs.loc[index, "Regulation_miRNA"] = "-"
    miRNA_thrs = miRNA_thrs[["Annotation", "Regulation_miRNA"]]

    lncRNA_thrs = raw_data_lncRNA[abs(raw_data_lncRNA["log2FoldChange"]) >= thrs_lncRNA]
    for index, row in lncRNA_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            lncRNA_thrs.loc[index, "Regulation_lncRNA"] = "+"
        else:
            lncRNA_thrs.loc[index, "Regulation_lncRNA"] = "-"
    lncRNA_thrs = lncRNA_thrs[["Annotation", "Regulation_lncRNA"]]

    TF_thrs = raw_data_TF[abs(raw_data_TF["log2FoldChange"]) >= thrs_TF]
    for index, row in TF_thrs.iterrows():
        if (row["log2FoldChange"] >= 0):
            TF_thrs.loc[index, "Regulation_TF"] = "+"
        else:
            TF_thrs.loc[index, "Regulation_TF"] = "-"
    TF_thrs = TF_thrs[["Annotation", "Regulation_TF"]]

    # Tüm hipotetik kombinasyonların belirlenmesi:
    ## miRNA-mRNA: 
    merge_miRNA_mRNA = (miRNA_thrs.merge(mRNA_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_mRNA = (merge_miRNA_mRNA[((merge_miRNA_mRNA["Regulation_miRNA"] == "+") & (merge_miRNA_mRNA["Regulation_mRNA"] == "-")) | ((merge_miRNA_mRNA["Regulation_miRNA"] == "-") & (merge_miRNA_mRNA["Regulation_mRNA"] == "+"))])
    filtered_miRNA_mRNA = filtered_miRNA_mRNA.iloc[:,[0, 2]]
    filtered_miRNA_mRNA.columns = ["miRNA", "mRNA"]  

    ## miRNA-lncRNA: 
    merge_miRNA_lncRNA = (miRNA_thrs.merge(lncRNA_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_lncRNA = (merge_miRNA_lncRNA[((merge_miRNA_lncRNA["Regulation_miRNA"] == "+") & (merge_miRNA_lncRNA["Regulation_lncRNA"] == "-")) | ((merge_miRNA_lncRNA["Regulation_miRNA"] == "-") & (merge_miRNA_lncRNA["Regulation_lncRNA"] == "+"))])
    filtered_miRNA_lncRNA = filtered_miRNA_lncRNA.iloc[:,[0, 2]]
    filtered_miRNA_lncRNA.columns = ["miRNA", "lncRNA"]  

    ## miRNA-TF: 
    merge_miRNA_TF = (miRNA_thrs.merge(TF_thrs, how = "cross")).drop_duplicates()
    filtered_miRNA_TF = (merge_miRNA_TF[((merge_miRNA_TF["Regulation_miRNA"] == "+") & (merge_miRNA_TF["Regulation_TF"] == "-")) | ((merge_miRNA_TF["Regulation_miRNA"] == "-") & (merge_miRNA_TF["Regulation_TF"] == "+"))])
    filtered_miRNA_TF = filtered_miRNA_TF.iloc[:,[0, 2]]
    filtered_miRNA_TF.columns = ["miRNA", "TF"]  

    ## lncRNA-miRNA: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = miRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_miRNA_df = ((pd.DataFrame(combinations, columns=["lncRNA", "miRNA"])).drop_duplicates())

    ## lncRNA-mRNA: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = mRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_mRNA_df = ((pd.DataFrame(combinations, columns=["lncRNA", "mRNA"])).drop_duplicates())

    ## lncRNA-TF: 
    list1 = lncRNA_thrs["Annotation"].tolist()
    list2 = TF_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    lncRNA_TF_df = ((pd.DataFrame(combinations, columns=["lncRNA", "TF"])).drop_duplicates())

    ## TF-lncRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = lncRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_lncRNA_df = ((pd.DataFrame(combinations, columns=["TF", "lncRNA"])).drop_duplicates())

    ## TF-miRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = miRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_miRNA_df = ((pd.DataFrame(combinations, columns=["TF", "miRNA"])).drop_duplicates())

    ## TF-mRNA: 
    list1 = TF_thrs["Annotation"].tolist()
    list2 = mRNA_thrs["Annotation"].tolist()
    combinations = list(itertools.product(list1, list2))
    TF_mRNA_df = ((pd.DataFrame(combinations, columns=["TF", "mRNA"])).drop_duplicates())

    # Gerçek listelerin elde edilmesi:
    miRNA_mRNA = pd.merge(miRNA_mRNA_library, filtered_miRNA_mRNA, on = ["miRNA", "mRNA"], how = "inner")
    miRNA_lncRNA = pd.merge(miRNA_lncRNA_library, filtered_miRNA_lncRNA, on = ["miRNA", "lncRNA"], how = "inner")
    miRNA_TF = pd.merge(miRNA_TF_library, filtered_miRNA_TF, on = ["miRNA", "TF"], how = "inner")
    lncRNA_miRNA = pd.merge(lncRNA_miRNA_library, lncRNA_miRNA_df, on = ["lncRNA", "miRNA"], how = "inner")
    lncRNA_mRNA = pd.merge(lncRNA_mRNA_library, lncRNA_mRNA_df, on = ["lncRNA", "mRNA"], how = "inner")
    lncRNA_TF = pd.merge(lncRNA_TF_library, lncRNA_TF_df, on = ["lncRNA", "TF"], how = "inner")
    TF_miRNA = pd.merge(TF_miRNA_library, TF_miRNA_df, on = ["TF", "miRNA"], how = "inner")
    TF_mRNA = pd.merge(TF_mRNA_library, TF_mRNA_df, on = ["TF", "mRNA"], how = "inner")
    TF_lncRNA = pd.merge(TF_lncRNA_library, TF_lncRNA_df, on = ["TF", "lncRNA"], how = "inner")

    # Devrelerin oluşturulması:
    # Devre 1:
    mRNA_miRNA_TF_tek_yön = (pd.merge(miRNA_mRNA, miRNA_TF, on = "miRNA", how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_tek_yön = mRNA_miRNA_TF_tek_yön[["TF", "miRNA", "mRNA"]]
    mRNA_miRNA_TF_tek_yön.to_csv("Output/Molecular_interactions/Total_analysis_interaction/1.TF_miRNA_mRNA_1.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/1.TF_miRNA_mRNA_1.txt", "w") as f:
        f.write(f"\tTF\t\t miRNA\t\t   mRNA\n\n")
        for index, row in mRNA_miRNA_TF_tek_yön.iterrows():
            f.write(f"\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\n")
    
    # Devre 2:
    mRNA_miRNA_TF_çift_yön_1 = (pd.merge(mRNA_miRNA_TF_tek_yön, TF_miRNA, on = ["TF", "miRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_çift_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/2.TF_miRNA_mRNA_2.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/2.TF_miRNA_mRNA_2.txt", "w") as f:
        f.write(f"\tTF\t\tmiRNA\t\tmRNA\n\n")
        for index, row in mRNA_miRNA_TF_çift_yön_1.iterrows():
            f.write(f"\n\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t   ------------->\n\n")
    
    # Devre 3:
    mRNA_miRNA_TF_çift_yön_2 = (pd.merge(mRNA_miRNA_TF_çift_yön_1, TF_mRNA, on = ["TF", "mRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_çift_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/3.TF_miRNA_mRNA_3.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/3.TF_miRNA_mRNA_3.txt", "w") as f:
        f.write(f"\tTF\t\tmiRNA\t\tmRNA\n\n")
        for index, row in mRNA_miRNA_TF_çift_yön_2.iterrows():
            f.write(f"\n\t  ------------------------------>\n\t{row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t  ------------->\n\n")

    # Devre 4:
    mRNA_miRNA_TF_lncRNA_tek_yön_1 = (pd.merge(mRNA_miRNA_TF_çift_yön_2, TF_lncRNA, on = "TF", how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/4.lncRNA_TF_miRNA_mRNA_1.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/4.lncRNA_TF_miRNA_mRNA_1.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_1.iterrows():
            f.write(f"\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\n\n")

    # Devre 5:
    mRNA_miRNA_TF_lncRNA_tek_yön_2 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_1, miRNA_lncRNA, on = ["miRNA", "lncRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/5.lncRNA_TF_miRNA_mRNA_2.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/5.lncRNA_TF_miRNA_mRNA_2.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_2.iterrows():
            f.write(f"\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 6: 
    mRNA_miRNA_TF_lncRNA_tek_yön_3 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_2, lncRNA_mRNA, on = ["mRNA", "lncRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_tek_yön_3.to_csv("Output/Molecular_interactions/Total_analysis_interaction/6.lncRNA_TF_miRNA_mRNA_3.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/6.lncRNA_TF_miRNA_mRNA_3.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_tek_yön_3.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - - {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 7:
    mRNA_miRNA_TF_lncRNA_çift_yön_1 = (pd.merge(mRNA_miRNA_TF_lncRNA_tek_yön_3, lncRNA_TF, on = ["lncRNA", "TF"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_çift_yön_1.to_csv("Output/Molecular_interactions/Total_analysis_interaction/7.lncRNA_TF_miRNA_mRNA_4.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/7.lncRNA_TF_miRNA_mRNA_4.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_çift_yön_1.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - > {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - -\n\n\n")

    # Devre 8:
    mRNA_miRNA_TF_lncRNA_çift_yön_2 = (pd.merge(mRNA_miRNA_TF_lncRNA_çift_yön_1, lncRNA_miRNA, on = ["lncRNA", "miRNA"], how = "inner")).drop_duplicates()
    mRNA_miRNA_TF_lncRNA_çift_yön_2.to_csv("Output/Molecular_interactions/Total_analysis_interaction/8.lncRNA_TF_miRNA_mRNA_5.csv", sep = "\t", index = False)
    with open("Output/Circuits/Total_analysis_circuits/8.lncRNA_TF_miRNA_mRNA_4.txt", "w") as f:
        f.write(f"\t  lncRNA\t     TF\t\t  miRNA\t\t  mRNA\n\n")
        for index, row in mRNA_miRNA_TF_lncRNA_çift_yön_2.iterrows():
            f.write(f"\n\t    - - - - - - - - - - - - - - - - - - - - - - - - >\n\t\t\t      ------------------------------>\n\t{row['lncRNA']} < - - - > {row['TF']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t\t\t      --------------->\n\t    < - - - - - - - - - - - - - - - >\n\n\n")

    ##### miRNA dependent lncRNA regulatory circuits

    lncRNA_miRNA_mRNA_tek_yön_1 = (pd.merge(miRNA_lncRNA, miRNA_mRNA, on = "miRNA", how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_tek_yön_2 = (pd.merge(lncRNA_miRNA_mRNA_tek_yön_1, lncRNA_miRNA, on = ["lncRNA", "miRNA"], how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_çift_yön = (pd.merge(lncRNA_miRNA_mRNA_tek_yön_2, lncRNA_mRNA, on = ["lncRNA", "mRNA"], how = "inner")).drop_duplicates()
    lncRNA_miRNA_mRNA_çift_yön = lncRNA_miRNA_mRNA_çift_yön[["lncRNA", "miRNA", "mRNA"]]
    lncRNA_miRNA_mRNA_çift_yön.to_csv("Output/Molecular_interactions/miRNA_dependent_lncRNA_regulatory_interaction/lncRNA_miRNA_mRNA.csv", sep = "\t", index = False)
    with open("Output/Circuits/miRNA_dependent_lncRNA_regulatory_circuits/lncRNA_miRNA_mRNA.txt", "w") as f:
        f.write(f"\tlncRNA\t\t   miRNA\t      mRNA\n\n")
        for index, row in lncRNA_miRNA_mRNA_çift_yön.iterrows():
            f.write(f"\n\t    - - - - - - - - - >\n\t{row['lncRNA']} |------- {row['miRNA']} -------| {row['mRNA']}\n\t    - - - - - - - - - - - - - - - - - >\n\n")

    ##### TF dependent lncRNA regulation circuits
    
    lncRNA_TF_mRNA_tek_yön_1 = (pd.merge(TF_lncRNA, TF_mRNA, on = "TF", how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_tek_yön_2 = (pd.merge(lncRNA_TF_mRNA_tek_yön_1, lncRNA_TF, on = ["lncRNA", "TF"], how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_çift_yön = (pd.merge(lncRNA_TF_mRNA_tek_yön_2, lncRNA_mRNA, on = ["lncRNA", "mRNA"], how = "inner")).drop_duplicates()
    lncRNA_TF_mRNA_çift_yön = lncRNA_TF_mRNA_çift_yön[["lncRNA", "TF", "mRNA"]]
    lncRNA_TF_mRNA_çift_yön.to_csv("Output/Molecular_interactions/TF_dependent_lncRNA_regulatory_interaction/lncRNA_TF_mRNA.csv", sep = "\t", index = False)
    with open("Output/Circuits/TF_dependent_lncRNA_regulatory_circuits/lncRNA_TF_mRNA.txt", "w") as f:
        f.write(f"\tlncRNA\t\tTF\t\tmRNA\n\n")
        for index, row in lncRNA_TF_mRNA_çift_yön.iterrows():
            f.write(f"\n\t    - - - - - - - - >\n\t{row['lncRNA']} <------- {row['TF']} -------> {row['mRNA']}\n\t    - - - - - - - - - - - - - - - >\n\n")


    ### GSEA 
    TF_dep_TF = mRNA_miRNA_TF_lncRNA_tek_yön_1[["mRNA"]].rename(columns = {"mRNA": "Annotation"})
    TF_dep_TF = (pd.merge(TF_dep_TF, raw_data_mRNA, on = "Annotation", how = "inner")).drop_duplicates()
    TF_dep_TF = (TF_dep_TF.groupby("Annotation")["log2FoldChange"].mean().reset_index()).sort_values(by = "log2FoldChange", ascending = False)
    TF_dep_TF_gsea_results = gp.prerank(rnk = TF_dep_TF,
                          gene_sets = "MSigDB_Hallmark_2020",
                          permutation_num = 1000,
                          min_size = 2,
                          max_size = 5000,
                          outdir = "Output/GSEA_Results",
                          seed = 4)
    TF_dep_TF_results_df = TF_dep_TF_gsea_results.res2d
    TF_dep_TF_significant_genesets = TF_dep_TF_results_df[TF_dep_TF_results_df['FDR q-val'] < 0.25]
    TF_dep_TF_top_genesets = TF_dep_TF_significant_genesets.sort_values(by = "NES", ascending = False)
    TF_dep_TF_top_genesets_df = TF_dep_TF_top_genesets[["Term", "NES", "NOM p-val", "FDR q-val", "Lead_genes"]]
    TF_dep_TF_top_genesets_df.to_csv("Output/GSEA_Results/miRCuit_Analysis_Results_Top_Gene_Sets.csv", index = False)

    ### PLOTS
    # 1. GSEA PLOT
    import matplotlib.pyplot as plt  # plt'nin import edilmesi gerekiyor
    from gseapy import gseaplot, dotplot  
    terms = TF_dep_TF_gsea_results.res2d.Term
    axs = TF_dep_TF_gsea_results.plot(terms = terms[0:5],
                                              show_ranking = True,
                                              figsize = (3,4))
    # Grafiği kaydetme
    plt.savefig('Output/GSEA_Results/GSEA_Plots/GSEA_Plot.png', bbox_inches='tight')
    plt.close()  # Grafiği kapatmak, bellek temizliği sağlar
   
    # 2. DOT PLOT
    import matplotlib.pyplot as plt  # plt'nin import edilmesi gerekiyor
    from gseapy import gseaplot, dotplot
    ax = dotplot(TF_dep_TF_gsea_results.res2d,
             column="FDR q-val",
             title="MSigDB_Hallmark_2020",
             cmap= "viridis",
             size=6, # adjust dot size
             figsize=(4,5), 
             cutoff=0.25, 
             show_ring=False)
    plt.savefig('Output/GSEA_Results/GSEA_Plots/Dot_Plot.png', bbox_inches='tight')
    plt.close()  # Grafiği kapatmak, bellek temizliği sağlar

    # 3. NETWORK
    from gseapy import enrichment_map
    import matplotlib.pyplot as plt
    import networkx as nx
    

    nodes, edges = enrichment_map(TF_dep_TF_gsea_results.res2d)
    # build graph
    G = nx.from_pandas_edgelist(edges,
                            source='src_idx',
                            target='targ_idx',
                            edge_attr=['jaccard_coef', 'overlap_coef', 'overlap_genes'])   
    fig, ax = plt.subplots(figsize=(12, 12))

    # init node cooridnates
    pos=nx.layout.spiral_layout(G)

    # draw node
    nx.draw_networkx_nodes(G,
                       pos=pos,
                       cmap= 'RdYlBu',
                       node_color=list(nodes.NES),
                       node_size=list(nodes.Hits_ratio *1000))
    # Etiketleri hafifçe kaydırarak düğüm etiketlerini çizme
    labels = nodes.Term.to_dict()

    label_pos = {key: (value[0], value[1] + 0.05) for key, value in pos.items()}
    
    # draw node label
    nx.draw_networkx_labels(G,
                        pos=label_pos,
                        labels=labels,
                        font_size=8,  # Yazı boyutunu küçültme
                        verticalalignment='bottom')  # Yazıların düğümlerin altında hizalanmasını sağlama

    # draw edge
    edge_weight = nx.get_edge_attributes(G, 'jaccard_coef').values()
    nx.draw_networkx_edges(G,
                       pos=pos,
                       width=list(map(lambda x: x*10, edge_weight)),
                       edge_color='#CDDBD4',
                       ax=ax)     
    plt.savefig('Output/GSEA_Results/GSEA_Plots/Network.png', bbox_inches='tight')
    plt.close()  # Grafiği kapatmak, bellek temizliği sağlar

    # Analiz tamamlandığında kullanıcıya bilgi ver
    print("Analiz tamamlandı ve dosyalar başarıyla oluşturuldu.")


if __name__ == "__main__":
    app = QApplication([])
    window = FileSelectorWindow()
    window.show()
    app.exec_()


