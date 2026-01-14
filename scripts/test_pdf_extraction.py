import pdfplumber
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_text_boxes_with_matplotlib(pdf_path, output_dir):
    """
    Draws the text boxes on each page of the PDF to visualize how text is interpreted.

    Args:
        pdf_path (str): The path to the PDF file.
        output_dir (str): The directory where to save the images with drawn text boxes.
    """
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            print(f"Processing page {page_number + 1}")

            # Get page dimensions
            page_width = page.width
            page_height = page.height

            # Create a new figure
            fig, ax = plt.subplots(1, figsize=(10, 15))
            ax.set_xlim(0, page_width)
            ax.set_ylim(page_height, 0)
            ax.axis("off")

            # Plot the text boxes
            for char in page.chars:
                x0, y0, x1, y1 = char["x0"], char["top"], char["x1"], char["bottom"]
                rect = patches.Rectangle(
                    (x0, y0),
                    x1 - x0,
                    y1 - y0,
                    linewidth=1,
                    edgecolor="r",
                    facecolor="none",
                )
                ax.add_patch(rect)

            # Convert the PDF page to an image and plot it as the background
            im = page.to_image(resolution=150).original
            ax.imshow(im, extent=[0, page_width, page_height, 0], aspect="auto")

            # Save the visual representation
            output_path = f"{output_dir}/page_{page_number + 1}_text_boxes.png"
            plt.savefig(output_path, bbox_inches="tight")
            plt.close(fig)
            print(f"Saved visual representation to {output_path}")


if __name__ == "__main__":
    pdf_path = "data/demo_eso.pdf"  # Path to your PDF file
    output_dir = "output_visuals"  # Directory to save images
    draw_text_boxes_with_matplotlib(pdf_path, output_dir)
