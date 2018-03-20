from botX.utils.doc_util import *
from botX.configs.config import *

def output_doc_meta():
    contents = []
    for doc_meta in DOC_STRUCT:
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
    output_command_pages()
    output_doc_meta()

if __name__ == '__main__':
    main()
