def file_path(instance, filename):
    return f"{instance._meta.model_name}s/{filename}"
