apt-get update -y
apt-get install git -y
pkg install cmake -y
apt update -y
apt upgrade  -y
pkg install python -y
git clone https://github.com/xmrig/xmrig.git 
cd xmrig
mkdir build
cd build
cmake -DWITH_HWLOC=OFF .. 
make
echo "cd /data/data/com.termux/files/home/xmrig-installer" > /data/data/com.termux/files/usr/bin/xmrig
echo "python /data/data/com.termux/files/home/xmrig-installer/xmrig.py" >> /data/data/com.termux/files/usr/bin/xmrig
chmod +x /data/data/com.termux/files/usr/bin/xmrig
xmrig
