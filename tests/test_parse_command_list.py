#!/usr/bin/env python3
"""
Test suite for parse_command_list function.
"""

import pytest
from atramentarium.atramentarium import parse_command_list


class TestParseCommandList:
    """Test cases for parse_command_list function."""

    def test_empty_list(self):
        """Test parsing an empty list."""
        result = parse_command_list([])
        assert result == []

    def test_single_list_single_command(self):
        """Test parsing a single list with one command."""
        result = parse_command_list([["cmd1"]])
        assert result == ["cmd1"]

    def test_single_list_multiple_commands(self):
        """Test parsing a single list with multiple commands."""
        result = parse_command_list([["cmd1", "cmd2", "cmd3"]])
        assert result == ["cmd1", "cmd2", "cmd3"]

    def test_multiple_lists(self):
        """Test parsing multiple lists."""
        result = parse_command_list([["cmd1", "cmd2"], ["cmd3", "cmd4"]])
        assert result == ["cmd1", "cmd2", "cmd3", "cmd4"]

    def test_nested_empty_lists(self):
        """Test parsing with empty nested lists."""
        result = parse_command_list([[], ["cmd1"], []])
        assert result == ["cmd1"]

    def test_preserves_order(self):
        """Test that the function preserves command order."""
        input_list = [["first", "second"], ["third", "fourth"]]
        result = parse_command_list(input_list)
        assert result == ["first", "second", "third", "fourth"]

    def test_duplicate_commands(self):
        """Test parsing with duplicate commands."""
        result = parse_command_list([["cmd1", "cmd2"], ["cmd2", "cmd3"]])
        assert result == ["cmd1", "cmd2", "cmd2", "cmd3"]
        assert result.count("cmd2") == 2

    def test_various_command_types(self):
        """Test parsing with various command strings."""
        commands = [
            ["simple"],
            ["with-dash", "with_underscore"],
            ["UPPERCASE", "lowercase", "MixedCase"]
        ]
        result = parse_command_list(commands)
        expected = [
            "simple",
            "with-dash", "with_underscore",
            "UPPERCASE", "lowercase", "MixedCase"
        ]
        assert result == expected
