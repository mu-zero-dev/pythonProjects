#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install necessary dependencies
pip install --upgrade pip

# Create project structure
mkdir -p src tests

# Create README file
cat <<EOT >> README.md
# Python Project

## Description
A brief description of the project.

## Installation
\`\`\`sh
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Usage
Instructions on how to use the project.
EOT

# Create .gitignore file
cat <<EOT >> .gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Install logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# PyCharm
.idea/

# VS Code
.vscode/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre
.pyre/
EOT

# Create requirements.txt file
touch requirements.txt

# Initialize the database
export FLASK_APP=src/app.py
flask db init
flask db migrate
flask db upgrade

echo "Setup complete. Don't forget to activate the virtual environment with 'source venv/bin/activate'."
