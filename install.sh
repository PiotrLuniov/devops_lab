#!/bin/bash

#Install additional software
yum install -y git zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils

#Install pyenv and tune it
curl https://pyenv.run | bash

cat>>$HOME/.bashrc<<'EOF'
export PATH="/home/vagrant/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF

#Install necessary versions of python
pyenv install 2.7.14
pyenv install 3.7.0

#Create environments
pyenv virtualenv 2.7.14 env_for_python27
pyenv virtualenv 3.7.0 env_for_python37
