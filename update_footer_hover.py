import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace inline style with a class
    content = content.replace('style="color: #ccc;"', 'class="footer-link"')
        
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {file}")
