import json
import math

# GitHub's green contribution palette
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap(input_path="data/contributions.json", output_path="contrib-heatmap.svg"):
    with open(input_path, "r") as f:
        data = json.load(f)
        
    box_size = 11
    gap = 4
    cols = math.ceil(len(data) / 7)
    
    # Calculate dimensions
    width = cols * (box_size + gap)
    height = 7 * (box_size + gap)
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        '    .box { opacity: 0; transform: translateY(-5px); animation: dropIn 0.3s ease-out forwards; }',
        '    @keyframes dropIn {',
        '      to { opacity: 1; transform: translateY(0); }',
        '    }',
        '  </style>'
    ]
    
    for i, day in enumerate(data):
        col = i // 7
        row = i % 7
        x = col * (box_size + gap)
        y = row * (box_size + gap)
        color = PALETTE[day["level"]]
        
        # Diagonal slide-in delay
        delay = (col + row) * 0.02
        svg.append(f'  <rect class="box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation-delay: {delay}s;" />')
        
    svg.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Done! Saved heatmap SVG to {output_path}")

if __name__ == "__main__":
    render_heatmap()