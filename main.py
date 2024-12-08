def printCards(kinds, suits):
    cards_num = len(kinds)
    suit_symbols = [''] * cards_num
    kind_symbols = [''] * cards_num
    for i in range(cards_num):
        suit_symbols[i] = ' '
        if suits[i] == 'club':
            suit_symbols[i] = '♣'
        elif suits[i] == 'diamond':
            suit_symbols[i] = '♦'
        elif suits[i] == 'heart':
            suit_symbols[i] = '♥'
        elif suits[i] == 'spade':
            suit_symbols[i] = '♠'
        
        kind_symbols[i] = ' '
        if kinds[i] == 1:
            kind_symbols[i] = 'A'
        elif kinds[i] >= 2 and kinds[i] <= 10:
            kind_symbols[i] = str(kinds[i])
        elif kinds[i] == 11:
            kind_symbols[i] = 'J'
        elif kinds[i] == 12:
            kind_symbols[i] = 'Q'
        elif kinds[i] == 13:
            kind_symbols[i] = 'K'

    print(' '.join(['╔═════════╗' for i in range(cards_num)]))
    print(' '.join([('║ 10      ║' if kinds[i] == 10 else f'║ {kind_symbols[i]:<2}      ║') for i in range(cards_num)]))
    print(' '.join(['║         ║' for i in range(cards_num)]))
    print(' '.join(['║         ║' for i in range(cards_num)]))
    print(' '.join([f'║    {suit_symbols[i]}    ║' for i in range(cards_num)]))
    print(' '.join(['║         ║' for i in range(cards_num)]))
    print(' '.join(['║         ║' for i in range(cards_num)]))
    print(' '.join([('║      10 ║' if kinds[i] == 10 else f'║       {kind_symbols[i]} ║') for i in range(cards_num)]))
    print(' '.join(['╚═════════╝' for i in range(cards_num)]))

# Запит у користувача
kinds_input = [1,2,3]
suits_input = ["spade", "diamond", "club"]
printCards(kinds_input, suits_input)
