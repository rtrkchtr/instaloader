# import instaloader as insta
# from datetime import datetime
#
# x = insta.Instaloader()
# # post_url = "https://www.instagram.com/p/B9d2STeHs3L"
# # file_destination = "C:/Users/kecht/Desktop/Test_Download_Instagram/"
# # x.download_pic(filename=file_destination, url=post_url, mtime=datetime.now().timestamp())
# # print(datetime)
# x.profile
# x.download_profilepic(profile=)
#
#
# x.download_profilepic(profile="idwyr")

#time is now


from itertools import islice
from math import ceil
import os

from instaloader import Instaloader, Profile

PROFILE = "gibsonclub"        # profile to download from
X_percentage = 20# percentage of posts that should be downloaded

L = Instaloader()
MAX_PICTURES_TO_DOWNLOAD = 120

profile = Profile.from_username(L.context, PROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)


i = 0
for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    x = L.download_post(post, PROFILE)
    #posts = L.get_hashtag_posts('urbanphotography')
    i += 1
    print(i)
    if i == MAX_PICTURES_TO_DOWNLOAD:
        break

# metadeaten, hashtag und mehr unter intstaloader/instaloder.py - Class Instaloader
# def download_post wegkommentieren

directory_prefix = 'C:/Users/kecht/Documents/MEGAsync/Code/PyCharm_Projects/Instaloader_Touchdesigner/instaloader/'

def create_textfile_for_td():
    directory = directory_prefix+PROFILE
    directory_inhalte = os.listdir(directory)
    if directory_inhalte != '':
        textfile = open(directory+"/td_image_paths.txt", "w+")
        textfile.write("name\tlink\n")
        i = 0
        print("Generating Textfile")
        for pic in directory_inhalte:
            if pic.endswith(".jpg"):
                base = os.path.basename(pic)
                textfile.write("insta_load_nr_"+str(i)+"\t"+directory+"/"+base+"\n")
                print("created entry for pic nr"+str(i))
                i += 1
                if i == MAX_PICTURES_TO_DOWNLOAD:
                    break


create_textfile_for_td()


# cmd via tcp

