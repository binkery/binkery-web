# Android ImageView 的 ScaleType 属性
- Android,imageview,scaletype,

Android ImageView 的 ScaleType 属性用来表示图片的显示方式。总共有8种取值，取值的范围定义在 android.widget.ImageView.ScaleType 这个枚举类型里。


 - ImageView.ScaleType.CENTER
 
居中，但不缩放。图片超出控件的部分不显示，小于控件的部分就留白。Center the image in the view , but perform no scaling .

 - ImageView.ScaleType.CENTER_CROP

 居中，缩放，裁剪。对图片进行等比例缩放，图片的宽高等于或大于控件对应的宽高，所以会有部分不能被显示出来。Scale the image uniformly (maintain the image's aspect ratio) so that both dimensions (width and height) of the image will be equal to or larger than the corresponding dimension of the view (minus padding). The image is then centered in the view. From XML, use this syntax: android:scaleType="centerCrop".

 - ImageView.ScaleType.CENTER_INSIDE

 居中，缩放。对图片进行等比例缩放，图片的宽高等于或小于控件相对应的宽高。和FIT_CENTER 不同的是，图片可能的宽高都同时可能比控件对应的宽高小。Scale the image uniformly (maintain the image's aspect ratio) so that both dimensions (width and height) of the image will be equal to or less than the corresponding dimension of the view (minus padding). The image is then centered in the view. From XML, use this syntax: android:scaleType="centerInside".

 - ImageView.ScaleType.FIT_CENTER

 居中，参考 android.graphics.Matrix.ScaleToFit.CENTER . 等比例缩放，但最少有一个边与控件对应的边是相等的。Compute a scale that will maintain the original src aspect ratio, but will also ensure that src fits entirely inside dst. At least one axis (X or Y) will fit exactly. The result is centered inside dst.

 - ImageView.ScaleType.FIT_END

 居下，等比例缩放，也是最少有个边与控件对应的边是相等的。参考 android.graphics.Matrix.ScaleToFit.END  Compute a scale that will maintain the original src aspect ratio, but will also ensure that src fits entirely inside dst. At least one axis (X or Y) will fit exactly. END aligns the result to the right and bottom edges of dst.

 - ImageView.ScaleType.FIT_START

 居上，等比例缩放，最少有个边与控件对应的边是相等的。参考 android.graphics.Matrix.ScaleToFit.START  Compute a scale that will maintain the original src aspect ratio, but will also ensure that src fits entirely inside dst. At least one axis (X or Y) will fit exactly. START aligns the result to the left and top edges of dst.

 - ImageView.ScaleType.FIX_XY

 不等比例缩放，X轴和Y轴都和控件对应的边相等，图片可能被拉伸。参考 android.graphics.Matrix.ScaleToFit.FILL  Scale in X and Y independently, so that src matches dst exactly. This may change the aspect ratio of the src.

 - ImageView.ScaleType.MATRIX

 根据一个矩阵对图片进行缩放。Scale using the image matrix when drawing. The image matrix can be set using setImageMatrix(Matrix). From XML, use this syntax: android:scaleType="matrix".