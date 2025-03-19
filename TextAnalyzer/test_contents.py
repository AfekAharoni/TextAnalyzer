Q1_SENTENCES_CONTENT = """sentence
"Afek woke up to a bright morning in Bikini Bottom and found SpongeBob jumping with joy."
"Patrick look! We have a new guest!" shouted SpongeBob but Pat was too busy eating ice cream.
"Squidward looked at them in disgust, sighing, 'Another day of endless noise...'"
"Afekito laughed and decided to explore, but Bob insisted on giving him a super fun tour."
"By the end of the day, even Squiddy had to admit-it was the most interesting day in Bikini Bottom!"""
Q1_REMOVEWORDS_CONTENT = """words
a
an
the
and
or
to
for
in
of
but
by
on
at
with
even
"""
Q1_PEOPLE_CONTENT = """Name,Other Names
Afek,"Afekito, aFekUsh, ..pito,"
SpongeBob,Bob
Squidward,Squiddy
Patrick,"Pat, pAtRicK sTaR"""
Q1_SENTENCES_RESULT = {0: ['afek', 'woke', 'up', 'bright', 'morning', 'bikini', 'bottom', 'found', 'spongebob', 'jumping', 'joy'], \
                                   1: ['patrick', 'look', 'we', 'have', 'new', 'guest', 'shouted', 'spongebob', 'pat', 'was', 'too', 'busy', 'eating', 'ice', 'cream'], \
                                      2: ['squidward', 'looked', 'them', 'disgust', 'sighing', 'another', 'day', 'endless', 'noise'], \
                                          3: ['afekito', 'laughed', 'decided', 'explore', 'bob', 'insisted', 'giving', 'him', 'super', 'fun', 'tour'], \
                                            4: ['end', 'day', 'squiddy', 'had', 'admit', 'it', 'was', 'most', 'interesting', 'day', 'bikini', 'bottom']}
