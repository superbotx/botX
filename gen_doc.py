from botX.utils.doc_util import *
from botX.configs.config import *

def output_installation_page():
    str_content = get_installation_page()
    with open('docs/_docs/installation.md', 'w') as installation_file:
        installation_file.write(str_content)

def output_example_pages():
    doc_struct = DOC_STRUCT.copy()
    example_meta = {
        'title': 'Examples',
        'docs': []
    }
    for filename in os.listdir('examples'):
        if '.py' in filename and filename.split('_')[0] == 'example':
            title = filename.split('.')[0]
            example_meta['docs'].append(title)
            str_content = get_example_page('examples/' + filename)
            with open('docs/_docs/' + title + '.md', 'w') as example_file:
                example_file.write(str_content)
    doc_struct.append(example_meta)
    output_doc_meta(doc_struct=doc_struct)

def output_doc_meta(doc_struct=DOC_STRUCT):
    contents = []
    for doc_meta in doc_struct:
        contents.append('- title: ' + doc_meta['title'] + '\n')
        contents.append('  docs:\n')
        for doc in doc_meta['docs']:
            contents.append('  - ' + doc + '\n')
        contents.append('\n')
    str_content = ''.join(s for s in contents)
    with open('docs/_data/docs.yml', 'w') as meta_file:
        meta_file.write(str_content)

def output_command_pages():
    doc_pages = get_command_pages()
    for doc_page_filename, doc_page_content in doc_pages.items():
        full_path = 'docs/_docs/' + doc_page_filename
        with open(full_path, 'w') as doc_page_file:
            doc_page_file.write(doc_page_content)

def output_readme_file():
    doc_content = get_readme_content()
    with open('README.md', 'w') as readme_file:
        readme_file.write(doc_content)

def main():
    output_readme_file()
    output_installation_page()
    output_command_pages()
    output_example_pages()

if __name__ == '__main__':
    main()
