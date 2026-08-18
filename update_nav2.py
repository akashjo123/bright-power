import os

directory = '/Users/apple/Documents/bright power/'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    if file in ['blog.html', 'blog-detail.html']:
        content = content.replace(
            '      <a href="contact.html">Contact</a>',
            '      <a href="blog.html" class="active">Blog</a>\n      <a href="contact.html">Contact</a>'
        )
    elif file == 'contact.html':
        content = content.replace(
            '      <a href="contact.html" class="active">Contact</a>',
            '      <a href="blog.html">Blog</a>\n      <a href="contact.html" class="active">Contact</a>'
        )
    else:
        content = content.replace(
            '      <a href="contact.html">Contact</a>',
            '      <a href="blog.html">Blog</a>\n      <a href="contact.html">Contact</a>'
        )
        
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {file}")
