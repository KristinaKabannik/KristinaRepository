import pytest
from registration import insert_registration_result, update_registration_status, fetch_all_results, \
    delete_registration_result


def test_insert_registration():
    inserted_id = insert_registration_result("Alex", "Alex", "alex.alex@test.test", "Success")
    assert inserted_id is not None


def test_update_registration_status():
    inserted_id = insert_registration_result("John", "John", "john.john@test.test", "Pending")
    update_registration_status(inserted_id, "Confirmed")

    results = fetch_all_results()
    for row in results:
        if row[0] == inserted_id:
            assert row[4] == "Confirmed"


def test_fetch_results():
    results = fetch_all_results()
    assert len(results) > 0


def test_delete_registration():
    inserted_id = insert_registration_result("Delete", "Me", "deleteme@example.com", "Pending")
    delete_registration_result(inserted_id)

    results = fetch_all_results()
    assert all(row[0] != inserted_id for row in results)
