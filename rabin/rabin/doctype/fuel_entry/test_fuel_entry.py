# Copyright (c) 2026, Rabin Karki and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestFuelEntry(IntegrationTestCase):
	"""
	Integration tests for FuelEntry.
	Use this class for testing interactions between multiple components.
	"""

	pass
