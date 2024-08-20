import numpy as np
import cv2
def cosine_similarity(x,y):
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))
def improved_window_base_matching(left_image,right_image,disparity_range,kernel_size=5,save_results=True):
    left_image = cv2.imread(left_image,0)
    right_image = cv2.imread(right_image,0)
    
    left_image = np.astype(left_image,np.float32)
    right_image = np.astype(right_image,np.float32)
    height,width = left_image.shape
    depth = np.zeros((height,width),dtype=np.uint8)
    scale = 3
    kernel_half = int((kernel_size -1)/2)
    for y in range(kernel_half,height-kernel_half):
        for x in range(kernel_half,width-kernel_half):
            disparity = 0
            cost_optimal = -1
            
            for j in range(disparity_range):
                d = x-j
                cost = -1
                if (d-kernel_half)>0:
                    wp = left_image[(y-kernel_half):(y+kernel_half)+1,(x-kernel_half):(x+kernel_half)+1]
                    wqd = right_image[(y-kernel_half):(y+kernel_half)+1,(d-kernel_half):(d+kernel_half)+1]    
            
                    cost = cosine_similarity(wp.flatten(),wqd.flatten())
                if cost > cost_optimal:
                    cost_optimal = cost
                    disparity = j
            depth[y,x] = disparity * scale
    if save_results == True:
        print("Saving results...")
        cv2.imwrite('./results/problem_4/grayscale.png',depth)
        cv2.imwrite('./results/problem_4/colored.png',cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print("Done.")
    return depth
left_image_path = './data/Aloe/Aloe_left_1.png'
right_image_path = './data/Aloe/Aloe_right_1.png'
disparity_range = 64
kernel_size = 5
result = improved_window_base_matching(
    left_image_path,
    right_image_path,
    disparity_range,
    kernel_size,
    save_results=True
)