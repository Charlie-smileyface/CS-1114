class VideoGameStore:
    def __init__(self, owner, games):
        self.owner = owner
        self.games = games

    def __str__(self):
        welcome = f"Welcome to {self.owner}'s Video Game Store"
        title = "We have the following titles avaiable for you:"
        games = [f"{game[0]} by {game[1]}" for game in self.games]  ## 通过 list comprehension 重新定义一个 list，其中的每一个 element 都是一个 string
        
        return welcome + "\n" + title + "\n" + "\n".join(games) # 如果想print多行内容，只能使用换行符进行分割

    def buy_game(self,game):
        if game in self.games:
            self.games.remove(game)
            print(f"Thank you for your purchase {game[0]}")
        else:
            print(f"Sorry, we do not have {game[0]}")
    
    def view_games(self):
        print("Available tiles: ")
        for game in self.games:
            print(game[0]) # 这样的print 不能再括号里用 comprehension

def main():
    bobs_store = VideoGameStore("Bob", [("Overwatch", "Blizzard"), ("Super Meat Boy", "Team Meat"), ("Deltarune", "Toby Fox")])
    print(bobs_store)
    bobs_store.buy_game(("League of Legends", "Riot Games"))
    bobs_store.buy_game(("Overwatch", "Blizzard"))
    bobs_store.view_games()
main()


