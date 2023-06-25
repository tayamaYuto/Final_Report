import cv2
import os

# PNGファイルが格納されているディレクトリのパス
png_directory = 'save/'

# 出力する動画ファイルの名前と保存先パス
output_file = 'video.mp4'

# 動画のフレームレートと解像度
frame_rate = 5
width, height = 640, 480

# 動画ファイルのエンコーディング設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

# PNGファイルの読み込みと結合
for filename in sorted(os.listdir(png_directory)):
    if filename.endswith('.png'):
        file_path = os.path.join(png_directory, filename)
        frame = cv2.imread(file_path)
        if frame is not None:
            frame = cv2.resize(frame, (width, height))
            video_writer.write(frame)

# リソースの解放
video_writer.release()
