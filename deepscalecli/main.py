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
          file: Annotated[str, typer.Argument()]):
    """
    Scale an image using specific model and factor.
    :param model:
    :param factor:
    :param file:
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

    current_directory = os.path.dirname(__file__)

    target_path = os.path.join(current_directory, f"results/{file}_{model}_x{factor}.jpg")
    model_path = os.path.join(current_directory, f"models/{model}_x{factor}.pb")
    image_path = os.path.join(current_directory, f"images/{file}")

    image = cv2.imread(image_path)

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel(model.lower(), factor)

    result = sr.upsample(image)

    cv2.imwrite(target_path, result)

    print(f"Image saved at {target_path}")
