const fs = require('fs');
const files = ['index.html', 'services.html', 'industries.html', 'toolkit.html', 'portfolio.html', 'pricing.html', 'contact.html'];
files.forEach(f => {
  let c = fs.readFileSync(f, 'utf8');
  c = c.replace(/^[ \t]*<a href=\"(?:industries|toolkit)\.html\"[^>]*>.*?<\/a>\r?\n/gmi, '');
  fs.writeFileSync(f, c);
});
console.log("Done.");
