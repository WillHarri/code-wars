#Solution 1
def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

#Other Solution
def greet(language):
    #your code here
    dict = {'english': 'Welcome',
            'czech': 'Vitejte',
            'danish': 'Velkomst',
            'dutch': 'Welkom',
            'estonian': 'Tere tulemast',
            'finnish': 'Tervetuloa',
            'flemish': 'Welgekomen',
            'french': 'Bienvenue',
            'german': 'Willkommen',
            'irish': 'Failte',
            'italian': 'Benvenuto',
            'latvian': 'Gaidits',
            'lithuanian': 'Laukiamas',
            'polish': 'Witamy',
            'spanish': 'Bienvenido',
            'swedish': 'Valkommen',
            'welsh': 'Croeso'}

    if language in dict.keys():
        return (dict[language])
    else:
        return ('Welcome')