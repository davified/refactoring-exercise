#!/usr/bin/env bash

set -e

virtual_env_name="$(basename $(pwd))"

if [[ $OSTYPE == "msys" ]]; then
  echo "[INFO] Non-Mac OSX operating system detected"
  echo "[TODO] Open https://docs.conda.io/en/latest/miniconda.html with your web browser"
  echo "[TODO] Download the Miniconda 3 installer for your OS"
  echo "[TODO] Run the installer. Go with the defaults, except make sure to check 'Make Anaconda the default Python'"
  echo "[INFO] Exiting..."
  exit 0
fi

export PATH="$PATH:$HOME/miniconda3/bin"
echo "[INFO] Adding miniconda bin path to current session"
if [[ -f ~/.zshrc ]]; then
  echo "[INFO] Adding miniconda bin path to ~/.zshrc config file"
  grep -q -F 'export PATH="$PATH:$HOME/miniconda3/bin"' ~/.zshrc || echo 'export PATH="$PATH:$HOME/miniconda3/bin"' >> ~/.zshrc
elif [[ -f ~/.bashrc ]]; then
  echo "[INFO] Adding miniconda bin path to ~/.bashrc config file"
  grep -q -F 'export PATH="$PATH:$HOME/miniconda3/bin"' ~/.bashrc || echo 'export PATH="$PATH:$HOME/miniconda3/bin"' >> ~/.bashrc
fi

if [[ `which conda` ]]; then
  echo "[INFO] OK Found conda!"
else
  if [[ ! -f ./bin/miniconda3.sh  ]]; then
    echo "[INFO] Downloading miniconda installation script..."
    echo "[INFO] This is a 511MB file and will some time to complete..."
    echo "downloading 511mb file"
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ./bin/miniconda3.sh
  fi

  echo "[INFO] Running miniconda installation script..."
  bash bin/miniconda3.sh -b -p ~/miniconda3
fi

if [[ ! -d "${HOME}/miniconda3/envs/${virtual_env_name}" ]]; then
  echo "[INFO] Creating virtual environment and installing dependencies..."
  conda env create -f ./environment.yml
else 
  echo "[INFO] Installing dependencies..."
  conda env update
fi

echo "[INFO] Done!"
echo "[INFO] To activate the virtual environment, run: source activate ${virtual_env_name}"
echo "[INFO] If you see a 'command not found: conda' error message, restart your shell/terminal"
echo "[INFO] To deactivate the virtual environment, run: conda deactivate"