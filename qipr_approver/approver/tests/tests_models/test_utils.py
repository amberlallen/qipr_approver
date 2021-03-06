import django
from django.db.models import fields

def check_fields(ModelName,fieldname,type,max_length=None):
    """
    Given a Model checks if the fieldname is of proper type.
    Also checks the max_length if it is not None
    """
    model_meta = getattr(ModelName, "_meta")
    fields = getattr(model_meta, "fields")
    for field in fields :
        if field.name == fieldname:
            if isinstance(field, getattr(django.db.models.fields, type+"Field")) == True :
                if max_length is not None :
                    if field.max_length == max_length :
                        return True
                else:
                    return True
            else:
                return False
    return False

def is_foreign_key_to(model_name, field_name, related_model_name):
    """
    Given a Model, check if the field_name is related to the
    related Model given and return true or false. If the field_name
    is not a foriegn key,it will error with AttributeError
    """
    try:
        return model_name._meta.get_field(field_name).rel.to is related_model_name
    except AttributeError:
        return False

    return False
