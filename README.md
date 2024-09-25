# Find and Replace for Orthographic Normalization

This repository implements orthographic normalization using sequential find and replace mapping rules. Given a list of word documents and ordered mapping rules, our code outputs the .txt and .docx version of the input text(s) after applying the standardization rules.

We are currently working on a more accessible drag-and-drop for Cypriot Greek (CyGr) orthographic normalization. If you are interested in using this tool for CyGr, please contact us at rebeccapattichis2000@gmail.com.

## Setting Up

Before running the normalizer, use the following examples to create your own files:

1. **configs/cygr-config-example.json:** 
    - BOL_token/EOL_token (str or None): Set if you want to pad every input line before applying the mapping rules.
    - exceptions (list of str or None): Part of the CyGr implementation that requires removing the second stress of most words. This key represents the list of words that are exceptions to the second stress removal.
    - vowel_mappings (dict of str to str): Also part of the second stress removal implementation. The keys are all the vowels (lower and uppercase) accented, and the values are their unaccented versions.
    - rules_list (list of str): Ordered list of the Excel files representing the find and replace mapping rules. See (2) for more explanation.
    - documents (list of str): List of documents to normalize.
    - is_word_doc (bool): Set to true to indication we are dealing with .docx.
    - data_path (str): The path where the documents are stored.
    - rules_path (str): The path where the rule files are stored.
2. **spelling-normalizer/*.xlsx:** In our implementation, there are three Excel files corresponding to the rules outlined below. All files are expected to have two columns, titled 'Find' and 'Replace', respectively. 
    - **1-smooth**: Meant to remove any emojis, lowercase all letters, and remove any extra spaces.
    - **2-corrections**: The biggest rule file with the actual normalization rules. See our example file for guidance, or reach out through email if you have any questions.
    - **3-restore**: Reverses the smoothing rules by restoring the casing of letters.
3. **texts/*.docx:** Make sure that your input documents are formatted as a Word document (.docx).

## Running Code

Note that there are CyGr-specific implementations that you might want to edit in the NormalizeText class. Specifically, we assume there are only three normalization files. This means we:

- pad each line at the very beginning (first thing done during the first iteration of the for loop), and
- apply the second stress removal after the smoothing file (second iteration of the for loop).

If your use case is different, please change the for loop code in the `__FaR_helper__` function accordingly.

Once you've set up all other files and customized your code, run the following line of code in your terminal:

> `python findandreplace.py -c ../configs/{CONFIG_FILENAME}`