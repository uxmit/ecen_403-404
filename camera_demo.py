import cv2
import imageio
import numpy as np
import pyrealsense2 as rs
import os
import shutil
import signal
import sys 
import datetime

g_isStreaming = True

def signal_handler(sig, frame):
	global g_isStreaming
	print('You pressed Ctrl+C!')
	g_isStreaming = False
	# sys.exit(0)

def signal_handler2(sig, frame):
		print('You pressed Ctrl+Z!')
		sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler2)

def make_clean_folder(path_folder):
	if not os.path.exists(path_folder):
		os.makedirs(path_folder)
	# else:
	# 	user_input = input("%s not empty. Overwrite? (y/n) : " % path_folder)
	# 	if user_input.lower() == "y":
	# 		shutil.rmtree(path_folder)
	# 		os.makedirs(path_folder)
	# 	else:
	# 		exit()


def record_rgbd():
	folder = "images/"
	make_clean_folder(folder)

	pipeline = rs.pipeline()

	config = rs.config()
	# pipeline.start(config)
	#config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
	config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
	config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

	profile = pipeline.start(config)

	depth_sensor = profile.get_device().first_depth_sensor()
	# pipeline.start(config)
	depth_sensor.set_option(
		rs.option.visual_preset, 3
	)  # Set high accuracy for depth sensor
	depth_scale = depth_sensor.get_depth_scale()

	clipping_distance_in_meters = 1
	clipping_distance = clipping_distance_in_meters / depth_scale

	align_to = rs.stream.color
	align = rs.align(align_to)

	try:
		#wiat for a coherent pair of frames: depht and color
		frames = pipeline.wait_for_frames()
		aligned_frames = align.process(frames)
		aligned_depth_frame = aligned_frames.get_depth_frame()
		color_frame = aligned_frames.get_color_frame()
		if not aligned_depth_frame or not color_frame:
			raise RuntimeError("Could not acquire depth or color frames.")

		#convert images to numpy arrays
		depth_image = np.asanyarray(aligned_depth_frame.get_data())
		# depth_image = cv2.applyColorMap(cv2.convertScaleAbs((np.float32(aligned_depth_frame.get_data())), cv2.COLORMAP_RAINBOW))
		color_image = np.asanyarray(color_frame.get_data())

		grey_color = 153
		depth_image_3d = np.dstack(
			(depth_image, depth_image, depth_image)
		)  # Depth image is 1 channel, color is 3 channels
		bg_removed = np.where(
			(depth_image_3d > clipping_distance) | (depth_image_3d <= 0),
			grey_color,
			color_image,
		)

		color_image = color_image[..., ::-1]

		# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
		depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

		depth_colormap_dim = depth_colormap.shape
		color_colormap_dim = color_image.shape

		# If depth and color resolutions are different, resize color image to match depth image for display
		if depth_colormap_dim != color_colormap_dim:
			resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
			images = np.hstack((resized_color_image, depth_colormap))
		else:
			images = np.hstack((color_image, depth_colormap))


	#show images
		# cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
		# cv2.imshow('RealSense', images)
		# cv2.waitKey(1)

		# usr_input=input("Take image? (y/n)..")
		# if usr_input =='y':
		# 	imageio.imwrite("../data/realsense/depth.png", depth_image)
		# 	imageio.imwrite("../data/realsense/rgb.png", color_image)
		
	
		# imageio.imwrite("../data/realsense/depth.png", depth_image)
		date = str(datetime.datetime.now()).replace("-", "_").replace(":", ".")
		imageio.imwrite(f"{folder}{date}rgb.png", color_image)

	finally:
		pipeline.stop()

	return color_image, depth_image

def stream_rgb():
	pipeline = rs.pipeline()
	config = rs.config()

	# Get device product line for setting a supporting resolution
	pipeline_wrapper = rs.pipeline_wrapper(pipeline)
	pipeline_profile = config.resolve(pipeline_wrapper)
	device = pipeline_profile.get_device()
	device_product_line = str(device.get_info(rs.camera_info.product_line))

	found_rgb = False
	for s in device.sensors:
		if s.get_info(rs.camera_info.name) == 'RGB Camera':
			found_rgb = True
			break
	if not found_rgb:
		print("The demo requires Depth camera with Color sensor")
		exit(0)

	config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

	# if device_product_line == 'L500':
	#     config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
	# else:
	config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

	# Start streaming
	pipeline.start(config)

	try:
		while g_isStreaming:

			# Wait for a coherent pair of frames: depth and color
			frames = pipeline.wait_for_frames()
			depth_frame = frames.get_depth_frame()
			color_frame = frames.get_color_frame()
			if not depth_frame or not color_frame:
				continue

			# Convert images to numpy arrays
			depth_image = np.asanyarray(depth_frame.get_data())
			color_image = np.asanyarray(color_frame.get_data())

			# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
			depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

			depth_colormap_dim = depth_colormap.shape
			color_colormap_dim = color_image.shape

			# If depth and color resolutions are different, resize color image to match depth image for display
			if depth_colormap_dim != color_colormap_dim:
				resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
				images = np.hstack((resized_color_image, depth_colormap))
			else:
				images = np.hstack((color_image, depth_colormap))

			# Show images
			cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
			cv2.imshow('RealSense', images)
			cv2.waitKey(1)
			# usr_input=input("Stop stream? (y/n)")
			# if usr_input=='y':
			# 	pipeline.stop()
			

	finally:

		# Stop streaming
		pipeline.stop()


# if __name__ == "__main__":
	# stream_rgb()
	# record_rgbd()

while True:
	stream_rgb()
	g_isStreaming = True
	# take_picture()
	print("takin pic")
	record_rgbd()
# print("hello world")

# record_rgbd()
