import pandas as pd
from googletrans import Translator

def transliterate_excel(input_file, output_file):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Initialize the translator
    translator = Translator()

    # Transliterate the text in all columns
    for column in df.columns:
        df[column] = df[column].apply(lambda x: translator.translate(x, src='en', dest='en').text if x is not None else '')

    # Save the translated DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

    print("Translation complete. Translated file saved as:", output_file)

# Prompt the user for input and output file paths
input_file = input("Enter the path to the input Excel file: ")
output_file = input("Enter the path to save the translated Excel file: ")

try:
    transliterate_excel(input_file, output_file)
except Exception as e:
    print("An error occurred during translation:", str(e))
