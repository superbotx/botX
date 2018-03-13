from botX.utils.doc_util import *

def main():
    doc_content = get_readme_content()
    with open('README.md', 'w') as readme_file:
        readme_file.write(doc_content)

if __name__ == '__main__':
    main()
