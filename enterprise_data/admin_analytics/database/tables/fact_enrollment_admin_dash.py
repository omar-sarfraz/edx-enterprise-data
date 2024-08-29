"""
Module for interacting with the fact_enrollment_admin_dash table.
"""
from datetime import date, datetime
from uuid import UUID

from ..queries import FactEnrollmentAdminDashQueries
from ..utils import run_query
from .base import BaseTable


class FactEnrollmentAdminDashTable(BaseTable):
    """
    Class for communicating with the fact_enrollment_admin_dash table.
    """
    queries = FactEnrollmentAdminDashQueries()

    def get_enrollment_date_range(self, enterprise_customer_uuid: UUID):
        """
        Get the enrollment date range for the given enterprise customer.

        Arguments:
            enterprise_customer_uuid (UUID): The UUID of the enterprise customer.

        Returns:
            (tuple<date, date>): The minimum and maximum enrollment dates.
        """
        results = run_query(
            query=self.queries.get_enrollment_date_range_query(),
            params={'enterprise_customer_uuid': enterprise_customer_uuid}
        )
        min_date, max_date = results[0]

        # We should return date objects, not datetime objects
        # This is done to counter cases where database values are datetime objects.
        if min_date and isinstance(min_date, datetime):
            min_date = min_date.date()
        if max_date and isinstance(max_date, datetime):
            max_date = max_date.date()

        return min_date, max_date

    def get_enrollment_and_course_count(self, enterprise_customer_uuid: UUID, start_date: date, end_date: date):
        """
        Get the enrollment and course count for the given enterprise customer.

        Arguments:
            enterprise_customer_uuid (UUID): The UUID of the enterprise customer.
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            (tuple<int, int>): The enrollment and course count.
        """
        results = run_query(
            query=self.queries.get_enrollment_and_course_count_query(),
            params={
                'enterprise_customer_uuid': enterprise_customer_uuid,
                'start_date': start_date,
                'end_date': end_date,
            }
        )
        return tuple(results[0])

    def get_completion_count(self, enterprise_customer_uuid: UUID, start_date: date, end_date: date):
        """
        Get the completion count for the given enterprise customer.

        Arguments:
            enterprise_customer_uuid (UUID): The UUID of the enterprise customer.
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            int: The completion count.
        """
        results = run_query(
            query=self.queries.get_completion_count_query(),
            params={
                'enterprise_customer_uuid': enterprise_customer_uuid,
                'start_date': start_date,
                'end_date': end_date,
            }
        )
        return results[0][0]
