import tempfile
import os
import photo_3d
from photo_3d import main

image_base = 'BarcelonaCityGuide.jpg'
temp_dir = tempfile.mkdtemp()
os.system('cp ../photo_3d/image/' + image_base + ' ' + os.path.join(temp_dir,image_base))

main.create_3d_video(
  input_path=temp_dir,
  x_shift_range=[-0.02],
  y_shift_range=[0.00],
  z_shift_range=[-0.07],
  traj_types=['double-straight-line'],
  video_postfix=['dolly-zoom-in']
)

