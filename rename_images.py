import os
import shutil
import PIL.Image as Image
import numpy as np

from tqdm import tqdm

for i in tqdm(os.listdir("images/")):
    org = f"images/{i}"
    if not org.endswith(".txt"):
        ext = "." + org.split(".")[-1]
        img = Image.open(org)  # type: ignore
        img = img.convert("RGB")
        new_fn = org.replace(ext, "_img.png")
        img.save(new_fn)  # type: ignore
        os.remove(org)

        # img = Image.open(org)  # type: ignore
        # # convert to grey
        img = img.convert("L")
        img = np.array(img)
        zeros_bg = np.zeros_like(img)
        ones_fg = np.ones_like(img)
        # stack images
        stacked = np.stack([zeros_bg, zeros_bg], axis=-1)  # (h,w,2)
        # save the stacked image
        new_fn = new_fn.replace("_img", "_mask")
        Image.fromarray(zeros_bg).save(new_fn)  # type: ignore

        # new_name = f"images/{i[:-4]}_img.{ext}"
        # shutil.copyfile(org, new_name)
        # os.remove(org)
