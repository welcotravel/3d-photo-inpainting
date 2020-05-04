import tempfile
import os
import photo_3d
from photo_3d import image_processor

image_base = 'BarcelonaCityGuide.jpg'
temp_dir = tempfile.mkdtemp()
os.system('cp ../photo_3d/image/' + image_base + ' ' + os.path.join(temp_dir,image_base))

video_files = image_processor.create_3d_video(
  fps=30,
  num_frames=180,
  input_path=temp_dir,
  output_path='./',
  x_shift_range=[0.00],
  y_shift_range=[0.00],
  z_shift_range=[-0.05],
  traj_types=['double-straight-line'],
  video_postfix=['dolly-zoom-in']
)

print('video_files',video_files)
