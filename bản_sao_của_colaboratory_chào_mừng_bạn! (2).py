# -*- coding: utf-8 -*-
"""Bản sao của Colaboratory chào mừng bạn!

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yLWIVcV5f7KNR24SyWMG1G_xlh4_J3sp

<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>Colaboratory là gì?</h1>

Colaboratory &#40;gọi tắt là "Colab"&#41; cho phép bạn viết và thực thi Python trong trình duyệt với các lợi ích sau: 
- Không yêu cầu cấu hình
- Sử dụng miễn phí GPU
- Chia sẻ dễ dàng

Cho dù bạn là <strong>sinh viên</strong>, <strong>nhà khoa học dữ liệu</strong> hay <strong>nhà nghiên cứu AI &#40;trí tuệ nhân tạo&#41;</strong>, Colab đều giúp bạn hoàn thành công việc dễ dàng hơn. Hãy xem phần <a href="https://www.youtube.com/watch?v=inN8seMm7UI">Hướng dẫn về Colab</a> để tìm hiểu thêm hoặc bắt đầu ngay ở bên dưới!

## <strong>Bắt đầu</strong>

Tài liệu bạn đang đọc không phải là trang web tĩnh, mà là một môi trường tương tác được gọi là <strong>sổ tay trên Colab</strong>. Trên đó, bạn có thể viết và thực thi mã.

Ví dụ: sau đây là một <strong>ô chứa mã</strong> có tập lệnh Python ngắn tính toán một giá trị, lưu trữ giá trị đó trong một biến và in kết quả:
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""Để thực thi mã trong ô trên, hãy nhấp để chọn mã đó rồi nhấn nút phát ở bên trái mã hoặc sử dụng tổ hợp phím tắt "Command/Ctrl+Enter". Để chỉnh sửa mã này, bạn chỉ cần nhấp vào ô đó và bắt đầu chỉnh sửa.

Các biến mà bạn xác định trong một ô có thể dùng trong các ô khác sau này:
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Sổ tay trên Colab cho phép bạn kết hợp <strong>mã có thể thực thi</strong> và <strong>văn bản đa dạng thức</strong> trong một tài liệu duy nhất, cùng với <strong>hình ảnh</strong>, <strong>HTML</strong>, <strong>LaTeX</strong> và nhiều nội dung khác. Khi bạn tạo sổ tay của riêng mình trên Colab, các sổ tay đó sẽ được lưu trữ trong tài khoản Google Drive của bạn. Bạn có thể dễ dàng chia sẻ sổ tay của mình trên Colab với đồng nghiệp hoặc bạn bè, cho phép họ nhận xét hoặc thậm chí là chỉnh sửa các sổ tay đó. Để tìm hiểu thêm, hãy xem phần <a href="/notebooks/basic_features_overview.ipynb">Tổng quan về Colab</a>. Để tạo một sổ tay mới trên Colab, bạn có thể sử dụng trình đơn Tệp ở trên hoặc sử dụng đường liên kết sau: <a href="http://colab.research.google.com#create=true">tạo một sổ tay mới trên Colab</a>.

Sổ tay trên Colab là các sổ tay Jupyter được Colab lưu trữ. Để tìm hiểu thêm về dự án Jupyter, hãy xem <a href="https://www.jupyter.org">jupyter.org</a>.

## Khoa học dữ liệu

Với Colab, bạn có thể khai thác toàn bộ sức mạnh của các thư viện Python phổ biến để phân tích và trực quan hóa dữ liệu. Ô chứa mã ở bên dưới sử dụng <strong>numpy</strong> để tạo một số dữ liệu ngẫu nhiên và sử dụng <strong>matplotlib</strong> để trực quan hóa dữ liệu đó. Để chỉnh sửa mã này, bạn chỉ cần nhấp vào ô đó và bắt đầu chỉnh sửa.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""Bạn có thể nhập dữ liệu của riêng mình vào các sổ tay trên Colab từ tài khoản Google Drive, bao gồm từ bảng tính, cũng như từ GitHub và nhiều nguồn khác. Để tìm hiểu thêm về cách nhập dữ liệu và cách áp dụng Colab cho ngành khoa học dữ liệu, hãy xem các đường liên kết trong phần <a href="#working-with-data">Làm việc với dữ liệu</a>.

## Máy học

Với Colab, chỉ cần sử dụng <a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb">một vài dòng mã</a> là bạn có thể nhập tập dữ liệu hình ảnh, huấn luyện một trình phân loại hình ảnh dựa trên tập dữ liệu đó và đánh giá mô hình này. Sổ tay trên Colab thực thi mã trên các máy chủ đám mây của Google. Nhờ đó, bạn có thể tận dụng sức mạnh của phần cứng Google, bao gồm cả <a href="#using-accelerated-hardware">GPU và TPU</a>, cho dù máy tính của bạn sử dụng sức mạnh phần cứng nào. Bạn chỉ cần một trình duyệt.

Colab được sử dụng rộng rãi trong cộng đồng máy học với các ứng dụng như:
- Bắt đầu sử dụng TensorFlow
- Phát triển và huấn luyện mạng nơron
- Thử nghiệm có sử dụng TPU
- Phổ biến nghiên cứu về AI &#40;trí tuệ nhân tạo&#41;
- Tạo hướng dẫn

Để xem các sổ tay mẫu trên Colab minh họa các ứng dụng dùng mô hình máy học, hãy xem <a href="#machine-learning-examples">các ví dụ về máy học</a> ở bên dưới.

## Tài nguyên khác

### Làm việc với Sổ tay trong Colab
- [Tổng quan về Colaboratory](/notebooks/basic_features_overview.ipynb)
- [Hướng dẫn sử dụng Markdown](/notebooks/markdown_guide.ipynb)
- [Nhập thư viện và cài đặt phần phụ thuộc](/notebooks/snippets/importing_libraries.ipynb)
- [Lưu và tải sổ tay trong GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Biểu mẫu tương tác](/notebooks/forms.ipynb)
- [Tiện ích tương tác](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [TensorFlow 2 trong Colab](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Làm việc với dữ liệu
- [Tải dữ liệu: Drive, Trang tính và Google Cloud Storage](/notebooks/io.ipynb) 
- [Biểu đồ: trực quan hóa dữ liệu](/notebooks/charts.ipynb)
- [Bắt đầu sử dụng BigQuery](/notebooks/bigquery.ipynb)

### Khóa học máy học ứng dụng
Khóa học trực tuyến của Google về Máy học có cung cấp một số sổ tay. Hãy xem <a href="https://developers.google.com/machine-learning/crash-course/">trang web của toàn bộ khóa học</a> để biết thêm thông tin.
- [Giới thiệu về Pandas](/notebooks/mlcc/intro_to_pandas.ipynb)
- [Các khái niệm về Tensorflow](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
- [Các bước đầu tiên khi sử dụng TensorFlow](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
- [Giới thiệu về mạng nơron](/notebooks/mlcc/intro_to_neural_nets.ipynb)
- [Giới thiệu về tính năng nhúng và dữ liệu thưa](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)

<a name="using-accelerated-hardware"></a>
### Sử dụng phần cứng tăng tốc
- [TensorFlow có GPU](/notebooks/gpu.ipynb)
- [TensorFlow có TPU](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Ví dụ về máy học

Để xem các ví dụ toàn diện về những phép phân tích máy học tương tác mà Colaboratory có thể hỗ trợ, hãy xem các hướng dẫn sau bằng cách sử dụng các mô hình từ <a href="https://tfhub.dev">TensorFlow Hub</a>.

Một vài sổ tay mẫu nổi bật:

- <a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining">Huấn luyện lại trình phân loại hình ảnh</a>: Tạo một mô hình Keras cùng với trình phân loại hình ảnh đã được huấn luyện trước để phân biệt các loại hoa.
- <a href="https://tensorflow.org/hub/tutorials/tf2_text_classification">Phân loại văn bản</a>: Phân loại các bài đánh giá phim trên IMDB là <em>tích cực</em> hoặc <em>tiêu cực</em>.
- <a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization">Sao chép phong cách</a>: Sử dụng mô hình học sâu để sao chép phong cách giữa các hình ảnh.
- <a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa">Hỏi và đáp về Bộ mã hóa câu tổng quát đa ngôn ngữ</a>: Sử dụng một mô hình máy học để giải đáp các câu hỏi từ tập dữ liệu SQuAD.
- <a href="https://tensorflow.org/hub/tutorials/tweening_conv3d">Nội suy video</a>: Dự đoán những điều đã xảy ra trong một video từ khung hình đầu tiên đến khung hình cuối cùng.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#assign column names to the dataset
names = ['sepal-length','sepal-width','petal-length','petal-width','Class']
#Read dataset to pandas dataframes
dataset = pd.read_csv(url,names=names)
dataset.head()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

error = []

# Calculating error for K values between 1 and 40
for i in range(, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(5, 18))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')