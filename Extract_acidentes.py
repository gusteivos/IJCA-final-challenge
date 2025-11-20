import os
import gdown
import zipfile


acidentes = [
    {
        'google_drive_id' : '1-Gp9S-ALO0D1nT8S_OKoC8xlW7BY8F82',
        'year'            : 2025,
    },
    {
        'google_drive_id' : '14lVfqdoE2gxDliaKZu7K9Mx6847maPtl',
        'year'            : 2024,
    }
]


def extract_acidentes():
    for csv in acidentes:
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
    extract_acidentes()
