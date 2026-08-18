import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Hero Overlays
    content = content.replace('rgba(8,43,76,0.9)', 'rgba(18,55,42,0.85)')
    content = content.replace('rgba(8,43,76,0.5)', 'rgba(18,55,42,0.75)')
    
    # Footer Backgrounds
    content = content.replace('background-color: #17212B;', 'background-color: #17231E;')
    
    # Footer text body
    content = content.replace('color: #ccc; margin-bottom: 4rem;', 'color: #AAB5AE; margin-bottom: 4rem;')
    
    # Social links
    content = content.replace('color: #ccc; background: rgba(255,255,255,0.1);', 'color: #DCE2DC; background: rgba(255,255,255,0.1);')
    
    # Logo Accents & Other hardcoded yellows
    content = content.replace('style="color: var(--color-secondary);"', 'style="color: var(--color-accent);"')
    
    # Borders
    content = content.replace('rgba(8,43,76,0.1)', 'var(--color-border)')
    
    # If any inline deep navy remains
    content = content.replace('color: #082B4C;', 'color: var(--color-primary);')
    content = content.replace('background-color: #082B4C;', 'background-color: var(--color-primary);')
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {file}")
