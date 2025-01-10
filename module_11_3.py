def introspection_info(obj):
    full_inf = {}
    properties = {}
    properties["type"] = type(obj).__name__
    full_inf.update(properties)
    properties['attributes'] = [x for x in dir(obj) if callable(getattr(obj, x)) and not x.startswith("__")]
    full_inf.update(properties)
    properties["methods"] = [x for x in dir(obj) if callable(getattr(obj, x)) and x.startswith("__")]
    full_inf.update(properties)
    properties['module'] = introspection_info.__module__
    full_inf.update(properties)
    properties["id"] = id(obj)
    full_inf.update(properties)
    return  full_inf

number_info = introspection_info(Gg)
print(number_info)
