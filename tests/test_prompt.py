#!/usr/bin/env python3
"""
Test suite for prompt function.
"""

import pytest
from unittest.mock import patch, MagicMock, mock_open, call
from pathlib import Path
from atramentarium.atramentarium import prompt


class TestPrompt:
    """Test cases for prompt function."""

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_basic_execution(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test basic prompt execution with one command."""
        mock_exists.return_value = False
        mock_input.side_effect = ["test_command", KeyboardInterrupt()]

        processed_commands = []
        def process_func(cmd):
            processed_commands.append(cmd)

        with pytest.raises(KeyboardInterrupt):
            prompt(process_func, command_list=["test"])

        assert processed_commands == ["test_command"]
        mock_set_completer.assert_called_once()
        mock_parse_bind.assert_called_once_with("tab: complete")

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_with_existing_history(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test prompt execution with existing history file."""
        history_path = "/tmp/test.hist"
        mock_exists.return_value = True
        mock_input.side_effect = [KeyboardInterrupt()]

        with pytest.raises(KeyboardInterrupt):
            prompt(
                lambda x: None,
                history_filepath=history_path
            )

        mock_exists.assert_called_with(history_path)
        mock_read_hist.assert_called_once_with(history_path)

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_without_existing_history(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test prompt execution without existing history file."""
        mock_exists.return_value = False
        mock_input.side_effect = [KeyboardInterrupt()]

        with pytest.raises(KeyboardInterrupt):
            prompt(lambda x: None)

        mock_read_hist.assert_not_called()

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_writes_history_after_each_command(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test that history is written after each command."""
        history_path = "/tmp/test.hist"
        mock_exists.return_value = False
        mock_input.side_effect = ["cmd1", "cmd2", KeyboardInterrupt()]

        with pytest.raises(KeyboardInterrupt):
            prompt(
                lambda x: None,
                history_filepath=history_path
            )

        # Should write history twice (once per command)
        assert mock_write_hist.call_count == 2
        mock_write_hist.assert_called_with(history_path)

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_custom_prompt_string(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test prompt with custom prompt string."""
        mock_exists.return_value = False
        mock_input.side_effect = [KeyboardInterrupt()]

        with pytest.raises(KeyboardInterrupt):
            prompt(lambda x: None, prompt_string="custom> ")

        mock_input.assert_called_with("custom> ")

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_custom_parse_and_bind(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test prompt with custom parse_and_bind configuration."""
        mock_exists.return_value = False
        mock_input.side_effect = [KeyboardInterrupt()]

        with pytest.raises(KeyboardInterrupt):
            prompt(
                lambda x: None,
                parse_and_bind_init_line="set editing-mode vi"
            )

        mock_parse_bind.assert_called_once_with("set editing-mode vi")

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_with_command_list(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test prompt with a command list."""
        mock_exists.return_value = False
        mock_input.side_effect = [KeyboardInterrupt()]
        commands = ["ALICE", "BOB", "CHARLIE"]

        with pytest.raises(KeyboardInterrupt):
            prompt(lambda x: None, command_list=commands)

        # Verify that set_completer was called with a completer
        # that has the command list
        mock_set_completer.assert_called_once()

    @patch('atramentarium.atramentarium.exists')
    @patch('readline.write_history_file')
    @patch('readline.read_history_file')
    @patch('readline.parse_and_bind')
    @patch('readline.set_completer')
    @patch('builtins.input')
    def test_prompt_processes_multiple_commands(
        self,
        mock_input,
        mock_set_completer,
        mock_parse_bind,
        mock_read_hist,
        mock_write_hist,
        mock_exists
    ):
        """Test that multiple commands are processed correctly."""
        mock_exists.return_value = False
        mock_input.side_effect = ["cmd1", "cmd2", "cmd3", KeyboardInterrupt()]

        processed = []
        def process_func(cmd):
            processed.append(cmd)

        with pytest.raises(KeyboardInterrupt):
            prompt(process_func)

        assert processed == ["cmd1", "cmd2", "cmd3"]
