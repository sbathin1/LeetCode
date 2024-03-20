def maxVowels(s, k):
    vowels = set('aeiou')

    current_vowel_count = sum(char in vowels for char in s[:k])

    max_vowel_count = current_vowel_count

    for i in range(k, len(s)):
        current_vowel_count += s[i] in vowels
        current_vowel_count -= s[i - k] in vowels

        max_vowel_count = max(max_vowel_count, current_vowel_count)

    print(max_vowel_count)


s = "leetcode"
k = 3

maxVowels(s, k)