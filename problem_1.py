import numpy as np
import cv2

def distance_l1(x,y):
    return abs(x-y)
def distance_l2(x,y):
    return (x-y)**2
# Using L1 method to calculate stereo matching
def pixel_wise_matching_l1(left_image,right_image,disparity_range,save_result=True):
    left_image = cv2.imread(left_image,0)
    right_image = cv2.imread(right_image,0)
    
    left_image = np.astype(left_image,np.float32)
    right_image = np.astype(right_image,np.float32)
    height,width = left_image.shape
    depth = np.zeros((height,width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            min_cost = 255
            disparity = 0
            for j in range(disparity_range):
                if x - j > 0:
                    cost = distance_l1(left_image[y,x],right_image[y,x-j])
                else:
                    cost = 255
                if cost < min_cost:
                    min_cost = cost
                    disparity = j
            depth[y,x] = disparity * 16
    if save_result == True:
        print("Saving result...")
        cv2.imwrite('./results/problem_1/grayscale_l1.png',depth)
        cv2.imwrite("./results/problem_1/colored_l1.png",cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print('Done')
    
    return depth
left_img_path = './data/tsukuba/left.png'
right_img_path = './data/tsukuba/right.png'
disparity_range = 16
# pixel_wise_result_l1 = pixel_wise_matching_l1(
#     left_img_path,
#     right_img_path,
#     disparity_range,
#     save_result=True
# )
# Using L2 method to calculate stereo matching
def pixel_wise_matching_l2(left_image,right_image,disparity_range,save_result=True):
    left_image = cv2.imread(left_image,0)
    right_image = cv2.imread(right_image,0)
    
    left_image = np.astype(left_image,np.float32)
    right_image = np.astype(right_image,np.float32)
    
    height,width = left_image.shape
    depth = np.zeros((height,width),np.uint8)
    scale = 16
    for y in range(height):
        for x in range(width):
            min_cost = 255**2
            disparity = 0
            for j in range(disparity_range):
                cost = 255 if x -j <0 else distance_l2(left_image[y,x],right_image[y,x-j])
                if cost <min_cost:
                    min_cost = cost
                    disparity = j
            depth[y,x] = disparity * scale
    if save_result==True:
        print("Saving result...")
        cv2.imwrite("./results/problem_1/grayscale_l2.png",depth)
        cv2.imwrite("./results/problem_1/colored_l2.png",cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print("Done")
    return depth
pixel_wise_result_l2 = pixel_wise_matching_l2(
    left_img_path,
    right_img_path,
    disparity_range,
    save_result=True
)