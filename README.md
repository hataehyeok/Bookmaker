# Bookmaker

## Introduction

Bookmaker is a tool designed to create PDF files from purchased ebooks by taking screenshots of the ebook viewer. This tool is developed with the intention of aiding students in their studies by converting ebooks into more accessible PDF formats. The created PDF files are intended for personal use only, in compliance with copyright laws, ensuring that users utilize the PDFs solely for their study purposes.

## Motivation

Many ebook viewers lack essential features for studying, such as highlighting, note-taking, and bookmarking. These limitations can hinder the learning experience, especially for students accustomed to using comprehensive note-taking apps like [GoodNotes](https://www.goodnotes.com/) on their iPads. Bookmaker addresses this issue by allowing students to convert their ebooks into PDF format, enabling them to study more effectively using their preferred apps.

## Installation

To get started with Bookmaker on your local machine, ensure you have Python installed. Follow these steps to set up the project:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/hataehyeok/Bookmaker.git
    cd Bookmaker
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the page pixel size in the ebook viewer (IMPORTANT):**

    The `src/take_image.py` file contains code for setting the page pixel size, tailored to a 14-inch MacBook Pro (2021), viewing a single page in the viewer app. If your setup differs, adjust the pixel size settings to match your monitor's scale and resolution:

    ```python
    # page pixel size
    x_pos = 412
    y_pos = 40
    width = 689
    height = 944
    ```

4. **Run the program:**

    Execute the program with the following command:

    ```bash
    python3 main.py <folder_name> <output_name> <page_count>
    ```

    Prepare your screen by switching to the ebook viewer within the three-second countdown. Pages can be turned by pressing the right arrow key. Note that some permissions may be required.

## Copyright Law

It is imperative to FOLLOW COPYRIGHT LAW. The PDF versions of ebooks created using Bookmaker are allowed for personal study use only. Do not distribute or share the PDFs with others.

## Contact

Should you have any questions or comments, feel free to reach out to the repository owner. Visit my GitHub profile for contact information and inquiries.
