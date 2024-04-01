# YouTube OCR to PowerPoint

This script downloads a YouTube video, processes its frames, performs OCR (Optical Character Recognition) on each frame, and generates a PowerPoint presentation containing the extracted text and corresponding frames.

## Installation

1. Navigate to the root directory of the project.
    ```
    cd youtube_ppt
    ```

3. Install the required Python packages:

    ```
    pip install .
    ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.
     ```
    cd youtube_ppt
    ```

3. Run the script using the following command format:

    ```
    python -m youtube_ocr.ocr <youtube_link> <output_pptx> <similarity_percentage>
    ```

    Replace `<youtube_link>` with the link to the YouTube video you want to process, and `<output_pptx>` with the desired filename for the output PowerPoint presentation.

    For example:

    ```
    python -m youtube_ocr.ocr "https://www.youtube.com/watch?v=ZlxSzizMP6w&ab_channel=VenkateshS.Kadandale" "output_presentation.pptx" 10
    ```

4. Press Enter to execute the command.

5. The script will start processing the YouTube video and generate the PowerPoint presentation. You can find the output file in the same directory where the script is run.

