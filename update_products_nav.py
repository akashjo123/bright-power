import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We replace >Products</a> with >Products and Services</a>
    # This safely targets both the header and footer instances
    if '>Products</a>' in content:
        content = content.replace('>Products</a>', '>Products and Services</a>')
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"No match found in {file}")
