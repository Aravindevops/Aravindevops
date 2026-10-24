import os

def make_info_card(output_path="info-card.svg"):
    # SVG Dimensions and styling
    width, height = 490, 300
    font_family = "Consolas, 'Courier New', monospace"
    bg_color = "#0d1117"
    text_color = "#c9d1d9"
    accent_color = "#58a6ff"
    prompt_color = "#7ee787"

    # The content of your card (fixed the & character here)
    lines = [
        f'<tspan fill="{prompt_color}">aravind</tspan><tspan fill="{text_color}">@</tspan><tspan fill="{accent_color}">github</tspan>',
        '-------------------------',
        f'<tspan fill="{accent_color}">Role:</tspan> Full-Stack Web Developer',
        f'<tspan fill="{accent_color}">Stack:</tspan> React, Node.js, Python, SQL, Tailwind',
        f'<tspan fill="{accent_color}">Edu:</tspan> B.Tech CSE @ VISAT Engineering College',
        f'<tspan fill="{accent_color}">Focus:</tspan> Web Apps &amp; Agentic Workflows',
        f'<tspan fill="{accent_color}">Projects:</tspan> SkillGrid, Campustry, EduStream'
    ]

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'  <rect width="100%" height="100%" fill="{bg_color}" rx="8" />',
        '  <style>',
        f'    .text {{ font-family: {font_family}; font-size: 15px; fill: {text_color}; }}',
        '    .line { opacity: 0; animation: fadeInSlide 0.4s ease-out forwards; }',
        '    @keyframes fadeInSlide {',
        '      from { opacity: 0; transform: translateY(10px); }',
        '      to { opacity: 1; transform: translateY(0); }',
        '    }',
        '  </style>',
        '  <g class="text" transform="translate(20, 40)">'
    ]

    # Add each line with a staggered animation delay
    delay_step = 0.15
    y_spacing = 25
    
    for i, line in enumerate(lines):
        delay = 0.5 + (i * delay_step)
        y_pos = i * y_spacing
        svg.append(f'    <text x="0" y="{y_pos}" class="line" style="animation-delay: {delay}s;">{line}</text>')

    svg.append('  </g>')
    svg.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Done! Saved Info Card SVG to {output_path}")

if __name__ == "__main__":
    make_info_card()