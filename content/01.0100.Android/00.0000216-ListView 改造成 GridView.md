# ListView 改造成 GridView
- 2013-03-30 10:55:41
- 
- android,listview,gridview,scrollview,

<div><br /></div><div>接上文。<a href="http://www.binkery.com/post.php?p=215">ScrollView 嵌套 GridView 或者 ListView</a></div><div><br /></div><div>不管怎么说，我总觉得在ScrollView里使用GridView本身就是个bug。</div><div>今天加班了，用ListView替代。最终貌似是实现了，一些小细节还没有处理，不过整体来说应该是能满足需求的。</div><div>在SimpleCursorAdapter的子类里，重写swapCursor方法，获取cursor对象。重写getCount方法，重新计算显示的行数。重写getView方法，不使用bindView 和 newView方法。</div><div><br /></div><div>在getView的使用，根据当前的position去调用cursor.moveToPosition ， 一行显示几个都行，稍微处理一下。</div><div><br /></div><div>大概思路是这样的，就是一些小细节得考虑清楚了。还有就是OnItemClickListener 和 ContextMenu得另外处理。可以给每个item设置onCliclListener 和 onLongClickListener ，在onLongClickListener 里，可以弹出一个Dialog出来，效果可以跟ContextMenu 差不多。</div>