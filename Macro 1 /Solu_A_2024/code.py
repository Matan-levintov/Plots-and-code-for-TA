import base64

def translate_to_64(id : str, course_code : str, semester: str, year:str):
    return base64.b64encode(f"{id}:{year}:{semester}:0:1:{course_code}:1:1".encode()).decode()








print(translate_to_64("208682666", "1221", "1", "142"))









# 208682666:2024:1:0:1:142.1.1221:1:1