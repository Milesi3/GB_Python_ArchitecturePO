from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


# Define a new game item, SilverReward
class SilverReward(IGameItem):
    def open(self):
        print('Silver')


# Define a new item generator, SilverGenerator
class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SilverReward()


if __name__ == '__main__':
    # Create a list of item generators including the new ones
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator()]

    # Open random chests 20 times
    for i in range(20):
        choice(lst).open_reward()