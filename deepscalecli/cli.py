from cv2 import dnn_superres
import numpy as np
import datetime
import time
import typer
import os
import cv2


welcome: str = """deepscalecli \n\n Deep learning photography up-scaling using OpenCV and Typer."""

app = typer.Typer(help=welcome, no_args_is_help=True)


@app.command()
def about():
    response = """
    deepscalecli @ OpenCV photography up-scaler.   
    """

    print(response)


@app.command(help="Scale photos using appropriate scale (x2, x3, x4). \n $ deepscalecli scale 3")
def scale(size: int):
    path = r'./source'
    files = os.listdir(path)

    if len(files) > 0:
        print(f"\n Found {len(files)} files in source folder. \nStarting deep learning up-scale procedure using: {size} scale model: \n")

        with typer.progressbar(files) as progress:
            for file in progress:
                date_time = datetime.datetime.now()
                timestamp = time.mktime(date_time.timetuple())

                sr = dnn_superres.DnnSuperResImpl_create()

                image = cv2.imread(f'./source/{file}')

                model_path = f"./models/EDSR_x{size}.pb"
                sr.readModel(model_path)
                sr.setModel("edsr", size)

                result = sr.upsample(image)

                cv2.imwrite(f"./results/{timestamp}_{file}", result)

                typer.echo(file)

        print(f"\n\n Scaled up all: {len(files)} images. \n All results can be found in ./results directory.")

    else:
        print(f"Please, put your source images into `source` directory in order to scale them up.")


@app.command(help="Scan `source` directory.")
def files():
    try:
        path = r'./source'
        source_files = os.listdir(path)

        if len(source_files) > 0:
            print(f"Files found in `source` directory: \n")
            for file in source_files:
                print(f"\t * {file}")
        else:
            print("Found no files in `source` directory.")
    except OSError as err:
        print(f"An exception has been raised: {err}")


@app.command(help="Cleanup `results` directory.")
def cleanup():
    try:
        path = r'./results'
        source_files = os.listdir(path)

        if len(source_files) > 0:
            print(f"Files found in `target` directory, removing: \n")
            for file in source_files:
                os.remove(f"./results/{file}")
                print(f"\t * {file}")
        else:
            print("Found no files in `target` directory.")
    except OSError as err:
        print(f"An exception has been raised: {err}")


if __name__ == "__main__":
    app()
