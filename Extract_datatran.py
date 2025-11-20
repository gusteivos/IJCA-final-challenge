import os
import gdown
import zipfile


datatran = [
    {
        'google_drive_id' : '1-G3MdmHBt6CprDwcW99xxC4BZ2DU5ryR',
        'year'            : 2025,
    },
    {
        'google_drive_id' : '14lB0vqMFkaZj8HZ44b0njYgxs9nAN8KO',
        'year'            : 2024,
    }
]


def extract_datatran():
    for csv in datatran:
        google_drive_id = csv["google_drive_id"]
        year = csv["year"]

        zip = os.path.join('download', f"{google_drive_id}.zip")

        gdown.download(
            f"https://drive.google.com/uc?id={google_drive_id}",
            zip,
            quiet=False
        )

        with zipfile.ZipFile(zip, "r") as zip_ref:
            zip_ref.extractall('medallion/bronze')


if __name__ == '__main__':
    extract_datatran()
