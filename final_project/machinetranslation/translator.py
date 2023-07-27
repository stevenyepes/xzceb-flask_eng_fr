"""
Module: translator.py

This module provides functions for translating text between English and French
using the MyMemoryTranslator API.

Functions:
    english_to_french(english_text):
        Translates English text to French using the MyMemoryTranslator API.

        Parameters:
            english_text (str): The input English text to be translated.

        Returns:
            str: The translated French text.

    french_to_english(french_text):
        Translates French text to English using the MyMemoryTranslator API.

        Parameters:
            french_text (str): The input French text to be translated.

        Returns:
            str: The translated English text.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using the MyMemoryTranslator API.

    Parameters:
        english_text (str): The input English text to be translated.

    Returns:
        str: The translated French text.
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using the MyMemoryTranslator API.

    Parameters:
        french_text (str): The input French text to be translated.

    Returns:
        str: The translated English text.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
