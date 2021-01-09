## Package structure
```
# tree
.
├── LICENSE
├── README.md
├── example_pkg
│   ├── __init__.py
│   └── submodule.py
└── setup.py
```

## Generate distribution archives
```
# Upgrade setuptools and wheel
python3 -m pip install --upgrade setuptools wheel

# Generate archives
python3 setup.py sdist bdist_wheel
```

## Upload the distribution archives
```
# Use twine to upload the distribution packages
python3 -m pip install --upgrade twine

# Upload all of the archives under dist to testpypi
python3 -m twine upload --repository testpypi dist/*

# Upload all of the archives under dist to pypi
python3 -m twine upload dist/*
```

## References
- https://packaging.python.org/tutorials/packaging-projects/
- https://python-packaging.readthedocs.io/en/latest/index.html
