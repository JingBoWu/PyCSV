

sudo apt-get install libjpeg-dev zlib1g-dev # 安装 pillow 需要 
sudo pip3 install numpy pandas matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

python3 -B pycsv.py -f example.csv  [ -m 1 -n 0.5 ]

-f file
-m  reduse sampling rate 
-n  move CHB line down  n voltage