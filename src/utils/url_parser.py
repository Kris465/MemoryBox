import re


def extract_course_id(url):
    match = re.search(r'course/(\d+)', url) or re.search(r'\d+', url)
    return match.group(1) if match else None
