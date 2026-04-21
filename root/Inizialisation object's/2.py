class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self. goals  = 0
        self.assists = 0

    def score(self, goals = 1):
        self.goals += goals

    def make_assists(self, assists = 1):
        self.assists += assists

    def statistics(self):
        return f'{self.surname} {self.name} - goals: {self.goals}, assists: {self.assists}'

leo = SoccerPlayer('Leo', 'Messi')

leo.score(700)
leo.make_assists(500)
print(leo.statistics())
