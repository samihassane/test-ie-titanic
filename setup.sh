# Bash script

echo "Installing miniforge3..."
pyenv install miniforge3

export PYENV_VERSION=miniforge3



#NOTE: Because of how conda activate works.
# this is difficult to make work inside a script

#conda create -n titanic39 python=3.9 --yes
#pip install -e .[dev]
