import contextlib
from unittest import TestCase

from burner.client import Client
from burner.database import Country, Price, Service


class CacheTestCase(TestCase):
    def setUp(self):
        with contextlib.ExitStack() as stack:
            self.client = stack.enter_context(
                Client(api_key=None, database_path=":memory:")
            )

            self.addCleanup(stack.pop_all().close)

    def test_country_cache(self):
        self.assertEqual(Country.select().count(), 0)

        self.client.get_countries()

        self.assertGreater(Country.select().count(), 0)

    def test_service_cache(self):
        self.assertEqual(Service.select().count(), 0)

        self.client.get_services()

        self.assertGreater(Service.select().count(), 0)

    def test_price_cache(self):
        self.assertEqual(Service.select().count(), 0)
        self.assertEqual(Country.select().count(), 0)
        self.assertEqual(Price.select().count(), 0)

        # Will populate countries, services, and prices.
        self.client.get_prices_by_service("opt20")

        self.assertGreater(Country.select().count(), 0)
        self.assertGreater(Service.select().count(), 0)
        self.assertGreater(Price.select().count(), 0)

    def test_cache_reset(self):
        self.assertEqual(Service.select().count(), 0)
        self.assertEqual(Country.select().count(), 0)
        self.assertEqual(Price.select().count(), 0)

        self.client.reset_cache()

        self.assertGreater(Country.select().count(), 0)
        self.assertGreater(Service.select().count(), 0)
        self.assertGreater(Price.select().count(), 0)
