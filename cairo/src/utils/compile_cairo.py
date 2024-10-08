import logging
import subprocess
import sys
from pathlib import Path

# Configure the logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def compile_cairo(file_name):
    input_path = Path(file_name)
    output_path = input_path.with_suffix(".json")

    command = [
        "cairo-compile",
        str(input_path),
        "--output",
        str(output_path),
        "--proof_mode",
        "--no_debug_info",
        "--cairo_path",
        str(Path(__file__).parents[2]),
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        logger.info("Compilation successful.")
        try:
            subprocess.run(["trunk", "fmt", str(output_path)])
        except Exception as e:
            logger.error("Formatting failed.")
            logger.error(e)
    else:
        logger.error("Compilation failed.")
        logger.error(result.stderr)


def compile_os():
    compile_cairo(Path(__file__).parents[2] / "programs" / "os.cairo")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python compile_cairo.py <file_name>")
    else:
        compile_cairo(sys.argv[1])
