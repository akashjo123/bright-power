const fs = require('fs');
const path = require('path');

const dir = '/Users/apple/Documents/bright power/';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  // Skip if already has Blog link
  if (content.includes('<a href="blog.html"')) {
    console.log(`Skipping ${file}, already has Blog link.`);
    return;
  }

  if (file === 'blog.html' || file === 'blog-detail.html') {
    content = content.replace(
      '      <a href="contact.html">Contact</a>',
      '      <a href="blog.html" class="active">Blog</a>\n      <a href="contact.html">Contact</a>'
    );
  } else if (file === 'contact.html') {
    content = content.replace(
      '      <a href="contact.html" class="active">Contact</a>',
      '      <a href="blog.html">Blog</a>\n      <a href="contact.html" class="active">Contact</a>'
    );
  } else {
    content = content.replace(
      '      <a href="contact.html">Contact</a>',
      '      <a href="blog.html">Blog</a>\n      <a href="contact.html">Contact</a>'
    );
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Updated ${file}`);
});
