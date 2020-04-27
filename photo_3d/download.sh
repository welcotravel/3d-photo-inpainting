#!/bin/sh
mkdir checkpoints
wget https://s3.amazonaws.com/dev.welco.me/3d/model/color-model.pth
mv color-model.pth checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/depth-model.pth
mv depth-model.pth checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/edge-model.pth
mv edge-model.pth checkpoints/.
wget https://s3.amazonaws.com/dev.welco.me/3d/model/model.pt
mkdir MidaS
mv model.pt MiDaS/.
