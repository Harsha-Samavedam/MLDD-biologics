# MLDD-biologics

Using a Novel Iterative Parametrization Method and Machine Learning Model To Classify DNA Binding Enzymes Through the Structure of the DNA Strand

[![Screenshot-2024-02-24-140430.png](https://i.postimg.cc/bw8K2BT5/Screenshot-2024-02-24-140430.png)](https://postimg.cc/BXYhrNR5)

### Previous Work

Automated classification methods such as DeepMind’s AlphaFold2 have been developed. AlphaFold2 creates 3D molecule representations from amino acid sequences.

### Our Approach

Our classification method leverages changes in DNA molecule geometry caused by proteins. We build upon existing methods such as CATH Protein Structure Classification and Families of Similarly Structured Proteins (FSSP) to automate classification using DNA strand geometry instead of alignment. This deepens our understanding of DNA-protein interactions, transcription, and regulation.

### Novelty

Our novel heuristic employs DNA molecule folding and geometry for classification. This fresh analysis allows for more precise protein study and accurate predictions of the effects on vital molecules in the body.

[![flc.png](https://i.postimg.cc/65pPWXbM/flc.png)](https://postimg.cc/7bj99pkz)

## Abstract

DNA Binding Enzymes play pivotal roles in driving fundamental biological processes, such as gene regulation, DNA repair, and replication. Understanding their structural characteristics is paramount for elucidating the mechanisms, interactions, and regulatory functions. In this study, we present a novel structural classification method for DNA Binding Enzymes in Homo sapiens, with a focus on the geometric aspects of the DNA strand, such as the macro-curvature, radius, and compression. By pinpointing and analyzing the phosphorus backbone of the DNA strand, we delved deeply into the common structural attributes shared across DNA strands when interacting with different enzymes, and we have determined varying structural features of each class of DNA-bound proteins. After collecting the essential structural data from the DNA strand, we are implementing multiple supervised learning methodologies. From the multiple models, we will determine the most accurate model to precisely map the correlation of specific structural features present in the DNA strand to the family of the bound protein. These findings can expand our comprehension of proteins and their functions, holding promise for applications in various biomedical domains, including drug development and pharmacotherapy.


## Methodology

- Extraction of Data
  - Data extracted from the RCSB PDB and MMDB for significant families in DNA Binding Enzymes.
  - Parameters inputted to select molecules containing DNA in Homo sapiens →  resulting list of PDB codes.
  - Duplicates were removed through an algorithm →  final dataset yielding 3,146 molecules from different DNA Binding enzyme families.
- Extraction of Phosphorus atoms
  - The phosphorus atoms in a given molecule were identified and extracted using PyMOL software 
  - Multiple DNA strands → saved to separate files with extracted adjacent phosphorus chains 
- Family Sorting
  - Used RCSB PDB GraphQL API to derive and organize DNA Binding Enzymes into families
  - BeautifulSoup web scraping script → find families not present in the API
[![steps.png](https://i.postimg.cc/6Qkwk392/steps.png)](https://postimg.cc/t1NLP9np)

**[1]** Extraction of Phosphorus atoms from DNA backbone in PyMOL  
**[2]** Selection of Phosphorus atoms from DNA backbone in PyMOL  
**[3]** Plotting of Phosphorus atoms from DNA backbone in Python  
**[4]** DNA helix parameterization of 1X9N with center of helix (red) and center of the DNA molecule (green)  

- Defining the Center + Radius of DNA
  - DNA separated into two helices with relatively equal length using the data of the phosphorus atoms
  - The length of the helix (Z) was measured by summing the distances between phosphorus atoms. Z was then divided by 2
  - Once repeated on the second helix, the average of the two midpoints was found to obtain the center of DNA
  - Distance from center to edge was calculated to be the radius of the DNA strand.
 
- Curve Fitting
  - Show in figure 1, curve fitting created defined coefficients and parameters that can be used as descriptions of DNA [6].
  - 3D curve fitting, shown in image 4, also provided coefficients which described the geometry of DNA and was used in the analysis.


## Results (Initial)

- Classification Models:
  - After running our code (which calculates the parameters described) on our existing database, we will have a list of CSV files that we can use to run our supervised learning models.
  - Allows us to effectively classify molecules based on the novel heuristic we defined.

**Figure 1:** Random Forest Feature Importance: optimized RF, and decision trees model → Accuracy: ~65%

**Figure 2:** Decision Trees Feature Importance: Decision trees feature importance → Accuracy: ~55%
[![Screenshot-2024-02-24-140056.png](https://i.postimg.cc/GmQxg716/Screenshot-2024-02-24-140056.png)](https://postimg.cc/ZWWNCLnL)

## References

<small>[1] Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S. A., Ballard, A. J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., … Hassabis, D. (2021). Highly accurate protein structure prediction with alphafold. Nature, 596(7873), 583–589. https://doi.org/10.1038/s41586-021-03819-2   
[2] H.M. Berman, J. Westbrook, Z. Feng, G. Gilliland, T.N. Bhat, H. Weissig, I.N. Shindyalov, P.E. Bourne. (2000) The Protein Data Bank Nucleic Acids Research, 28: 235-242.  
[3] Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.  
[4] Miki. (2016, July 20). Parametric curve fitting with iterative parametrization. MeshLogic. https://meshlogic.github.io/posts/ jupyter/curve-fitting/parametric-curve-fitting/   
[5] Schauperl, M., & Denny, R. A. (2022). AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges. Journal of chemical information and modeling, 62(13), 3142–3156. https://doi.org/10.1021/acs.jcim.2c00026  
[6] Warnecke, A., Sandalova, T., Achour, A. et al. PyTMs: a useful PyMOL plugin for modeling common post-translational modifications. BMC Bioinformatics 15, 370 (2014). https://doi.org/10.1186/s12859-014-0370-6  
[7] Yang, J.; Anishchenko, I. Improved protein structure prediction using predicted interresidue orientations. Proceedings of the National Academy of Sciences 2020, 117(3), 1496-1503. https://doi.org/10.1073/pnas.1914677117  
[8] Detlefsen, N.S., Hauberg, S. & Boomsma, W. Learning meaningful representations of protein sequences. Nat Commun 13, 1914 (2022). https://doi.org/10.1038/s41467-022-29443-w </small>