Q1_PEOPLE_RESULT = [[['afek'], [['afekito'], ['afekush'], ['pito']]], [['spongebob'], [['bob']]], [['squidward'], [['squiddy']]], [['patrick'], [['pat'], ['patrick', 'star']]]]
Q1_REMOVEWORDS_RESULT = ['a', 'an', 'the', 'and', 'or', 'to', 'for', 'in', 'of', 'but', 'by', 'on', 'at', 'with', 'even']
Q1_FINAL_RESULT = """{
    "Question 1": {
        "Processed Sentences": [
            [
                "afek",
                "woke",
                "up",
                "bright",
                "morning",
                "bikini",
                "bottom",
                "found",
                "spongebob",
                "jumping",
                "joy"
            ],
            [
                "patrick",
                "look",
                "we",
                "have",
                "new",
                "guest",
                "shouted",
                "spongebob",
                "pat",
                "was",
                "too",
                "busy",
                "eating",
                "ice",
                "cream"
            ],
            [
                "squidward",
                "looked",
                "them",
                "disgust",
                "sighing",
                "another",
                "day",
                "endless",
                "noise"
            ],
            [
                "afekito",
                "laughed",
                "decided",
                "explore",
                "bob",
                "insisted",
                "giving",
                "him",
                "super",
                "fun",
                "tour"
            ],
            [
                "end",
                "day",
                "squiddy",
                "had",
                "admit",
                "it",
                "was",
                "most",
                "interesting",
                "day",
                "bikini",
                "bottom"
            ]
        ],
        "Processed Names": [
            [
                [
                    "afek"
                ],
                [
                    [
                        "afekito"
                    ],
                    [
                        "afekush"
                    ],
                    [
                        "pito"
                    ]
                ]
            ],
            [
                [
                    "spongebob"
                ],
                [
                    [
                        "bob"
                    ]
                ]
            ],
            [
                [
                    "squidward"
                ],
                [
                    [
                        "squiddy"
                    ]
                ]
            ],
            [
                [
                    "patrick"
                ],
                [
                    [
                        "pat"
                    ],
                    [
                        "patrick",
                        "star"
                    ]
                ]
            ]
        ]
    }
}"""
Q1_FINAL_RESULT_AS_DICT = {
    "Question 1": {
        "Processed Sentences": [
            [
                "afek",
                "woke",
                "up",
                "bright",
                "morning",
                "bikini",
                "bottom",
                "found",
                "spongebob",
                "jumping",
                "joy"
            ],
            [
                "patrick",
                "look",
                "we",
                "have",
                "new",
                "guest",
                "shouted",
                "spongebob",
                "pat",
                "was",
                "too",
                "busy",
                "eating",
                "ice",
                "cream"
            ],
            [
                "squidward",
                "looked",
                "them",
                "disgust",
                "sighing",
                "another",
                "day",
                "endless",
                "noise"
            ],
            [
                "afekito",
                "laughed",
                "decided",
                "explore",
                "bob",
                "insisted",
                "giving",
                "him",
                "super",
                "fun",
                "tour"
            ],
            [
                "end",
                "day",
                "squiddy",
                "had",
                "admit",
                "it",
                "was",
                "most",
                "interesting",
                "day",
                "bikini",
                "bottom"
            ]
        ],
        "Processed Names": [
            [
                [
                    "afek"
                ],
                [
                    [
                        "afekito"
                    ],
                    [
                        "afekush"
                    ],
                    [
                        "pito"
                    ]
                ]
            ],
            [
                [
                    "spongebob"
                ],
                [
                    [
                        "bob"
                    ]
                ]
            ],
            [
                [
                    "squidward"
                ],
                [
                    [
                        "squiddy"
                    ]
                ]
            ],
            [
                [
                    "patrick"
                ],
                [
                    [
                        "pat"
                    ],
                    [
                        "patrick",
                        "star"
                    ]
                ]
            ]
        ]
    }
}
KSEQCOUNTER_RESULT = {
    1: {
        ('admit',): 1, ('afek',): 1, ('afekito',): 1, ('another',): 1, ('bikini',): 2, 
        ('bob',): 1, ('bottom',): 2, ('bright',): 1, ('busy',): 1, ('cream',): 1, 
        ('day',): 3, ('decided',): 1, ('disgust',): 1, ('eating',): 1, ('end',): 1, 
        ('endless',): 1, ('explore',): 1, ('found',): 1, ('fun',): 1, ('giving',): 1, 
        ('guest',): 1, ('had',): 1, ('have',): 1, ('him',): 1, ('ice',): 1, 
        ('insisted',): 1, ('interesting',): 1, ('it',): 1, ('joy',): 1, ('jumping',): 1, 
        ('laughed',): 1, ('look',): 1, ('looked',): 1, ('morning',): 1, ('most',): 1, 
        ('new',): 1, ('noise',): 1, ('pat',): 1, ('patrick',): 1, ('shouted',): 1, 
        ('sighing',): 1, ('spongebob',): 2, ('squiddy',): 1, ('squidward',): 1, 
        ('super',): 1, ('them',): 1, ('too',): 1, ('tour',): 1, ('up',): 1, 
        ('was',): 2, ('we',): 1, ('woke',): 1
    }, 
    2: {
        ('admit', 'it'): 1, ('afek', 'woke'): 1, ('afekito', 'laughed'): 1, 
        ('another', 'day'): 1, ('bikini', 'bottom'): 2, ('bob', 'insisted'): 1, 
        ('bottom', 'found'): 1, ('bright', 'morning'): 1, ('busy', 'eating'): 1, 
        ('day', 'bikini'): 1, ('day', 'endless'): 1, ('day', 'squiddy'): 1, 
        ('decided', 'explore'): 1, ('disgust', 'sighing'): 1, ('eating', 'ice'): 1, 
        ('end', 'day'): 1, ('endless', 'noise'): 1, ('explore', 'bob'): 1, 
        ('found', 'spongebob'): 1, ('fun', 'tour'): 1, ('giving', 'him'): 1, 
        ('guest', 'shouted'): 1, ('had', 'admit'): 1, ('have', 'new'): 1, 
        ('him', 'super'): 1, ('ice', 'cream'): 1, ('insisted', 'giving'): 1, 
        ('interesting', 'day'): 1, ('it', 'was'): 1, ('jumping', 'joy'): 1, 
        ('laughed', 'decided'): 1, ('look', 'we'): 1, ('looked', 'them'): 1, 
        ('morning', 'bikini'): 1, ('most', 'interesting'): 1, ('new', 'guest'): 1, 
        ('pat', 'was'): 1, ('patrick', 'look'): 1, ('shouted', 'spongebob'): 1, 
        ('sighing', 'another'): 1, ('spongebob', 'jumping'): 1, ('spongebob', 'pat'): 1, 
        ('squiddy', 'had'): 1, ('squidward', 'looked'): 1, ('super', 'fun'): 1, 
        ('them', 'disgust'): 1, ('too', 'busy'): 1, ('up', 'bright'): 1, 
        ('was', 'most'): 1, ('was', 'too'): 1, ('we', 'have'): 1, ('woke', 'up'): 1
    }
}
Q2_FINAL_RESULT = """{
    "Question 2": {
        "2-Seq Counts": [
            [
                "1_seq",
                [
                    [
                        "admit",
                        1
                    ],
                    [
                        "afek",
                        1
                    ],
                    [
                        "afekito",
                        1
                    ],
                    [
                        "another",
                        1
                    ],
                    [
                        "bikini",
                        2
                    ],
                    [
                        "bob",
                        1
                    ],
                    [
                        "bottom",
                        2
                    ],
                    [
                        "bright",
                        1
                    ],
                    [
                        "busy",
                        1
                    ],
                    [
                        "cream",
                        1
                    ],
                    [
                        "day",
                        3
                    ],
                    [
                        "decided",
                        1
                    ],
                    [
                        "disgust",
                        1
                    ],
                    [
                        "eating",
                        1
                    ],
                    [
                        "end",
                        1
                    ],
                    [
                        "endless",
                        1
                    ],
                    [
                        "explore",
                        1
                    ],
                    [
                        "found",
                        1
                    ],
                    [
                        "fun",
                        1
                    ],
                    [
                        "giving",
                        1
                    ],
                    [
                        "guest",
                        1
                    ],
                    [
                        "had",
                        1
                    ],
                    [
                        "have",
                        1
                    ],
                    [
                        "him",
                        1
                    ],
                    [
                        "ice",
                        1
                    ],
                    [
                        "insisted",
                        1
                    ],
                    [
                        "interesting",
                        1
                    ],
                    [
                        "it",
                        1
                    ],
                    [
                        "joy",
                        1
                    ],
                    [
                        "jumping",
                        1
                    ],
                    [
                        "laughed",
                        1
                    ],
                    [
                        "look",
                        1
                    ],
                    [
                        "looked",
                        1
                    ],
                    [
                        "morning",
                        1
                    ],
                    [
                        "most",
                        1
                    ],
                    [
                        "new",
                        1
                    ],
                    [
                        "noise",
                        1
                    ],
                    [
                        "pat",
                        1
                    ],
                    [
                        "patrick",
                        1
                    ],
                    [
                        "shouted",
                        1
                    ],
                    [
                        "sighing",
                        1
                    ],
                    [
                        "spongebob",
                        2
                    ],
                    [
                        "squiddy",
                        1
                    ],
                    [
                        "squidward",
                        1
                    ],
                    [
                        "super",
                        1
                    ],
                    [
                        "them",
                        1
                    ],
                    [
                        "too",
                        1
                    ],
                    [
                        "tour",
                        1
                    ],
                    [
                        "up",
                        1
                    ],
                    [
                        "was",
                        2
                    ],
                    [
                        "we",
                        1
                    ],
                    [
                        "woke",
                        1
                    ]
                ]
            ],
            [
                "2_seq",
                [
                    [
                        "admit it",
                        1
                    ],
                    [
                        "afek woke",
                        1
                    ],
                    [
                        "afekito laughed",
                        1
                    ],
                    [
                        "another day",
                        1
                    ],
                    [
                        "bikini bottom",
                        2
                    ],
                    [
                        "bob insisted",
                        1
                    ],
                    [
                        "bottom found",
                        1
                    ],
                    [
                        "bright morning",
                        1
                    ],
                    [
                        "busy eating",
                        1
                    ],
                    [
                        "day bikini",
                        1
                    ],
                    [
                        "day endless",
                        1
                    ],
                    [
                        "day squiddy",
                        1
                    ],
                    [
                        "decided explore",
                        1
                    ],
                    [
                        "disgust sighing",
                        1
                    ],
                    [
                        "eating ice",
                        1
                    ],
                    [
                        "end day",
                        1
                    ],
                    [
                        "endless noise",
                        1
                    ],
                    [
                        "explore bob",
                        1
                    ],
                    [
                        "found spongebob",
                        1
                    ],
                    [
                        "fun tour",
                        1
                    ],
                    [
                        "giving him",
                        1
                    ],
                    [
                        "guest shouted",
                        1
                    ],
                    [
                        "had admit",
                        1
                    ],
                    [
                        "have new",
                        1
                    ],
                    [
                        "him super",
                        1
                    ],
                    [
                        "ice cream",
                        1
                    ],
                    [
                        "insisted giving",
                        1
                    ],
                    [
                        "interesting day",
                        1
                    ],
                    [
                        "it was",
                        1
                    ],
                    [
                        "jumping joy",
                        1
                    ],
                    [
                        "laughed decided",
                        1
                    ],
                    [
                        "look we",
                        1
                    ],
                    [
                        "looked them",
                        1
                    ],
                    [
                        "morning bikini",
                        1
                    ],
                    [
                        "most interesting",
                        1
                    ],
                    [
                        "new guest",
                        1
                    ],
                    [
                        "pat was",
                        1
                    ],
                    [
                        "patrick look",
                        1
                    ],
                    [
                        "shouted spongebob",
                        1
                    ],
                    [
                        "sighing another",
                        1
                    ],
                    [
                        "spongebob jumping",
                        1
                    ],
                    [
                        "spongebob pat",
                        1
                    ],
                    [
                        "squiddy had",
                        1
                    ],
                    [
                        "squidward looked",
                        1
                    ],
                    [
                        "super fun",
                        1
                    ],
                    [
                        "them disgust",
                        1
                    ],
                    [
                        "too busy",
                        1
                    ],
                    [
                        "up bright",
                        1
                    ],
                    [
                        "was most",
                        1
                    ],
                    [
                        "was too",
                        1
                    ],
                    [
                        "we have",
                        1
                    ],
                    [
                        "woke up",
                        1
                    ]
                ]
            ]
        ]
    }
}"""
PEOPLE_MENTIONS_COUNTER = {'afek': 3, 'spongebob': 5, 'squidward': 2, 'patrick': 3}
Q3_FINAL_RESULT = """{
    "Question 3": {
        "Name Mentions": [
            [
                "afek",
                3
            ],
            [
                "patrick",
                3
            ],
            [
                "spongebob",
                5
            ],
            [
                "squidward",
                2
            ]
        ]
    }
}"""
KSEQ_QUERY_KEYS = """{
    "keys":[
		["afek", "woke"],
        ["spongebob", "jumping", "joy"],
        ["looked", "them"],
        ["insisted"],
        ["squiddy", "had", "admit", "it"],
        ["day", "bikini", "bottom"],
        ["bikini", "bottom"]
    ]
}"""
KSEQ_QUERY_KEYS_DICT = {
    "keys":[
		["afek", "woke"],
        ["spongebob", "jumping", "joy"],
        ["looked", "them"],
        ["insisted"],
        ["squiddy", "had", "admit", "it"],
        ["day", "bikini", "bottom"],
        ["bikini", "bottom"]
    ]
}
KSEQ_QUERY_KEYS_AFTER_ASSIGNMENT = {'keys': [['afek', 'woke'], ['spongebob', 'jumping', 'joy'], 
                                             ['looked', 'them'], ['insisted'], ['squiddy', 'had', 'admit', 'it'], 
                                             ['day', 'bikini', 'bottom'], ['bikini', 'bottom']]}
