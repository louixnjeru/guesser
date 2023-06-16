# guesser

Guesser guesses a word in a given array in as few guesses as possible. It is modified from Leetcode problem 843 - Guess the Word.

The distances between words are precomputed and stored in a graph held in a dictionary before any words are guessed. The search is carried out using DFS to find words that are more similar to the current word.
