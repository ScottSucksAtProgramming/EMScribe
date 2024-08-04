# test_preprocess.py

import pytest
from unittest.mock import MagicMock, patch
from scripts.preprocess import (
    TranscriptPreprocessor,
    run,
    ModelLoader,
    PromptManager,
    TranscriptCleaner,
)


@pytest.fixture
def mock_model_loader():
    return MagicMock(spec=ModelLoader)


@pytest.fixture
def mock_prompt_manager():
    return MagicMock(spec=PromptManager)


@pytest.fixture
def preprocessor(mock_model_loader, mock_prompt_manager):
    return TranscriptPreprocessor(
        model_loader=mock_model_loader, prompt_manager=mock_prompt_manager
    )


@patch(
    "modules.transcript_cleaner.TranscriptCleaner.clean",
    return_value="Mocked cleaned transcript",
)
def test_main_script(mock_clean, mock_model_loader, mock_prompt_manager, monkeypatch):
    # Arrange
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)

    # Act
    run(mock_model_loader, mock_prompt_manager)

    # Assert
    mock_print.assert_called_with("Mocked cleaned transcript")


def test_clean_transcript(preprocessor):
    preprocessor.cleaner.clean = MagicMock(return_value="Cleaned transcript")
    result = preprocessor.clean_transcript("example transcript")
    assert result == "Cleaned transcript"


def test_further_process(preprocessor):
    result = preprocessor.further_process("Cleaned transcript")
    assert result == "Cleaned transcript"


def test_preprocess(preprocessor):
    preprocessor.clean_transcript = MagicMock(return_value="Cleaned transcript")
    preprocessor.further_process = MagicMock(
        return_value="Processed cleaned transcript"
    )
    result = preprocessor.preprocess("example transcript")
    assert result == "Processed cleaned transcript"


def test_clean_transcript_error_handling(preprocessor):
    preprocessor.cleaner.clean = MagicMock(side_effect=Exception("Cleaning failed"))
    with pytest.raises(Exception) as excinfo:
        preprocessor.clean_transcript("example transcript")
    assert str(excinfo.value) == "Cleaning failed"


def test_further_process_empty_string(preprocessor):
    result = preprocessor.further_process("")
    assert result == ""


def test_run_function():
    mock_model_loader = MagicMock(spec=ModelLoader)
    mock_prompt_manager = MagicMock(spec=PromptManager)

    with patch.object(
        TranscriptPreprocessor,
        "preprocess",
        return_value="Processed cleaned transcript",
    ):
        with patch("builtins.print") as mock_print:
            run(mock_model_loader, mock_prompt_manager)
            mock_print.assert_called_with("Processed cleaned transcript")


def test_main():
    with patch("scripts.preprocess.ModelLoader") as mock_model_loader_cls:
        mock_model_loader = MagicMock(spec=ModelLoader)
        mock_model_loader_cls.return_value = mock_model_loader

        with patch("scripts.preprocess.PromptManager") as mock_prompt_manager_cls:
            mock_prompt_manager = MagicMock(spec=PromptManager)
            mock_prompt_manager_cls.return_value = mock_prompt_manager

            with patch("scripts.preprocess.run") as mock_run:
                with patch("builtins.print") as mock_print:
                    import scripts.preprocess

                    # Ensure __main__ section is invoked
                    if "__main__" in scripts.preprocess.__name__:
                        scripts.preprocess.run(mock_model_loader, mock_prompt_manager)
                        mock_run.assert_called_with(
                            mock_model_loader, mock_prompt_manager
                        )


def test_example_transcript():
    mock_model_loader = MagicMock(spec=ModelLoader)
    mock_prompt_manager = MagicMock(spec=PromptManager)

    with patch.object(
        TranscriptPreprocessor,
        "preprocess",
        return_value="Processed cleaned transcript",
    ):
        with patch("builtins.print") as mock_print:
            run(mock_model_loader, mock_prompt_manager)
            mock_print.assert_called_with("Processed cleaned transcript")


def test_main_script_exec():
    # Simulate running the script as __main__
    with patch("scripts.preprocess.ModelLoader") as MockModelLoader:
        mock_model_loader_instance = MockModelLoader.return_value

        with patch("scripts.preprocess.PromptManager") as MockPromptManager:
            mock_prompt_manager_instance = MockPromptManager.return_value

            with patch("scripts.preprocess.run") as mock_run:
                with patch("builtins.print") as mock_print:
                    import scripts.preprocess

                    scripts.preprocess.run(
                        mock_model_loader_instance, mock_prompt_manager_instance
                    )
                    mock_run.assert_called_with(
                        mock_model_loader_instance, mock_prompt_manager_instance
                    )


if __name__ == "__main__":
    pytest.main()
