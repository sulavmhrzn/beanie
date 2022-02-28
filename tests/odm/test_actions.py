import pytest

from beanie.odm.actions import ActionDirections

from tests.odm.models import DocumentWithActions, InheritedDocumentWithActions


# @pytest.mark.parametrize(
#     "doc_class", [DocumentWithActions, InheritedDocumentWithActions]
# )
# async def test_actions_insert_replace(doc_class):
#     test_name = "test_name"
#     sample = doc_class(name=test_name)

#     # TEST INSERT
#     await sample.insert()
#     assert sample.name != test_name
#     assert sample.name == test_name.capitalize()
#     assert sample.num_1 == 1
#     assert sample.num_2 == 9

#     # TEST REPLACE
#     await sample.replace()
#     assert sample.num_1 == 2
#     assert sample.num_3 == 99


@pytest.mark.parametrize(
    "doc_class", [DocumentWithActions, InheritedDocumentWithActions]
)
async def test_actions_insert(doc_class):
    test_name = f"test_actions_insert_{doc_class}"
    sample = doc_class(name=test_name)

    await sample.insert()
    assert sample.name != test_name
    assert sample.name == test_name.capitalize()
    assert sample.num_1 == 1
    assert sample.num_2 == 9


@pytest.mark.parametrize(
    "doc_class", [DocumentWithActions, InheritedDocumentWithActions]
)
async def test_actions_replace(doc_class):
    test_name = f"test_actions_replace_{doc_class}"
    sample = doc_class(name=test_name)

    await sample.insert()

    await sample.replace()
    assert sample.num_1 == 2
    assert sample.num_3 == 99


@pytest.mark.parametrize(
    "doc_class", [DocumentWithActions, InheritedDocumentWithActions]
)
async def test_skip_actions_insert(doc_class):
    test_name = f"test_skip_actions_insert_{doc_class}"
    sample = doc_class(name=test_name)

    await sample.insert(skip_actions=[ActionDirections.AFTER, 'capitalize_name'])
    # capitalize_name has been skipped
    assert sample.name == test_name
    # add_one has not been skipped
    assert sample.num_1 == 1
    # num_2_change has been skipped
    assert sample.num_2 == 10


@pytest.mark.parametrize(
    "doc_class", [DocumentWithActions, InheritedDocumentWithActions]
)
async def test_skip_actions_replace(doc_class):
    test_name = f"test_skip_actions_replace{doc_class}"
    sample = doc_class(name=test_name)

    await sample.insert()

    await sample.replace(skip_actions=[ActionDirections.BEFORE, 'num_3_change'])
    # add_one has been skipped
    assert sample.num_1 == 1
    # num_3_change has been skipped
    assert sample.num_3 == 100
