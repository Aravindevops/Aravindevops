import cv2
import html

# Brightness ramp: White maps to leading space (clears background) -> Dark maps to @
RAMP = " .`:-=+*cs#%@"

def make_ascii_svg(input_path="source-prepped.png", output_path="avi-ascii.svg"):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read {input_path}")
        return

    cols, rows = 100, 53
    img_resized = cv2.resize(img, (cols, rows))
    
    ascii_grid = []
    for y in range(rows):
        row_str = ""
        for x in range(cols):
            pixel = img_resized[y, x]
            # Map 255 (white) to 0, 0 (black) to end of ramp
            idx = int((255 - pixel) / 255.0 * (len(RAMP) - 1))
            row_str += RAMP[idx]
        ascii_grid.append(row_str)

    char_width, char_height = 8, 14
    width, height = cols * char_width, rows * char_height
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '<style>',
        '  .text { font-family: monospace; font-size: 14px; fill: #a3a3a3; white-space: pre; }',
        '</style>',
        '<defs>'
    ]
    
    delay_per_row = 0.04
    duration = 0.8
    
    # Generate wiping clip-paths for each row
    for i in range(rows):
        delay = i * delay_per_row
        svg.append(f'  <clipPath id="clip-{i}">')
        svg.append(f'    <rect x="0" y="{i * char_height}" width="0" height="{char_height + 4}">')
        svg.append(f'      <animate attributeName="width" from="0" to="{width}" begin="{delay}s" dur="{duration}s" fill="freeze" />')
        svg.append('    </rect>')
        svg.append('  </clipPath>')
    svg.append('</defs>')
    
    # Render text rows
    for i, row_str in enumerate(ascii_grid):
        y_pos = (i + 1) * char_height
        safe_str = html.escape(row_str)
        svg.append(f'  <text x="0" y="{y_pos}" class="text" clip-path="url(#clip-{i})">{safe_str}</text>')
    
    svg.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Done! Saved SVG to {output_path}")

if __name__ == "__main__":
    make_ascii_svg()