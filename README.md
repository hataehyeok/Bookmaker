# Bookmaker

## Introduction

This project is for making pdf file from purchased ebook through taking screen capture on ebook viewer in which created pdf file is followed the copyright law so user have to only use pdf file for your study.

## Motivation

Ebook viewer is discomfort in study because lineing, notetaking, bookmark is not supported and most students is already familier on ipad app such as [Goodnote](https://www.goodnotes.com/). When student wants to use their notetaking app for studying their ebook, they can use this program for make pdf book from ebook viewer.

## Installation

To run Bookmaker on your local machine, you need to have Python installed. Follow these steps:

1. Clone the repository

    ```bash
    git clone https://github.com/hataehyeok/Bookmaker.git
    cd Bookmaker
    ```

2. Install the required Python packages

    ```bash
    pip install -r requirements.txt
    ```

3. Setting page's pixel size in ebook view (IMPORTANT)

    ```python
    # page pixel size
    x_pos = 412
    y_pos = 40
    width = 689
    height = 944
    ```

    Above code is in `src/take_image.py` and setting is based on my laptop MacBook Pro 14-inch, 2021 and viewing single page on viewer app. If you are not match my machine's environmnet, you have to set your own page pixel size and also have to take care your monitor scale and resolutions.

4. Run the program

    ```bash
    python3 main.py <folder_name> <output_name> <page_count>
    ```

    Like situation you take a photo, this program count ***three second*** and inside countdown, you should turn your screen to viewer's screen that open the ebook screen will be taken. And ebook page is certainly passed when press the right key. Maybe some authority acess is required.

## Copyright Law

MUST FOLLOW COPYLIGHT LAW. You only allowed when you using ebook's pdf version in your personal study don't share pdf to other person.

## Contact

For any additional questions or comments, please contact the repository owner. Refer to my github profile, you can contact and question.
