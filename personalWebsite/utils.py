import os
from personalWebsite import app

def set_type_image(form_type_image):
    path = 'images/'
    if form_type_image == 'coding':
        fname = 'coding_project_type.png'
    elif form_type_image == 'writing':
        fname = 'writing_project_type.png'
    else:
        fname = 'photography_project_type.png'
    path += fname
    return path

def save_file(form_file, proj_dir_path):
    fn = secure_filename(form_file.filename)
    file_path = os.path.join(proj_dir_path, fn)
    form_file.save(file_path)
    return fn

def save_project_files(form):
    #create the relative path to make directory
    rel_dir_path = os.path.join(app.config['UPLOAD_FOLDER'], form.title.data.strip().replace(" ", ""))
    full_dir_path = os.path.join(app.root_path, 'static', rel_dir_path)
    os.mkdir(full_dir_path)
    for file in form.files.data:
        save_file(file, full_dir_path)
    return rel_dir_path

'''
Returns all files in the project's directory as a full file path
Return type: list
'''
def get_project_files(project):
    #we should only attempt to load image files if they exist
    if project.files:
        full_dir_path = os.path.join(app.root_path, 'static', project.files)
        files = os.listdir(full_dir_path)
        file_paths = []
        for file in files:
            # we simply join them here to avoid concatenation in HTML file
            file_paths.append(os.path.join(project.files, file))
            return file_paths
    else:
        return None
