# Simple photo booth script
0. connect to a monitor with HDMI
1. login as user `pi`
2. clone this repository `git clone https://github.com/xiubert/PiPhotoBooth.git`
3. navigate to photobooth directory `cd PiPhotoBooth`
4. make scripts executable:
   1. `chmod +x ./startPhotoBooth.sh`
   2. `chmod +x lib/*.sh`
5. start the booth `./startPhotoBooth.sh`
   1. position the camera where desired
   2. take photo by pressing button wired to GPIO (pin 11)
   3. preview will show for a few seconds to pose
   4. captured photo will be shown followed by most recent captures. photos will continue to cycle until another photo is taken, after which most recent will again cycle
   5. close with `ESC` then `ctrl+c` to stop the booth script
6. saved photos available in `PhotoBoothCycle`

## note:
- script assumes user `pi` can execute `sudo` commands. this is needed to avoid permissions issues with showing photos via `fbi` on `/dev/tty`