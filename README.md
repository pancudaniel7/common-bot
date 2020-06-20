# common-bot
Common packages bot project

###Usage

Create the package:
```sh
python3 setup.py sdist bdist_wheel
```
Upload new version to pypi repo
```sh
twine upload dist/* --repository-url https://upload.pypi.org/legacy/ 
```
Check project version
```sh
pip list | grep [package-name]
```

More about packaging:
https://packaging.python.org/tutorials/packaging-projects/