# GridView 设置 item 间距的方法
- Android,开发,gridview,

GridView 提供这么两个方法 setHorizontalSpacing(int) 和 setVerticalSpacing(int)。API的DOC如下：


## setHorizontalSpacing

### public void setHorizontalSpacing(int horizontalSpacing)

Set the amount of horizontal (x) spacing to place between each item in the grid.

Parameters:horizontalSpacing The amount of horizontal space between items, in pixels.

@attr ref android.R.styleable#GridView_horizontalSpacing

## setVerticalSpacing

### public void setVerticalSpacing(int verticalSpacing)

Set the amount of vertical (y) spacing to place between each item in the grid.

Parameters:verticalSpacing The amount of vertical space between items, in pixels.

@attr ref android.R.styleable#GridView_verticalSpacing


注意：这里设置的是item之间的间隔,space between items.
