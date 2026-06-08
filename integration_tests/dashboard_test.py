from src.models.dashboard_repository import get_dashboard_stats


def test_dashboard_stats():

    stats = get_dashboard_stats()

    assert stats["total_listings"] >= 0