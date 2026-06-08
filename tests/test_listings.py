from src.models.rental_repository import get_all_listings


def test_get_all_listings():

    listings = get_all_listings()

    assert len(listings) > 0