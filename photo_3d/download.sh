#!/bin/sh
mkdir -p /tmp/3d/checkpoints
wget https://s3.amazonaws.com/dev.welco.me/3d/model/color-model.pth
mv color-model.pth /tmp/3d/checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/depth-model.pth
mv depth-model.pth /tmp/3d/checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/edge-model.pth
mv edge-model.pth /tmp/3d/checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/model.pt
mkdir -p /tmp/3d/MiDaS
mv model.pt /tmp/3d/MiDaS/.
