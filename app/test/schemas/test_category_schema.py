import pytest
from app.schemas.category import Category

def test_cetegory_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.dict() == {
        'name': 'Roupa',
        'slug': 'roupa'
    }

def test_category_schemas_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='roupa de cama'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='cèe'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='Roupa'
        )