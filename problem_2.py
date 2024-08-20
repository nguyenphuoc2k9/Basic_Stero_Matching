import numpy as np
import cv2

def distance_l1(x,y):
    return abs(x-y)
def distance_l2(x,y):
    return (x-y)**2

def window_base_matching_l1(left_image,right_image,disparity_range,kernel_size=5,save_results=True):
    left_image = cv2.imread(left_image,0)
    right_image = cv2.imread(right_image,0)
    
    left_image = np.astype(left_image,np.float32)
    right_image = np.astype(right_image,np.float32)
    height,width = left_image.shape
    depth = np.zeros((height,width),dtype=np.uint8)
    scale = 3
    max_value = 255*9
    kernel_half = int((kernel_size -1)/2)
    for y in range(kernel_half,height-kernel_half):
        for x in range(kernel_half,width-kernel_half):
            disparity = 0
            cost_min = 65534
            
            for j in range(disparity_range):
                total = 0
                value = 0
                
                for v in range(-kernel_half,kernel_half+1):
                    for u in range(-kernel_half,kernel_half+1):
                        value = max_value
                        if(x+u-j) >=0:
                            value =distance_l1(left_image[y+v,x+u],right_image[y+v,x+u-j])
                        total += value
                if total < cost_min:
                    cost_min = total
                    disparity =j
            depth[y,x] = disparity * scale
    if save_results == True:
        print("Saving results...")
        cv2.imwrite('./results/problem_2/grayscale_l1.png',depth)
        cv2.imwrite('./results/problem_2/colored_l1.png',cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print("Done.")
    return depth
left_image_path = './data/Aloe/Aloe_left_1.png'
right_image_path = './data/Aloe/Aloe_right_1.png'
disparity_range = 64
kernel_size = 3

# window_base_results_l1 = window_base_matching_l1(
#     left_image_path,
#     right_image_path,
#     disparity_range,
#     kernel_size,
#     save_results=True
# )
def window_base_matching_l2(left_image,right_image,disparity_range,kernel_size=5,save_results=True):
    left_image = cv2.imread(left_image,0)
    right_image = cv2.imread(right_image,0)
    
    left_image = np.astype(left_image,np.float32)
    right_image = np.astype(right_image,np.float32)
    height,width = left_image.shape
    depth = np.zeros((height,width),dtype=np.uint8)
    scale = 3
    max_value = (255**2)
    kernel_half = int((kernel_size -1)/2)
    for y in range(kernel_half,height-kernel_half):
        for x in range(kernel_half,width-kernel_half):
            disparity = 0
            cost_min = 65534
            
            for j in range(disparity_range):
                total = 0
                value = 0
                
                for v in range(-kernel_half,kernel_half+1):
                    for u in range(-kernel_half,kernel_half+1):
                        value = max_value
                        if(x+u-j) >=0:
                            value =distance_l2(left_image[y+v,x+u],right_image[y+v,x+u-j])
                        total += value
                if total < cost_min:
                    cost_min = total
                    disparity =j
            depth[y,x] = disparity * scale
    if save_results == True:
        print("Saving results...")
        cv2.imwrite('./results/problem_2/grayscale_l2.png',depth)
        cv2.imwrite('./results/problem_2/colored_l2.png',cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print("Done.")
    return depth
window_base_results_l2 = window_base_matching_l2(
    left_image_path,
    right_image_path,
    disparity_range,
    kernel_size,
    save_results=True
)