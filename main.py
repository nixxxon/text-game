from typing import Tuple
from pick import pick

class Object:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name: str, backpack: [Object]):
        self.name = name
        self.backpack = backpack

class State:
    def __init__(self, player: Player):
        self.player = player

def event_1(state: State) -> Tuple[callable, State]:
    title = 'Please choose a name '
    options = ['Bob', 'Maria']
    option, index = pick(options, title, min_selection_count=1)
    state.player.name = option
    return event_2, state

def event_2(state: State) -> Tuple[callable, State]:
    title = 'Hi {} '.format(state.player.name)
    options = ['Go Right', 'Go Left']
    option, index = pick(options, title, min_selection_count=1)

    if index == 0:
        return event_5, state

    return event_3, state

def event_3(state: State) -> Tuple[callable, State]:
    title = 'You found a key '
    options = ['Pickup', 'Leave']
    option, index = pick(options, title, min_selection_count=1)

    if index == 0:
        state.player.backpack.append(Object('Key'))

    return event_4, state

def event_4(state: State) -> Tuple[callable, State]:
    print(state.player.backpack)
    print('Goodbye')
    return None, state

def event_5(state: State) -> Tuple[callable, State]:
    title = 'Left '
    options = ['Go Right', 'Go Left']
    option, index = pick(options, title, min_selection_count=1)
    return None, state

def run(event, state) -> Tuple[callable, State]:
    next, _state = event(state)

    if next == None:
        return

    return run(next, _state)

if __name__ == '__main__':
    player = Player('', [])
    state = State(player)
    run(event_1, state)

