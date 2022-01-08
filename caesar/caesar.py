def verschluesselnEntschluesselnZeichen(klartextZeichen, verschieben, modus='verschluesseln'):
    if klartextZeichen.isalpha():
        ersterLexikographischerBuchstabe = 'a'
        if klartextZeichen.isupper():
            ersterLexikographischerBuchstabe = 'A'
        alteZeichenposition = ord(klartextZeichen) - ord(ersterLexikographischerBuchstabe)

        if modus == 'verschluesseln':
            neueZeichenPosition = (alteZeichenposition + verschieben) % 26
        else:
            neueZeichenPosition = (alteZeichenposition - verschieben) % 26
        return chr(neueZeichenPosition + ord(ersterLexikographischerBuchstabe))
    return klartextZeichen

def verschluesseln(klartext, verschiebung):
    verschluesselungsText = ''
    for klartextZeichen in klartext:
        verschluesselungsText += verschluesselnEntschluesselnZeichen(klartextZeichen, verschiebung)
    return verschluesselungsText

def entschluesseln(verschluesselungsText, verschiebung):
    klarText = ''
    for ciphertextChar in verschluesselungsText:
        klarText += verschluesselnEntschluesselnZeichen(ciphertextChar, verschiebung, modus='entschluesseln')
    return klarText

print("Wilkommen bei der Post von Caesar.")
klarText = input('Gebe deine Nachricht ein: ')
verschiebung = int(input('Um wie viele stellen, soll deine Nachricht verschoben werden?: '))
verschluesselungsText = verschluesseln(klarText, verschiebung)
entschluesselterKlartext = entschluesseln(verschluesselungsText, verschiebung)
print(f'Verschlüsselungstext: {verschluesselungsText}')
print(f'Entschlüsselter Klartext: {entschluesselterKlartext}')
print("Die Post von Caesar freut sich auf deinen nächsten Besuch.")