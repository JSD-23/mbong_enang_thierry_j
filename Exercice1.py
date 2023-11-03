def lengthOfLastWord(s):
    # Votre code ici
    mots = s.split()
    if len(mots) == 0:
        return 0
    return len(mots[-1])