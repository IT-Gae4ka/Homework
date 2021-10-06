# Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet. Add the provided keyword at the begining of the alphabet. A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# Encryption: Keyword is "Crypto"

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:

# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"

from collections import deque

class Cipher():
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
	def __init__(self, cipher_word):
		self.cipher_word = cipher_word

	def delete_similar_letters(self):
		self.alphabet_list = list(self.alphabet)
		self.cipher_word_list = list(self.cipher_word)
		for letter in self.cipher_word_list:
			if letter in self.alphabet_list:
				self.alphabet_list.remove(letter)
		return self.alphabet_list

	def add_cipher_word(self):
		self.delete_similar_letters()
		self.alphabet_ciphered = deque(self.alphabet_list)
		self.alphabet_ciphered.extendleft(reversed(self.cipher_word_list))
		self.alphabet_ciphered_list = list(self.alphabet_ciphered)
		return self.alphabet_ciphered_list
		
	def encode(self, text):
		self.add_cipher_word()
		self.encoded_text_list = []
		self.text = text
		self.full_alphabet_list = list(self.alphabet)
		self.whitespace = ' '
		for letter in self.text:
			if letter.isupper():
				letter = letter.lower()
				if letter in self.full_alphabet_list:
					i = self.full_alphabet_list.index(letter)
					upper_letter = self.alphabet_ciphered_list[i].upper()
					self.encoded_text_list.append(upper_letter)
			else:
				if letter in self.full_alphabet_list:
					i = self.full_alphabet_list.index(letter)
					self.encoded_text_list.append(self.alphabet_ciphered_list[i])
			if letter in self.whitespace:
					self.encoded_text_list.append(self.whitespace)
		self.encoded_text = ''.join(self.encoded_text_list)
		return self.encoded_text

	def decode(self, text):
			self.add_cipher_word()
			self.decoded_text_list = []
			self.text = text
			self.full_alphabet_list = list(self.alphabet)
			self.whitespace = ' '
			for letter in self.text:
				if letter.isupper():
					letter = letter.lower()
					if letter in self.alphabet_ciphered_list:
						i = self.alphabet_ciphered_list.index(letter)
						upper_letter = self.full_alphabet_list[i].upper()
						self.decoded_text_list.append(upper_letter)
				else:
					if letter in self.alphabet_ciphered_list:
						i = self.alphabet_ciphered_list.index(letter)
						self.decoded_text_list.append(self.full_alphabet_list[i])
				if letter in self.whitespace:
						self.decoded_text_list.append(self.whitespace)
			self.decoded_text = ''.join(self.decoded_text_list)
			return self.decoded_text


cipher = Cipher("crypto")	

print(cipher.decode("Fjedhc dn atidsn"))
print(cipher.encode("Hello world"))
