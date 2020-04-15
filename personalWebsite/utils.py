def set_type_image(form_type_image):
    path = 'images/'
    if form_type_image == 'code':
        fname = 'coding_project_type.png'
    elif form_type_image == 'writing':
        fname = 'writing_project_type.png'
    else:
        fname = 'photography_project_type.png'
    path += fname
    return path
