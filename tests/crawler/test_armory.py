import pytest

from bot.crawler.armory import ArmoryCrawler


@pytest.fixture(scope="module")
def armory():
    yield ArmoryCrawler("구의동최고미남손남기")


def test_armory_get_character_name(armory):
    characters = armory.get_characters_name()['카마인']
    assert characters == ['Vittel', 'FREIBURG']


def test_armory_get_character_item_level(armory):
    item_level = armory.get_characters_item_level()
    assert item_level == 101.67
