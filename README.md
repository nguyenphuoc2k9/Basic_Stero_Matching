Giới thiệu
----------

Trong Thị giác máy tính, việc khôi phục cấu trúc 3D từ các cặp ảnh 2D, hay còn gọi là **Stereo Matching**, là một nhiệm vụ quan trọng. Kỹ thuật này được áp dụng rộng rãi trong các lĩnh vực như lái xe tự hành, xây dựng mô hình 3D, và thị giác robot. Stereo Matching giúp chúng ta hiểu được khoảng cách giữa các đối tượng trong một cảnh, nhờ đó có thể xây dựng bản đồ độ sâu (disparity map).

Mục tiêu của Dự án
------------------

Dự án này được thiết kế để hướng dẫn bạn qua quy trình xây dựng bản đồ độ sâu từ các cặp ảnh stereo. Mục tiêu của dự án bao gồm:

-   Hiểu được các phương pháp cơ bản để so khớp ảnh (image matching).
-   Xây dựng các thuật toán cơ bản để tính toán bản đồ độ sâu.
-   Phân tích và so sánh hiệu quả của các phương pháp khác nhau.
-   Thực hành điều chỉnh các tham số để cải thiện kết quả.

Cấu trúc Dự án
--------------

Dự án bao gồm các thư mục và tệp tin chính như sau:

-   `src/`: Chứa các script Python để triển khai các thuật toán.
-   `data/`: Thư mục lưu trữ các cặp ảnh stereo đầu vào.
-   `results/`: Thư mục lưu trữ các bản đồ độ sâu được tạo ra.
-   `README.md`: Tệp tài liệu này.
-   `requirements.txt`: Danh sách các thư viện Python cần thiết.

Phụ thuộc
---------

Dự án này yêu cầu các thư viện Python sau:

-   `opencv-python`: Thư viện OpenCV cho xử lý ảnh.
-   `numpy`: Thư viện NumPy cho tính toán số học.

Cài đặt các thư viện này bằng lệnh sau:

bash

Copy code

`pip install -r requirements.txt`

Hướng dẫn Cài đặt
-----------------

1.  **Clone dự án từ GitHub**:

    bash

    Copy code
```
    git clone https://github.com/yourusername/image-depth-estimation.git
    
    cd image-depth-estimation
```


2.  **Cài đặt các phụ thuộc**:

    bash

    `pip install opencv-python numpy`

3.  **Chạy các hàm tính toán**: Tùy thuộc vào bài toán bạn muốn thực hiện, bạn có thể chạy các script tương ứng.

    python


    `python src/problem_1.py`

4.  **Xem kết quả**: Các kết quả sẽ được lưu trong thư mục `results/` và bạn có thể mở chúng bằng trình xem ảnh.

Chi tiết các Bài toán
---------------------

### Bài toán 1: Pixel-Wise Matching

Bài toán này yêu cầu bạn triển khai phương pháp so khớp điểm ảnh (Pixel-Wise Matching). Đây là phương pháp cơ bản nhất, trong đó độ lệch (disparity) của từng điểm ảnh được xác định bằng cách tìm kiếm sự tương đồng giữa các điểm ảnh từ hai ảnh stereo.

**Cách thực hiện**:

1.  Đọc hai ảnh stereo (ảnh trái và ảnh phải) dưới dạng ảnh mức xám.
2.  Khởi tạo một ma trận zero để lưu trữ bản đồ độ sâu.
3.  Duyệt qua từng điểm ảnh trong ảnh trái và tìm điểm tương đồng nhất trong ảnh phải, trong một phạm vi disparity cho trước.
4.  Tính toán độ lệch dựa trên các hàm chi phí (cost function) như L1, L2.
5.  Lưu kết quả vào tệp tin trong thư mục `results/`.

**Hàm cần triển khai**:

-   `pixel_wise_matching_l1(left_image, right_image, disparity_range)`
-   `pixel_wise_matching_l2(left_image, right_image, disparity_range)`

