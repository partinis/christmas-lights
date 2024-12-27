cd ~/ws2812show/show/lights
git pull
echo "$(date)" > run.log
sudo python3 lights.py &