def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split()
    title_words = []
    for word in words:
        title_word = word.capitalize()
        title_words.append(title_word)
    return ' '.join(title_words)


