
import os

def test_download(page):

    page.goto("https://demoqa.com/upload-download", wait_until = 'commit')

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))
