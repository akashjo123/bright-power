import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

old_block = """          <h4 style="color: var(--color-white); margin-bottom: 1.5rem; font-size: 1.125rem;">Quick links.</h4>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.875rem;">
            <a href="index.html" style="color: #ccc;">Home</a>
            <a href="about.html" style="color: #ccc;">About Us</a>
            <a href="products-services.html" style="color: #ccc;">Order Online</a>
            <a href="projects.html" style="color: #ccc;">Projects</a>
          </div>"""

new_block = """          <h4 style="color: var(--color-white); margin-bottom: 1.5rem; font-size: 1.125rem;">Quick links.</h4>
          <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.875rem;">
            <a href="index.html" style="color: #ccc;">Home</a>
            <a href="about.html" style="color: #ccc;">About Us</a>
            <a href="products-services.html" style="color: #ccc;">Products</a>
            <a href="projects.html" style="color: #ccc;">Projects</a>
            <a href="blog.html" style="color: #ccc;">Blog</a>
            <a href="contact.html" style="color: #ccc;">Contact</a>
          </div>"""

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Target block not found in {file}")
