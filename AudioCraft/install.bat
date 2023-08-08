cd c:\ai

git clone https://github.com/facebookresearch/audiocraft.git

cd audiocraft

echo y | conda create -n audiocraft python=3.9

call activate audiocraft

echo y | conda install -c conda-forge "ffmpeg<5"

echo y | pip install -r requirements.txt

echo y | pip install -U git+https://git@github.com/facebookresearch/audiocraft#egg=audiocraft

echo y | conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

echo y | pip install numpy==1.24

echo y | pip install chardet

echo y | pip install notebook

echo y | conda install -c conda-forge ipywidgets
