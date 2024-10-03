from abc import ABC, abstractmethod


villains = {
    "Кострома": "Годзилла",
    "Токио": "Инопланетяне"
}


class Superhero(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass


class ChuckNorris(Superhero):
    def attack(self):
        return "PIU PIU"


class MediaChannel(ABC):
    def __init__(self, channel_name):
        self.channel_name = channel_name

    @abstractmethod
    def announce(self, message):
        pass


class Newspaper(MediaChannel):
    def announce(self, message):
        return f"Today in newspapers: {message}"


class TVChannel(MediaChannel):
    def announce(self, message):
        return f"Watch on the {self.channel_name}: {message}"


class Scenario:
    def __init__(self, superhero, city, media_channel):
        self.superhero = superhero
        self.city = city
        self.media_channel = media_channel

    def run(self):
        villain = villains.get(self.city, "Unknown villain")
        attack_message = self.superhero.attack()
        announcement = self.media_channel.announce(f"{self.superhero.name} saved the {self.city}!")

        print(f"{villain} stands near a skyscraper")
        print(attack_message)
        print(announcement)


if __name__ == "__main__":
    superhero = ChuckNorris("Chuck Norris")
    media_channel = TVChannel("first channel")
    scenario = Scenario(superhero, "Tokio", media_channel)
    scenario.run()

    print("--------------------")

    media_channel = Newspaper("newspapers")
    scenario = Scenario(superhero, "Costroma", media_channel)
    scenario.run()
