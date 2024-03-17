import cv2
import os
import pykinect_azure as pykinect

def save_frame_images(video_filename, output_folder):
    # 初始化PyKinect
    pykinect.initialize_libraries()

    # 開始播放
    playback = pykinect.start_playback(video_filename)

    # 創建輸出資料夾
    output_path_2D = os.path.join(output_folder, "2D")
    output_path_3D = os.path.join(output_folder, "3D")
    os.makedirs(output_path_2D, exist_ok=True)
    os.makedirs(output_path_3D, exist_ok=True)

    frame_index = 0
    while True:
        # 獲取攝像機捕捉
        ret, capture = playback.update()
        if not ret:
            break

        # 獲取彩色圖像和深度圖像
        ret_color, color_image = capture.get_color_image()
        ret_depth, depth_image = capture.get_depth_image()

        if not ret_color or not ret_depth:
            continue

        # 儲存2D彩色圖像
        cv2.imwrite(os.path.join(output_path_2D, f"frame_{frame_index}.jpg"), color_image)

        # 轉換深度圖像為可視化圖像 (這裡需要對深度圖像進行處理才能正確顯示)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        # 儲存3D深度圖像
        cv2.imwrite(os.path.join(output_path_3D, f"frame_{frame_index}.jpg"), depth_colormap)

        frame_index += 1

# 設定檔案名和輸出資料夾
file = "output_data_2024-02-23_095016"
num = "S0110_1_output_7.054147958755493s_27.93fps"
video_filename = f"depth_image_data/{file}/{num}.mkv"
output_folder = f"jpg/{num}"

# 執行儲存圖像函數
save_frame_images(video_filename, output_folder)