KSEQ_QUERY_KEYS_WITH_EMPTY_CELLS = """{
    "keys":[
		["afek", "woke"],
        ["spongebob", "jumping", "joy"],
        ["looked", "them"],
        ["insisted"],
        ["squiddy", "had", "admit", "it"],
        ["day", "bikini", "bottom"],
        ["bikini", "bottom", "   "],
        [""],
        ["", ""]
    ]
}"""
Q4_MATCHES_RESULT = {'afek woke': ['afek woke up bright morning bikini bottom found spongebob jumping joy'],
                      'bikini bottom': ['afek woke up bright morning bikini bottom found spongebob jumping joy', 'end day squiddy had admit it was most interesting day bikini bottom'], 
                      'day bikini bottom': ['end day squiddy had admit it was most interesting day bikini bottom'], 
                      'insisted': ['afekito laughed decided explore bob insisted giving him super fun tour'], 
                      'looked them': ['squidward looked them disgust sighing another day endless noise'], 
                      'spongebob jumping joy': ['afek woke up bright morning bikini bottom found spongebob jumping joy'],
                        'squiddy had admit it': ['end day squiddy had admit it was most interesting day bikini bottom']}
Q4_FINAL_RESULT = """{
    "Question 4": {
        "K-Seq Matches": [
            [
                "afek woke",
                [
                    [
                        "afek",
                        "woke",
                        "up",
                        "bright",
                        "morning",
                        "bikini",
                        "bottom",
                        "found",
                        "spongebob",
                        "jumping",
                        "joy"
                    ]
                ]
            ],
            [
                "bikini bottom",
                [
                    [
                        "afek",
                        "woke",
                        "up",
                        "bright",
                        "morning",
                        "bikini",
                        "bottom",
                        "found",
                        "spongebob",
                        "jumping",
                        "joy"
                    ],
                    [
                        "end",
                        "day",
                        "squiddy",
                        "had",
                        "admit",
                        "it",
                        "was",
                        "most",
                        "interesting",
                        "day",
                        "bikini",
                        "bottom"
                    ]
                ]
            ],
            [
                "day bikini bottom",
                [
                    [
                        "end",
                        "day",
                        "squiddy",
                        "had",
                        "admit",
                        "it",
                        "was",
                        "most",
                        "interesting",
                        "day",
                        "bikini",
                        "bottom"
                    ]
                ]
            ],
            [
                "insisted",
                [
                    [
                        "afekito",
                        "laughed",
                        "decided",
                        "explore",
                        "bob",
                        "insisted",
                        "giving",
                        "him",
                        "super",
                        "fun",
                        "tour"
                    ]
                ]
            ],
            [
                "looked them",
                [
                    [
                        "squidward",
                        "looked",
                        "them",
                        "disgust",
                        "sighing",
                        "another",
                        "day",
                        "endless",
                        "noise"
                    ]
                ]
            ],
            [
                "spongebob jumping joy",
                [
                    [
                        "afek",
                        "woke",
                        "up",
                        "bright",
                        "morning",
                        "bikini",
                        "bottom",
                        "found",
                        "spongebob",
                        "jumping",
                        "joy"
                    ]
                ]
            ],
            [
                "squiddy had admit it",
                [
                    [
                        "end",
                        "day",
                        "squiddy",
                        "had",
                        "admit",
                        "it",
                        "was",
                        "most",
                        "interesting",
                        "day",
                        "bikini",
                        "bottom"
                    ]
                ]
            ]
        ]
    }
}"""
Q5_FINAL_RESULT = """{
    "Question 5": {
        "Person Contexts and K-Seqs": [
            [
                "afek",
                [
                    [
                        "afek"
                    ],
                    [
                        "afek",
                        "woke"
                    ],
                    [
                        "afekito"
                    ],
                    [
                        "afekito",
                        "laughed"
                    ],
                    [
                        "bikini"
                    ],
                    [
                        "bikini",
                        "bottom"
                    ],
                    [
                        "bob"
                    ],
                    [
                        "bob",
                        "insisted"
                    ],
                    [
                        "bottom"
                    ],
                    [
                        "bottom",
                        "found"
                    ],
                    [
                        "bright"
                    ],
                    [
                        "bright",
                        "morning"
                    ],
                    [
                        "decided"
                    ],
                    [
                        "decided",
                        "explore"
                    ],
                    [
                        "explore"
                    ],
                    [
                        "explore",
                        "bob"
                    ],
                    [
                        "found"
                    ],
                    [
                        "found",
                        "spongebob"
                    ],
                    [
                        "fun"
                    ],
                    [
                        "fun",
                        "tour"
                    ],
                    [
                        "giving"
                    ],
                    [
                        "giving",
                        "him"
                    ],
                    [
                        "him"
                    ],
                    [
                        "him",
                        "super"
                    ],
                    [
                        "insisted"
                    ],
                    [
                        "insisted",
                        "giving"
                    ],
                    [
                        "joy"
                    ],
                    [
                        "jumping"
                    ],
                    [
                        "jumping",
                        "joy"
                    ],
                    [
                        "laughed"
                    ],
                    [
                        "laughed",
                        "decided"
                    ],
                    [
                        "morning"
                    ],
                    [
                        "morning",
                        "bikini"
                    ],
                    [
                        "spongebob"
                    ],
                    [
                        "spongebob",
                        "jumping"
                    ],
                    [
                        "super"
                    ],
                    [
                        "super",
                        "fun"
                    ],
                    [
                        "tour"
                    ],
                    [
                        "up"
                    ],
                    [
                        "up",
                        "bright"
                    ],
                    [
                        "woke"
                    ],
                    [
                        "woke",
                        "up"
                    ]
                ]
            ],
            [
                "patrick",
                [
                    [
                        "busy"
                    ],
                    [
                        "busy",
                        "eating"
                    ],
                    [
                        "cream"
                    ],
                    [
                        "eating"
                    ],
                    [
                        "eating",
                        "ice"
                    ],
                    [
                        "guest"
                    ],
                    [
                        "guest",
                        "shouted"
                    ],
                    [
                        "have"
                    ],
                    [
                        "have",
                        "new"
                    ],
                    [
                        "ice"
                    ],
                    [
                        "ice",
                        "cream"
                    ],
                    [
                        "look"
                    ],
                    [
                        "look",
                        "we"
                    ],
                    [
                        "new"
                    ],
                    [
                        "new",
                        "guest"
                    ],
                    [
                        "pat"
                    ],
                    [
                        "pat",
                        "was"
                    ],
                    [
                        "patrick"
                    ],
                    [
                        "patrick",
                        "look"
                    ],
                    [
                        "shouted"
                    ],
                    [
                        "shouted",
                        "spongebob"
                    ],
                    [
                        "spongebob"
                    ],
                    [
                        "spongebob",
                        "pat"
                    ],
                    [
                        "too"
                    ],
                    [
                        "too",
                        "busy"
                    ],
                    [
                        "was"
                    ],
                    [
                        "was",
                        "too"
                    ],
                    [
                        "we"
                    ],
                    [
                        "we",
                        "have"
                    ]
                ]
            ],
            [
                "spongebob",
                [
                    [
                        "afek"
                    ],
                    [
                        "afek",
                        "woke"
                    ],
                    [
                        "afekito"
                    ],
                    [
                        "afekito",
                        "laughed"
                    ],
                    [
                        "bikini"
                    ],
                    [
                        "bikini",
                        "bottom"
                    ],
                    [
                        "bob"
                    ],
                    [
                        "bob",
                        "insisted"
                    ],
                    [
                        "bottom"
                    ],
                    [
                        "bottom",
                        "found"
                    ],
                    [
                        "bright"
                    ],
                    [
                        "bright",
                        "morning"
                    ],
                    [
                        "busy"
                    ],
                    [
                        "busy",
                        "eating"
                    ],
                    [
                        "cream"
                    ],
                    [
                        "decided"
                    ],
                    [
                        "decided",
                        "explore"
                    ],
                    [
                        "eating"
                    ],
                    [
                        "eating",
                        "ice"
                    ],
                    [
                        "explore"
                    ],
                    [
                        "explore",
                        "bob"
                    ],
                    [
                        "found"
                    ],
                    [
                        "found",
                        "spongebob"
                    ],
                    [
                        "fun"
                    ],
                    [
                        "fun",
                        "tour"
                    ],
                    [
                        "giving"
                    ],
                    [
                        "giving",
                        "him"
                    ],
                    [
                        "guest"
                    ],
                    [
                        "guest",
                        "shouted"
                    ],
                    [
                        "have"
                    ],
                    [
                        "have",
                        "new"
                    ],
                    [
                        "him"
                    ],
                    [
                        "him",
                        "super"
                    ],
                    [
                        "ice"
                    ],
                    [
                        "ice",
                        "cream"
                    ],
                    [
                        "insisted"
                    ],
                    [
                        "insisted",
                        "giving"
                    ],
                    [
                        "joy"
                    ],
                    [
                        "jumping"
                    ],
                    [
                        "jumping",
                        "joy"
                    ],
                    [
                        "laughed"
                    ],
                    [
                        "laughed",
                        "decided"
                    ],
                    [
                        "look"
                    ],
                    [
                        "look",
                        "we"
                    ],
                    [
                        "morning"
                    ],
                    [
                        "morning",
                        "bikini"
                    ],
                    [
                        "new"
                    ],
                    [
                        "new",
                        "guest"
                    ],
                    [
                        "pat"
                    ],
                    [
                        "pat",
                        "was"
                    ],
                    [
                        "patrick"
                    ],
                    [
                        "patrick",
                        "look"
                    ],
                    [
                        "shouted"
                    ],
                    [
                        "shouted",
                        "spongebob"
                    ],
                    [
                        "spongebob"
                    ],
                    [
                        "spongebob",
                        "jumping"
                    ],
                    [
                        "spongebob",
                        "pat"
                    ],
                    [
                        "super"
                    ],
                    [
                        "super",
                        "fun"
                    ],
                    [
                        "too"
                    ],
                    [
                        "too",
                        "busy"
                    ],
                    [
                        "tour"
                    ],
                    [
                        "up"
                    ],
                    [
                        "up",
                        "bright"
                    ],
                    [
                        "was"
                    ],
                    [
                        "was",
                        "too"
                    ],
                    [
                        "we"
                    ],
                    [
                        "we",
                        "have"
                    ],
                    [
                        "woke"
                    ],
                    [
                        "woke",
                        "up"
                    ]
                ]
            ],
            [
                "squidward",
                [
                    [
                        "admit"
                    ],
                    [
                        "admit",
                        "it"
                    ],
                    [
                        "another"
                    ],
                    [
                        "another",
                        "day"
                    ],
                    [
                        "bikini"
                    ],
                    [
                        "bikini",
                        "bottom"
                    ],
                    [
                        "bottom"
                    ],
                    [
                        "day"
                    ],
                    [
                        "day",
                        "bikini"
                    ],
                    [
                        "day",
                        "endless"
                    ],
                    [
                        "day",
                        "squiddy"
                    ],
                    [
                        "disgust"
                    ],
                    [
                        "disgust",
                        "sighing"
                    ],
                    [
                        "end"
                    ],
                    [
                        "end",
                        "day"
                    ],
                    [
                        "endless"
                    ],
                    [
                        "endless",
                        "noise"
                    ],
                    [
                        "had"
                    ],
                    [
                        "had",
                        "admit"
                    ],
                    [
                        "interesting"
                    ],
                    [
                        "interesting",
                        "day"
                    ],
                    [
                        "it"
                    ],
                    [
                        "it",
                        "was"
                    ],
                    [
                        "looked"
                    ],
                    [
                        "looked",
                        "them"
                    ],
                    [
                        "most"
                    ],
                    [
                        "most",
                        "interesting"
                    ],
                    [
                        "noise"
                    ],
                    [
                        "sighing"
                    ],
                    [
                        "sighing",
                        "another"
                    ],
                    [
                        "squiddy"
                    ],
                    [
                        "squiddy",
                        "had"
                    ],
                    [
                        "squidward"
                    ],
                    [
                        "squidward",
                        "looked"
                    ],
                    [
                        "them"
                    ],
                    [
                        "them",
                        "disgust"
                    ],
                    [
                        "was"
                    ],
                    [
                        "was",
                        "most"
                    ]
                ]
            ]
        ]
    }
}"""
Q6_FINAL_RESULT = """{
    "Question 6": {
        "Pair Matches": [
            [
                [
                    "afek"
                ],
                [
                    "spongebob"
                ]
            ],
            [
                [
                    "afek"
                ],
                [
                    "squidward"
                ]
            ],
            [
                [
                    "spongebob"
                ],
                [
                    "squidward"
                ]
            ]
        ]
    }
}"""
Q6_FINAL_RESULT_WITH_CONNECTION = """{
    "Question 7": {
        "Pair Matches": [
            [
                "afek",
                "squideward",
                false
            ],
            [
                "patrick",
                "spongebob",
                true
            ],
            [
                "patrick",
                "squideward",
                false
            ]
        ]
    }
}"""
PEOPLE_CONNECTIONS = """{
    "keys": [
        ["afek", "squideward"],
        ["patrick", "spongebob"],
        ["patrick", "squideward"]
    ]
}"""
PEOPLE_CONNECTIONS_AS_DICT = {
    "keys": [
        ["afek", "squideward"],
        ["patrick", "spongebob"],
        ["patrick", "squideward"]
    ]
}
Q7_FINAL_RESULT = """{
    "Question 7": {
        "Pair Matches": [
            [
                "afek",
                "squideward",
                false
            ],
            [
                "patrick",
                "spongebob",
                false
            ],
            [
                "patrick",
                "squideward",
                false
            ]
        ]
    }
}"""
Q8_FINAL_RESULT = """{
    "Question 8": {
        "Pair Matches": [
            [
                "afek",
                "squideward",
                false
            ],
            [
                "patrick",
                "spongebob",
                false
            ],
            [
                "patrick",
                "squideward",
                false
            ]
        ]
    }
}"""
Q8_FINAL_RESULT_WITH_CONNECTION = """{
    "Question 8": {
        "Pair Matches": [
            [
                "afek",
                "squideward",
                false
            ],
            [
                "patrick",
                "spongebob",
                true
            ],
            [
                "patrick",
                "squideward",
                false
            ]
        ]
    }
}"""
NEIGHBORS_DICT = {'afek': ['squidward', 'spongebob'], 'squidward':['patrick']}
FIRST_PERSON = 'afek'
SECOND_PERSON = 'patrick'
Q9_GRAPH = {'afek woke up bright morning bikini bottom found spongebob jumping joy':
             ['patrick look we have new guest shouted spongebob pat was too busy eating ice cream', 'end day squiddy had admit it was most interesting day bikini bottom'], 
             'patrick look we have new guest shouted spongebob pat was too busy eating ice cream':
               ['afek woke up bright morning bikini bottom found spongebob jumping joy', 'end day squiddy had admit it was most interesting day bikini bottom'],
                 'end day squiddy had admit it was most interesting day bikini bottom':
                   ['afek woke up bright morning bikini bottom found spongebob jumping joy', 'patrick look we have new guest shouted spongebob pat was too busy eating ice cream', 'squidward looked them disgust sighing another day endless noise'], 
                   'squidward looked them disgust sighing another day endless noise': 
                   ['end day squiddy had admit it was most interesting day bikini bottom']}
