# Lab 5.2: String Reverser and Analyzer

def reverse_string(text):
    return text[::-1]


def count_vowels_consonants(text):
    text = text.lower()
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


def is_palindrome(text):
    cleaned_text = ""
    for char in text.lower():
        if char.isalnum():
            cleaned_text += char

    return cleaned_text == cleaned_text[::-1]


# Main Program
phrase = input("Enter a phrase: ")

reversed_phrase = reverse_string(phrase)
print(f"Reversed phrase: {reversed_phrase}")

vowels, consonants = count_vowels_consonants(phrase)
print(f"Vowels: {vowels}, Consonants: {consonants}")

print(f"Is it a palindrome? {is_palindrome(phrase)}")