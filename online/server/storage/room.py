class Room:
    def __init__(self, id, owner):
        self.owner = owner
        self.id = id
        self.players = {owner: owner}
        
    def get_id(self):
        return self.id
    
    def get_players(self):
        return self.players        
        
    def in_room(self, player: str):
        return player in self.players
    
    def add_player(self, player: str):
        if self.in_room(player):
            return False
        self.players[player] = player

    def remove_player(self, player: str):
        return self.players.pop(player, False)

    def get_owner(self):
        return self.owner

    def get_info(self):
        return {"id": self.id, "owner": self.owner, "players": self.players }