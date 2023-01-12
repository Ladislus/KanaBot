from enum import Enum, auto


class AlphabetType(Enum):
    ALL = auto()
    SIMPLE = auto()
    COMPLEX = auto()


class CategoryType(Enum):
    DEFAULT = auto()
    K = auto()
    S = auto()
    T = auto()
    N = auto()
    H = auto()
    M = auto()
    R = auto()
    Y = auto()
    W = auto()


CharacterSetType: type = dict[str, str]
CharacterCategoryType: type = dict[CategoryType, CharacterSetType]
CharacterDictionaryType: type = dict[AlphabetType, CharacterCategoryType]

HIRAGANA_DICTIONARY: CharacterDictionaryType = {
    AlphabetType.SIMPLE: {
        CategoryType.DEFAULT: {
            'あ': 'A',
            'い': 'I',
            'う': 'U',
            'え': 'E',
            'お': 'O',
        },
        CategoryType.K: {
            'か': 'KA',
            'き': 'KI',
            'く': 'KU',
            'け': 'KE',
            'こ': 'KO',
        },
        CategoryType.S: {
            'さ': 'SA',
            'し': 'SHI',
            'す': 'SU',
            'せ': 'SE',
            'そ': 'SO',
        },
        CategoryType.T: {
            'た': 'TA',
            'ち': 'CHI',
            'つ': 'TSU',
            'て': 'TE',
            'と': 'TO',
        },
        CategoryType.N: {
            'な': 'NA',
            'に': 'NI',
            'ぬ': 'NU',
            'ね': 'NE',
            'の': 'NO',
        },
        CategoryType.H: {
            'は': 'HA',
            'ひ': 'HI',
            'ふ': 'FU',
            'へ': 'HE',
            'ほ': 'HO',
        },
        CategoryType.M: {
            'ま': 'MA',
            'み': 'MI',
            'む': 'MU',
            'め': 'ME',
            'も': 'MO',
        },
        CategoryType.R: {
            'ら': 'RA',
            'り': 'RI',
            'る': 'RU',
            'れ': 'RE',
            'ろ': 'RO',
        },
        CategoryType.Y: {
            'や': 'YA',
            'ゆ': 'YU',
            'よ': 'YO',
        },
        CategoryType.W: {
            'わ': 'WA',
            'ゐ': 'WI',
            'ゑ': 'WE',
            'を': 'WO',
            'ん': 'N',
        }
    },
    AlphabetType.COMPLEX: {}
}

KATAKANA_DICTIONARY: CharacterDictionaryType = {
    AlphabetType.SIMPLE: {},
    AlphabetType.COMPLEX: {}
}