import os
from google_images_download import google_images_download


def imageCrawling(keyword, dir):

    response = google_images_download.googleimagesdownload()

    arguments = {"keywords":keyword,
                 "limit":100,
                 "print_urls":True,
                 "no_directory":True,
                 "output_directory":dir}

    paths = response.download(arguments)
    print(paths)

prefix = "오마이걸"
for member in ["효정", "유아", "승희", "미미", "비니", "지호", "아린"]:
    if not os.path.isdir(member):
        os.makedirs(member)
    imageCrawling(prefix+member, member)