Q9_SENTENCES = {'afek woke up bright morning bikini bottom found spongebob jumping joy':
                 ['afek', 'woke', 'up', 'bright', 'morning', 'bikini', 'bottom', 'found', 'spongebob', 'jumping', 'joy'], 
                 'patrick look we have new guest shouted spongebob pat was too busy eating ice cream': 
                 ['patrick', 'look', 'we', 'have', 'new', 'guest', 'shouted', 'spongebob', 'pat', 'was', 'too', 'busy', 'eating', 'ice', 'cream'],
                   'squidward looked them disgust sighing another day endless noise': 
                   ['squidward', 'looked', 'them', 'disgust', 'sighing', 'another', 'day', 'endless', 'noise'],
                     'afekito laughed decided explore bob insisted giving him super fun tour': 
                     ['afekito', 'laughed', 'decided', 'explore', 'bob', 'insisted', 'giving', 'him', 'super', 'fun', 'tour'],
                       'end day squiddy had admit it was most interesting day bikini bottom':
                         ['end', 'day', 'squiddy', 'had', 'admit', 'it', 'was', 'most', 'interesting', 'day', 'bikini', 'bottom']}
Q9_FINAL_RESULT = """{
    "Question 9": {
        "group Matches": [
            [
                "Group 1",
                [
                    [
                        "afekito",
                        "laughed",
                        "decided",
                        "explore",
                        "bob",
                        "insisted",
                        "giving",
                        "him",
                        "super",
                        "fun",
                        "tour"
                    ]
                ]
            ],
            [
                "Group 2",
                [
                    [
                        "afek",
                        "woke",
                        "up",
                        "bright",
                        "morning",
                        "bikini",
                        "bottom",
                        "found",
                        "spongebob",
                        "jumping",
                        "joy"
                    ],
                    [
                        "end",
                        "day",
                        "squiddy",
                        "had",
                        "admit",
                        "it",
                        "was",
                        "most",
                        "interesting",
                        "day",
                        "bikini",
                        "bottom"
                    ],
                    [
                        "patrick",
                        "look",
                        "we",
                        "have",
                        "new",
                        "guest",
                        "shouted",
                        "spongebob",
                        "pat",
                        "was",
                        "too",
                        "busy",
                        "eating",
                        "ice",
                        "cream"
                    ],
                    [
                        "squidward",
                        "looked",
                        "them",
                        "disgust",
                        "sighing",
                        "another",
                        "day",
                        "endless",
                        "noise"
                    ]
                ]
            ]
        ]
    }
}"""