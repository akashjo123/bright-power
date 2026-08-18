import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Change footer background
    content = content.replace('background-color: #17231E;', 'background-color: var(--color-primary);')
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {file}")
