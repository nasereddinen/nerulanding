def check_all_fields_filled(obj):
    return all((getattr(obj, field.name) for field in obj._meta.fields))


def get_dict_of_fields(obj):
    return {field.name: getattr(obj, field.name) for field in obj._meta.fields}


def check_all_required_fields_filled(obj):
    return all((getattr(obj, field.name) for field in obj._meta.fields if not field.blank))
