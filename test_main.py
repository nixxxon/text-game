import unittest
import mock
import main

class Testing(unittest.TestCase):

    @mock.patch('main.pick', mock.MagicMock(return_value=("Bob", 0)))
    def test_event_1_sets_player_name(self):
        wantPlayer = main.Player("Bob", [])
        wantState = main.State(wantPlayer)

        player = main.Player('', [])
        state = main.State(player)
        next, _state = main.event_1(state)

        self.assertEqual(next, main.event_2)
        self.assertEqual(_state.player.name, wantState.player.name)

    @mock.patch('main.pick', mock.MagicMock(return_value=("", 0)))
    def test_event_2_choose_right(self):
        player = main.Player('', [])
        state = main.State(player)
        next, _state = main.event_2(state)

        self.assertEqual(next, main.event_5)

    @mock.patch('main.pick', mock.MagicMock(return_value=("", 1)))
    def test_event_2_choose_left(self):
        player = main.Player('', [])
        state = main.State(player)
        next, _state = main.event_2(state)

        self.assertEqual(next, main.event_3)

if __name__ == '__main__':
    unittest.main()