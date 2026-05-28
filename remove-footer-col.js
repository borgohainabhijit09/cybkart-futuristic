const fs = require('fs');
const files = ['index.html', 'services.html', 'industries.html', 'toolkit.html', 'portfolio.html', 'pricing.html', 'contact.html'];
files.forEach(f => {
  let c = fs.readFileSync(f, 'utf8');
  c = c.replace(/^[ \t]*<!-- Links column 2 \(Industries\) -->\r?\n[ \t]*<div class="footer-links-col">\r?\n[ \t]*<span class="footer-col-title">Industries<\/span>\r?\n[ \t]*<\/div>\r?\n/gmi, '');
  fs.writeFileSync(f, c);
});
console.log("Done.");
