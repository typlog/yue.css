const fs = require('fs');
const postcss = require('postcss');
const autoprefixer = require('autoprefixer');
const customProperties = require('postcss-custom-properties');

const css = fs.readFileSync('index.css', 'utf8');
const output = postcss()
  .use(customProperties())
  .use(autoprefixer())
  .process(css).css;
fs.writeFileSync('yue.css', output);
