# yue.css

**yue.css** is a typography stylesheet for readable content. It was
created for my blog at first since I always designed a new theme for my
blog. But later it becomes the offical stylesheet for yuehu site.

> **yue.css** is not a reset stylesheet.

It is designed for article content, and only article content. If you are
looking for a reset css, you are watching the wrong repository.

## Installation

Install with [component(1)](http://component.io):

    $ component install lepture/yue.css

However, if you don't fancy component, you can just grab the css file
from GitHub. There is no dependency of [this project](https://github.com/lepture/yue.css).

## API

For readable content, wrapper them under the `.yue` class, and everything
would be ok now:

```css
<div class="yue">
    <h1>Heading</h1>
    <p>Paragraph of contents...</p>
</div>
```

## Tags

**yue.css** only supports selected tags which are commonly used in an
article.

Tag Name   | Description
---------- | -----------------------------
h1 - h6    | headings for title
p          | paragraph
a          | anchor links
strong b   | emphasis in bold style
em i       | emphasis in italic style
img        | image
figure     | figure wrapper for images
figcaption | figcaption in figure
hr         | separator
blockquote | style for quotes
ul ol li   | ordered and unordered list
pre        | code block
code tt    | inline code
table ..   | tables (not well designed)
iframe     | embed iframe style


### Headings

Headings are tags `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>` and `<h6>`.
But the most commonly used tags are `<h1>`, `<h2>`, and `<h3>`.

### Emphasis

Emphasis works on something **important** or *valuable*. `<b>` and `<i>`
are not designed for this purpose, you should always use `<strong>` and `<em>`.

### Links & Images

Links are the soul of internet. [Fork it on GitHub](https://github.com/lepture/yue.css).

![art of human body](http://lab.lepture.com/gaussian-blur/art.jpg)

Images can be wrappered in a `<figure>` tag:

![art of human body](http://lab.lepture.com/gaussian-blur/art.jpg "The Art of Human Body")

### List

There is ordered list `<ol>` and unordered list `<ul>`.

* Unordered list is tagged in `<ul>`
* Another item of unordered list
    1. An ordered list in un ordered list
    2. Another ordered item
* Unordered list can has unordered list children
    * Item of the children
    * Another item of the children

----

1. Ordered list is tagged in `<ol>`
2. Each item is tagged in `<li>`

----

## Note

yue.css has no target language, however it looks great in both English
and Chinese.

> yue.css 并不是为某一特定语言设计的，但是它确实在英文和中文上表现出色。

## License

MIT for personal websites only. Commercial websites should contact me
for more information.
