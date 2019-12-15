# Chrome 插件开发 - background
- Chrome,插件开发,background
- 2019.03.22

background 是 Chrome 插件比较重要的一个部分。是 Chrome 插件生命周期最长的一个组件。background 的生命周期在 Chrome 启动后，启用的插件会被启动，background.js 或者 background.html 会被执行，如果是 background.html ，那么它是一个看不见的虚拟的网页的存在。如果是 background.js 的话，其实也可以理解为有一个虚拟的 html 页面。
