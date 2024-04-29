import os

from dotenv import load_dotenv

load_dotenv()
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


def detect(post):
    """
    Detects and generates new content based on the input post.

    Parameters:
        post (str): The post to detect and generate new content from.

    Returns:
        str: The newly generated content based on the input post.
    """
    # Create a generative model for generating new content
    model = genai.GenerativeModel("gemini-pro")

    # Path to the file containing the prompt
    file_path = "./prompt.txt"

    # Read the content of the prompt file
    with open(file_path, "r") as file:
        prompt = file.read()

    # Combine the prompt and the post to create input for the model
    input_text = prompt + str(post)

    # Generate new content based on the input
    response = model.generate_content(input_text)

    # Return the newly generated content
    return response.text


"""
 [DANANG] Meta Technology Lab vẫn cần tuyển Middle/Senior từ 3 năm+ kinh nghiệm về tham gia dự án game bùng nổ tháng 5/2024
	1. Project manager
	2. Middle Blockchain
	3. Senior Cloud infrastructure
	4. Senior Unreal Engine
	Mức offer upto 3k5 cho các ứng viên tiềm năng cùng các trải nghiệm dự án
	Liên hệ:
	Mail: hr@metatechnologylab.io
	Zalo: 0336 256 356
	Skype: live:.cid.7d8bc6574e23c88b

"""
#     data = """
# 	CÔNG TY CỔ PHẦN GIẢI PHÁP SỐ AION TUYỂN DỤNG
# 	📣📣Vị trí: Inter/Fresher Video Editor
# 	📣📣Số lượng: 2
# 	🏢🏢 Nơi làm việc: Số 384 đường 2/9, Đà Nẵng
# 	✅️ Công việc
# 	Thực hiện Quay, dựng về các sản phẩm, dịch vụ của AIOM
# 	Chỉnh sửa, cắt dán, lồng ghép video, âm thanh, hình ảnh.
# 	Phối hợp với các phòng ban làm các nhiệm vụ liên quan.
# 	✅️ Quyền lợi:
# 	- Mức lương: thỏa thuận trực tiếp khi phỏng vấn
# 	- Môi trường trẻ 9x năng động sáng tạo
# 	- Có cơ hội thăng tiến dựa trên năng lực của bạn.
# 	- Các chính sách ưu đãi khác của công ty,... tham gia các hoạt động của công ty hằng tháng, năm.
# 	- Được cọ sát với dự án thực tế, nâng cao kinh nghiệm và năng lực bản thân.
# 	✅️ Yêu cầu:
# 	Biết sử dụng các phần mềm hỗ trợ: Adobe Premiere, Adobe After Effects, Capcut, PTS
# 	Có laptop cá nhân
# 	Ưu tiên có kinh nghiệm
# 	Lễ phép
# 	Chăm chỉ, chịu khó
# 	CHỦ ĐỘNG học hỏi và CHỦ ĐỘNG trong công việc
# 	Thời gian làm việc thứ 2 - 7. Sáng 8h30 - 12h30, chiều 13h30 - 17h30. (Thứ 7 làm remote)
# 	‼️ Liên hệ:
# 	- Hồ sơ gửi về mail: info@aioncard.vn - CV đặt theo cú pháp: CV_TenUngVien_ViTriUngTuyen (Những CV ko đặt tên theo đúng yêu cầu sẽ bị loại).
# 	- Số điện thoại: 0327611291 ( Mr Phát )
# 	- Địa chỉ: 384 đường 2/9, Hải Châu, Đà Nẵng
#  """
#     data_1 = """
# [DANANG] Meta Technology Lab vẫn cần tuyển Middle/Senior từ 3 năm+ kinh nghiệm về tham gia dự án game bùng nổ tháng 5/2024
# 	1. Project manager
# 	2. Middle Blockchain
# 	3. Senior Cloud infrastructure
# 	4. Senior Unreal Engine
# 	Mức offer upto 3k5 cho các ứng viên tiềm năng cùng các trải nghiệm dự án
# 	Liên hệ:
# 	Mail: hr@metatechnologylab.io
# 	Zalo: 0336 256 356
# 	Skype: live:.cid.7d8bc6574e23c88b
# 	"""
