from typing import Type, Tuple

from core.models import Base


def get_filter_params(model: Type[Base], **kwargs) -> Tuple:
    """
    Prepare filter arguments
    return model.field_name and value

    Usage:
        >>> model_field, search_query = get_filter_params(model, **kwargs)
        >>> db.query(model).filter(model_field == search_query).all()

    @param model:
    @param kwargs:
    @return:
    """
    mapping = {
        'name': model.name if hasattr(model, 'name') else None,
        'email': model.email if hasattr(model, 'email') else None,
        'pk': model.id if hasattr(model, 'id') else None,
        'id': model.id if hasattr(model, 'id') else None,
    }

    key, value = kwargs.copy().popitem()
    return mapping[key], value


def get_object(db, model, **kwargs):
    """
    Get object from model by pk
    if object does not exist return None

    @param db:
    @param model:
    @param kwargs:
    @return:
    """
    key, value = get_filter_params(model, **kwargs)

    return db.query(model).filter(key == value, model.deleted is not False).first()
