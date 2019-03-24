#!/usr/bin/env python
"""
    factory.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    :author: wongxinjie
    :copyright: (c) 2019, Tungee
    :date created: 2019-03-24 16:53
    :python version: Python3.6
"""
from abc import ABC, abstractmethod


class Room(ABC):

    @abstractmethod
    def connect(self, room2):
        pass


class MazeRoom(ABC):

    @abstractmethod
    def make_room(self):
        print('abstract make_room')
        pass

    def add_room(self, room):
        print("adding room", room)

    def __init__(self):
        room1 = self.make_room()
        room2 = self.make_room()
        room1.connect(room2)
        self.add_room(room1)
        self.add_room(room2)


class MagicMazeGame(MazeRoom):

    def make_room(self):
        return MagicRoom()


class MagicRoom(Room):

    def connect(self, room2):
        print("connecting magic room")


if __name__ == "__main__":
    game = MagicMazeGame()
