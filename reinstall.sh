pip3 uninstall botX
rm -r -f build
rm -r -f dist
rm -r -f botX.egg-info
python3 setup.py build
python3 setup.py install
