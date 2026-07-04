pip install opencv-python

conda create -n tf213 python=3.10 -y
conda activate tf213
pip install tensorflow==2.13.0 opencv-python notebook
python -c "import tensorflow as tf; print(tf.__version__)"

python -m notebook
