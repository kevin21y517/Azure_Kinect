import cv2
import time
import pykinect_azure as pykinect

if __name__ == "__main__":
    file = "output_data_2024-02-23_095016"
    num = "S0050_4_output_6.390077829360962s_27.86fps"
    # video_filename = f"output.mkv"
    video_filename = f"depth_image_data/{file}/{num}.mkv"

    # Initialize the library, if the library is not found, add the library path as argument
    pykinect.initialize_libraries()

    # Start playback
    playback = pykinect.start_playback(video_filename)

    playback_config = playback.get_record_configuration()
    # print(playback_config)

    cv2.namedWindow('Depth Image', cv2.WINDOW_NORMAL)

    delay = 0.145  # 延遲時間（秒）
    # while True:

    #     # Get camera capture
    #     ret, capture = playback.update()

    #     if not ret:
    #         break

    #     # Get color image
    #     ret_color, color_image = capture.get_transformed_color_image()

    #     # Get the colored depth
    #     ret_depth, depth_color_image = capture.get_colored_depth_image()

    #     if not ret_color or not ret_depth:
    #         continue

    #     # Plot the image
    #     combined_image = cv2.addWeighted(color_image[:, :, :3], 1.0, depth_color_image, 0.0, 0)
    #     cv2.imshow('Depth Image', combined_image)

    #     time.sleep(delay)

    #     # Press q key to stop
    #     if cv2.waitKey(1) == 27:
    #         break

    #我想顯示video_filename的2D影像

    # Start playback
    playback = pykinect.start_playback(video_filename)
    while True:
        # Get camera capture
        ret, capture = playback.update()

        if not ret:
            break

        # Get color image
        ret_color, color_image = capture.get_color_image()

        if not ret_color:
            continue

        # Plot the image
        cv2.imshow('Video', color_image)
        time.sleep(delay)
        # Press q key to stop
        if cv2.waitKey(1) == 27:
            break