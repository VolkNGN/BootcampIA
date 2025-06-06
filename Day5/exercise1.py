import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text = "   La pizza de la mama, la pizza des combats !!! "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)