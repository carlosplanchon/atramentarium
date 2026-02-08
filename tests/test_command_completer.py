#!/usr/bin/env python3
"""
Test suite for CommandCompleter class.
"""

import pytest
from unittest.mock import patch, MagicMock
from atramentarium.atramentarium import CommandCompleter


class TestCommandCompleter:
    """Test cases for CommandCompleter class."""

    def test_init_empty_list(self):
        """Test initialization with empty command list."""
        completer = CommandCompleter()
        assert completer._CommandCompleter__command_list == []
        assert completer.matches == []

    def test_init_with_commands(self):
        """Test initialization with command list."""
        commands = ["ALICE", "BOB", "CHARLIE"]
        completer = CommandCompleter(commands)
        assert completer._CommandCompleter__command_list == commands
        assert completer.matches == []

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_get_history_items_empty(self, mock_get_item, mock_get_length):
        """Test getting history items when history is empty."""
        mock_get_length.return_value = 0
        completer = CommandCompleter()
        history = completer.get_history_items()
        assert history == []

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_get_history_items_with_data(self, mock_get_item, mock_get_length):
        """Test getting history items with data."""
        mock_get_length.return_value = 3
        mock_get_item.side_effect = ["cmd1", "cmd2", "cmd3"]

        completer = CommandCompleter()
        history = completer.get_history_items()

        assert history == ["cmd1", "cmd2", "cmd3"]
        assert mock_get_item.call_count == 3

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_state_zero(self, mock_get_item, mock_get_length):
        """Test complete function with state=0 (first call)."""
        mock_get_length.return_value = 0
        commands = ["ALICE", "BOB", "CHARLIE"]
        completer = CommandCompleter(commands)

        result = completer.complete("A", 0)

        assert result == "ALICE"
        assert "ALICE" in completer.matches

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_multiple_matches(self, mock_get_item, mock_get_length):
        """Test complete function with multiple matches."""
        mock_get_length.return_value = 0
        commands = ["ALICE", "ALBERT", "BOB"]
        completer = CommandCompleter(commands)

        # First match
        result1 = completer.complete("AL", 0)
        assert result1 == "ALBERT"

        # Second match
        result2 = completer.complete("AL", 1)
        assert result2 == "ALICE"

        # No more matches
        result3 = completer.complete("AL", 2)
        assert result3 is None

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_no_matches(self, mock_get_item, mock_get_length):
        """Test complete function with no matches."""
        mock_get_length.return_value = 0
        commands = ["ALICE", "BOB"]
        completer = CommandCompleter(commands)

        result = completer.complete("X", 0)

        assert result is None
        assert completer.matches == []

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_with_history(self, mock_get_item, mock_get_length):
        """Test complete function includes history items."""
        mock_get_length.return_value = 2
        mock_get_item.side_effect = ["ALICE", "BOB"]
        commands = ["CHARLIE"]
        completer = CommandCompleter(commands)

        result = completer.complete("A", 0)

        assert result == "ALICE"
        assert "ALICE" in completer.matches

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_sorted_results(self, mock_get_item, mock_get_length):
        """Test that complete returns sorted results."""
        mock_get_length.return_value = 0
        commands = ["ZEBRA", "ALICE", "BOB"]
        completer = CommandCompleter(commands)

        completer.complete("", 0)  # Initialize matches

        # Verify matches are sorted
        assert completer.matches == sorted(completer.matches)

    @patch('readline.get_current_history_length')
    @patch('readline.get_history_item')
    def test_complete_filters_empty_strings(self, mock_get_item, mock_get_length):
        """Test that complete filters out empty strings."""
        mock_get_length.return_value = 2
        mock_get_item.side_effect = ["ALICE", ""]
        commands = ["BOB"]
        completer = CommandCompleter(commands)

        completer.complete("", 0)

        # Empty strings should be filtered out
        assert "" not in completer.matches
