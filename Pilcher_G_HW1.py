# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 08:27:44 2016

@author: gs13macpro
"""

def reverse(String): #Problem 7
    """
    This function reverses a string, e.g. "abcd" to "dcba"
    
    Parameter:
    A string
    
    Returns:
    The reverse of a string
    """
    #get the length of the string and subtract 1
    #remember that strings are indexed from 0
    end_of_str = len(String)-1
    revStr = '' ## Initialize the reversed string to null
    for Char in String:
        #start at the end of the string and work back to the
        #beginning to build the reversed string
        revStr = revStr + String[end_of_str]
        end_of_str = end_of_str - 1
    return revStr


def is_palindrome(input_word=""):
    """
    This function, is_palindrome(), recognizes 
    palindromes (i.e. words that look the same written backwards). 
    For example, is_palindrome("radar")should return True. 

    Parameters:
    input_word - any word with alphabetic characters
    
    Returns: 
    True is the word is a Palindrome, False otherwise

    gp-2015
    """
    ## Take care of mixed case, make sure that the word only contains
    ## alpha characters (no numbers, punctuation, etc.) and strip out
    ## any spaces.
    
    palindrome = False #Initialize our return variable to False
    
    input_word = input_word.upper() # Take care of mixed case by upper
                                    # casing the word
    
    input_word = input_word.replace(" ", "") # Take care of spaces
    
    if not input_word.isalpha(): # Return false if there are any numbers
                                 # in the word
        return palindrome
        
    if reverse(input_word) == input_word:
        palindrome = True
    
    return palindrome 