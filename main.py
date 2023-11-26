
import re

def scale_units(css, scale_factor):
    # Regular expression to match units like px, em, rem, pt, cm, mm, in, vh, vw, vmin, vmax, but not percentages
    unit_pattern = re.compile(r'(?<!\w)(\d+(\.\d+)?)(px|em|rem|pt|cm|mm|in|vh|vw|vmin|vmax)(?!\w)')

    # Function to scale a unit
    def scale_unit(match):
        value = float(match.group(1)) * scale_factor
        unit = match.group(3)
        return f'{value}{unit}'

    # Applying the scaling to all matched units
    return unit_pattern.sub(scale_unit, css)

def scale_css_file(input_path, scale_factor, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        css_content = file.read()

    scaled_css = scale_units(css_content, scale_factor)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(scaled_css)

# Example usage
input_path = 'calendar-style.css'  # Replace with your input file path
scale_factor = 0.4  # Replace with your desired scale factor
output_path = 'mod.css'  # Replace with your output file path

scale_css_file(input_path, scale_factor, output_path)