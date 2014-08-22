from django.forms.models import modelform_factory
from django.db.models.loading import get_models, get_app, get_apps


def normalize_model_name(string, uppercase_first_letter=True):
    """
    Convert strings to CamelCase.

    Examples::

        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"

    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::

        >>> camelize(underscore("IOError"))
        "IoError"

    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """
    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize(string)[1:]


def get_model_form(model_name):
    app_list = get_apps()
    for app in app_list:
        for model in get_models(app):
            if model.__name__ == model_name: 
                try:
                    # add_new_form is a class method
                    # that can be used to specialize the form
                    form = model.add_new_form()
                except AttributeError:
                    form = None
                if not form:
                    form = modelform_factory(model)
                return form

    raise Exception('Did not find the model %s' % (model_name))