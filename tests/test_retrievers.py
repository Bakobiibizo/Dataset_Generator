from vectordb.retrivers import RetrieverSelector
import loguru

import unittest
from unittest.mock import Mock

logger = loguru.logger


class MockRetrieverOptions:
    OPTION1 = Mock(return_value="Option1")
    OPTION2 = Mock(return_value="Option2")
    OPTION3 = Mock(return_value="Option3")


class MockRetrieverSelector(RetrieverSelector):
    def __init__(self, default_retriever=MockRetrieverOptions.OPTION1):
        super().__init__()
        logger.info("Initializing MockRetrieverSelector")
        self.option_map = {
            "Option1": "Option1",
            "Option2": "Option2",
        }
        self.option_index = {0: "Option1", 1: "Option2"}
        self.selected_option = None
        self.Retriever = default_retriever


class TestRetrieverSelector(unittest.TestCase):
    def setUp(self):
        logger.info("Setting up TestRetrieverSelector")
        self.selector = MockRetrieverSelector()
        self.options = [
            MockRetrieverOptions.OPTION1,
            MockRetrieverOptions.OPTION2,
        ]
        self.selector.initialize_maps(self.options)

    def test_initialize_maps(self):
        logger.info("Testing initialize_maps")
        self.assertEqual(
            self.selector.option_map, {"Option1": "Option1", "Option2": "Option2"}
        )
        self.assertEqual(self.selector.option_index, {0: "Option1", 1: "Option2"})

    def test_select(self):
        logger.info("Testing select")
        self.selector.select("Option1")
        self.assertEqual(self.selector.selected_option, "Option1")

        self.selector.select("Option2")
        self.assertEqual(self.selector.selected_option, "Option2")

        self.selector.select("Option3")
        self.assertIsNone(self.selector.selected_option)

    def test_add(self):
        logger.info("Testing add")
        self.selector.add("Option3")
        self.assertEqual(
            self.selector.option_map,
            {"Option1": "Option1", "Option2": "Option2", "Option3": "Option3"},
        )
        self.assertEqual(
            self.selector.option_index, {0: "Option1", 1: "Option2", 2: "Option3"}
        )

    def test_get_maps(self):
        logger.info("Testing get_maps")
        option_map, option_index = self.selector.get_maps()
        self.assertEqual(option_map, {"Option1": "Option1", "Option2": "Option2"})
        self.assertEqual(option_index, {0: "Option1", 1: "Option2"})


if __name__ == "__main__":
    unittest.main()
