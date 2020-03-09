#!/bin/bash

sudo pip install jupyter
jupyter notebook --generate-config
sed -i "s/# c.NotebookApp.port = 8888/c.NotebookApp.port = $PORT/" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/# c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/" ~/.jupyter/jupyter_notebook_config.py
