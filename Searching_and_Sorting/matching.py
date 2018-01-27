"""
python implementation of basic matching algorithms
"""


class Match:
    """
    ways to make a happy match
    """

    @staticmethod
    def gale_shapley_match(men, women, preferences):
        """
        create stable marraiges. end adultery. be heteronormative.
        >>> men = ['tim', 'tom', 'kevin']
        >>> women = ['sarah', 'helen', 'alison']
        >>> preferences = {'tim' : ['sarah', 'helen', 'alison'],
        ...                'tom' : ['helen', 'sarah', 'alison'],
        ...                'kevin' : ['sarah', 'helen', 'alison'],
        ...                'sarah' : ['tom', 'tim', 'kevin'],
        ...                'helen' : ['tim', 'tom', 'kevin'],
        ...                'alison' : ['tim', 'tom', 'kevin']}
        >>> marraiges = Match.gale_shapley_match(men, women, preferences)
        >>> marraiges == {'tim': 'helen', 'tom': 'sarah', 'kevin': 'alison'}
        True
        """
        engagements = {}
        single_ladies = [woman for woman in women]
        while single_ladies:
            lady = single_ladies.pop()
            best_man = preferences[lady].pop(0)
            fiancee = engagements.get(best_man)
            if not fiancee:
                # he's single too!
                engagements[best_man] = lady
            elif preferences[best_man].index(lady) < preferences[best_man].index(fiancee):
                # time for some light adultery
                engagements[best_man] = lady
                if preferences[fiancee]:
                    single_ladies.append(fiancee)
            else:
                single_ladies.append(lady)
        marraiges = engagements
        return marraiges
