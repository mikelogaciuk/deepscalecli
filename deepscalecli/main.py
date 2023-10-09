from deepscalecli.utils import chronometer
from typing_extensions import Annotated
from typing import Optional
import typer
import cv2
import os


welcome: str = """deepscalecli @ The simple and elegant scale tool"""
app = typer.Typer(help=welcome, no_args_is_help=True)


@app.callback()
def callback():
    """
    Welcome to deepscalecli! The simple and elegant scale tool.
    """


@app.command(help="Scale an image using specific model and factor.\n\n"
                  "Example:\n"
                  "  deepscalecli scale --model=ESPCN --factor=2 --file=example.png\n")
@chronometer
def scale(model: Annotated[str, typer.Argument()],
          factor: Annotated[int, typer.Argument()],
          source: Annotated[str, typer.Argument()],
          target: Annotated[str, typer.Argument()]
          ):
    """
    Scale images from specific directory using specific model and factor.
    :param model:
    :param factor:
    :param source:
    :param target:
    :return: image

    Available models:
        - ESPCN x2, x3, x4
        - FSRCNN x2, x3, x4
        - LapSRN x2, x4, x8

    Example:
        `deepscalecli scale espcn 4 example.png`
    """
    if model.lower() not in ["espcn", "fsrcnn", "lapsrn"]:
        raise typer.BadParameter("Model not available")

    model = model.upper() if model.lower() in ["espcn", "fsrcnn"] else "LapSRN"

    current_directory = os.getcwd()

    file_list = os.listdir(source)
    model_path = os.path.join(current_directory, f"models/{model}_x{factor}.pb")

    if not os.path.exists(target):
        os.makedirs(target)

    print(f"Found {len(file_list)} images in {source} directory")

    for file in file_list:

        file_path = f"{source}{file}"

        print(f"Processing {file_path}...")

        target_path = f"{target}/{model}_{factor}_{file}"

        if os.path.exists(target_path):
            print(f"Image {file} already processed")
            continue

        image = cv2.imread(file_path)

        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        sr.readModel(model_path)
        sr.setModel(model.lower(), factor)

        result = sr.upsample(image)

        cv2.imwrite(target_path, result)

        print(f"Image saved at {target_path}")