### Bài toán 2: Window-Based Matching

Phương pháp so khớp dựa trên cửa sổ (Window-Based Matching) nâng cao độ chính xác bằng cách so sánh một vùng (window) thay vì chỉ một điểm ảnh duy nhất.

**Cách thực hiện**:

1.  Đọc hai ảnh stereo và chuyển đổi sang định dạng `np.float32`.
2.  Khởi tạo một ma trận zero để lưu trữ bản đồ độ sâu.
3.  Sử dụng một cửa sổ `k x k` để so khớp các vùng ảnh nhỏ từ hai ảnh.
4.  Tính toán độ lệch dựa trên các hàm chi phí L1 hoặc L2 cho toàn bộ cửa sổ.
5.  Lưu kết quả vào thư mục `results/`.

**Hàm cần triển khai**:

-   `window_based_matching_l1(left_image, right_image, disparity_range, kernel_size)`
-   `window_based_matching_l2(left_image, right_image, disparity_range, kernel_size)`

### Bài toán 3: Ảnh hưởng của Tham số đến Bản đồ Độ sâu

Trong bài toán này, bạn sẽ thực hiện các thử nghiệm để đánh giá ảnh hưởng của các tham số khác nhau như kích thước cửa sổ (kernel size) và phạm vi độ lệch (disparity range) đến chất lượng của bản đồ độ sâu.

**Cách thực hiện**:

1.  Sử dụng các hàm đã triển khai ở bài toán 2.
2.  Thay đổi các tham số như `kernel_size` và `disparity_range`.
3.  Quan sát và so sánh các bản đồ độ sâu tạo ra.
4.  Lưu các kết quả với các thông số khác nhau để so sánh.

**Phân tích**:

-   Kích thước cửa sổ lớn hơn thường mang lại kết quả mượt mà hơn nhưng có thể mất chi tiết.
-   Phạm vi độ lệch lớn hơn có thể cải thiện độ chính xác nhưng sẽ tăng thời gian tính toán.

### Bài toán 4: So sánh Cosine

Trong bài toán này, bạn sẽ thay thế các hàm chi phí L1 và L2 bằng hàm **cosine similarity** để tính toán sự tương đồng giữa các vùng ảnh.

**Cách thực hiện**:

1.  Triển khai hàm tính cosine similarity giữa hai cửa sổ ảnh.
2.  Sử dụng hàm này thay cho L1/L2 trong bài toán 2.
3.  Tính toán bản đồ độ sâu bằng phương pháp mới này.
4.  Lưu kết quả vào thư mục `results/`.

**Hàm cần triển khai**:

-   `cosine_similarity(window1, window2)`

**Phân tích**:

-   Cosine similarity có thể cho kết quả tốt hơn trong một số trường hợp nhất định, đặc biệt khi các cửa sổ có cường độ sáng khác nhau.

Kết quả Dự án
-------------

Tất cả các bản đồ độ sâu được tạo ra sẽ được lưu trong thư mục `results/`. Bạn có thể mở các tệp này bằng các phần mềm xem ảnh để kiểm tra chất lượng của chúng.

-   **Bản đồ độ sâu gốc**: Sử dụng grayscale để biểu diễn.
-   **Bản đồ màu**: Sử dụng color map để dễ dàng quan sát.

Tài liệu Tham khảo
------------------

-   Bộ ảnh Tsukuba: [Tải về tại đây](https://drive.google.com/file/d/14gf8bcym_lTcvjZQmg8kwq3aXkENBxMQ/view?usp=sharing)
-   Bộ ảnh Aloe: [Tải về tại đây](https://drive.google.com/file/d/1wxmiUdqMciuTOs0ouKEISl8-iTVXdOWn/view?usp=sharing)
-   Tài liệu tham khảo về phương pháp Stereo Matching và Disparity Estimation.