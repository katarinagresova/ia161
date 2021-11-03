from ia161.detector import PlagiarismDetector
from pathlib import Path

TEST_RESOURCES_DIR_PATH = (Path(__file__).parents[0] / 'resources').resolve()

def test_parse_input():
    detector = PlagiarismDetector()
    detector.parse_input(TEST_RESOURCES_DIR_PATH / 'test_data.vert')

    assert detector.metadata is not None
