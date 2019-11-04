# Android官方文档 Starting an Activity
- 2015-03-10 11:14:44
- Android
- android,activity,翻译,官方文档,

<!--markdown-->## Starting an Activity 

You can start another activity by calling startActivity(), passing(通过) it an Intent that describes（描述） the activity you want to start. The intent specifies（指定） either the exact（确切的） activity you want to start or describes（描述） the type of action you want to perform（执行） (and the system selects the appropriate（适当的） activity for you, which can even be from a different application). An intent can also carry（携带） small amounts（小批量） of data to be used by the activity that is started.
When working within your own application, you'll often need to simply（简单的） launch a known activity. You can do so by creating an intent that explicitly（明确的） defines the activity you want to start, using the class name（类名）. For example, here's how one activity starts another activity named SignInActivity:

    Intent intent = new Intent(this, SignInActivity.class);
    startActivity(intent);

However, your application might also want to perform（执行） some action, such as send an email, text message, or status update, using data from your activity. In this case(在这种情况下), your application might not have its own activities to perform such actions, so you can instead leverage the activities provided by other applications on the device, which can perform the actions for you. （你的应用里没有activity来执行这些操作的时候，可以让手机里的其他程序里的activity来执行这些操作。）This is where intents are really valuable（有价值的）—you can create an intent that describes（描述） an action you want to perform and the system launches（启动） the appropriate（适合的） activity from another application. If there are multiple activities that can handle the intent（如果有多个activity能处理这个intent）, then the user can select which one to use（用户可以主动选择其中一个）. For example, if you want to allow the user to send an email message, you can create the following intent（这是一个发送邮件的例子）:

    Intent intent = new Intent(Intent.ACTION_SEND);
    intent.putExtra(Intent.EXTRA_EMAIL, recipientArray);
    startActivity(intent);

The EXTRA_EMAIL extra added to the intent is a string array of email addresses to which the email should be sent.（这个intent里EXTRA_EMAIL 附加的内容是email地址的string数组列表。） When an email application responds to this intent, it reads the string array provided in the extra and places them in the "to" field of the email composition（作文） form. In this situation（在这种情况下）, the email application's activity starts and when the user is done, your activity resumes（email应用被启动，用户执行完操作后会返回到你的activity的。）.

 
## Starting an activity for a result

Sometimes, you might want to receive a result from the activity that you start. （有时候你启动一个activity并希望从这个activity返回一个结果。）In that case, start the activity by calling startActivityForResult() (instead of startActivity()). To then receive the result from the subsequent activity, implement the onActivityResult() callback method.（通过实现onActivityResult()这个回调方法来接收返回的结果。） When the subsequent activity is done, it returns a result in an Intent to your onActivityResult() method.（返回的结果是一个intent，数据也被包含在里面了。）

For example, perhaps（假设） you want the user to pick one of their contacts, so your activity can do something with the information in that contact. Here's how you can create such an intent and handle the result:

    private void pickContact() {
        // Create an intent to "pick" a contact, as defined by the content provider URI
        Intent intent = new Intent(Intent.ACTION_PICK, Contacts.CONTENT_URI);
        startActivityForResult(intent, PICK_CONTACT_REQUEST);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // If the request went well (OK) and the request was PICK_CONTACT_REQUEST
        if (resultCode == Activity.RESULT_OK && requestCode == PICK_CONTACT_REQUEST) {
            // Perform a query to the contact's content provider for the contact's name
            Cursor cursor = getContentResolver().query(data.getData(),new String[] {Contacts.DISPLAY_NAME}, null, null, null);
            if (cursor.moveToFirst()) { // True if the cursor is not empty
                int columnIndex = cursor.getColumnIndex(Contacts.DISPLAY_NAME);
                String name = cursor.getString(columnIndex);
                // Do something with the selected contact's name...
            }
        }
    }

This example shows the basic logic you should use in your onActivityResult() method in order to handle an activity result. （上面的例子显示的是在onActivityResult()方法里处理结果的基本逻辑。）The first condition checks whether the request was successful（首先要确认请求是否成功）—if it was, then the resultCode will be RESULT_OK（如果成功的话，resultCode返回的值是RESULT_OK）—and whether the request to which this result is responding is known（还要确认请求的响应是否是已知的。）—in this case, the requestCode matches the second parameter sent with startActivityForResult(). （requestCode的值对应着startActivityForResult()的第二个参数。）From there, the code handles the activity result by querying the data returned in an Intent (the data parameter)（然后就可以处理结果了。主要是从intent里获取数据。）.

binkery：文档上写的，基本的逻辑是分3个步骤。

What happens is, a ContentResolver performs a query against a content provider, which returns a Cursor that allows the queried data to be read. For more information, see the Content Providers document.（接下来的是，通过content provider返回一个cursor来查询获取数据。）

For more information about using intents, see the Intents and Intent Filters document. 

Shutting Down an Activity You can shut down an activity by calling its finish() method. You can also shut down a separate activity that you previously started by calling finishActivity().(你可以使用activity的finish()方法来关闭它，也可以使用finshActivity()来关闭一个activity。)
Note: In most cases, you should not explicitly finish an activity using these methods. （在大多数情况下，你不需要这样明确的关闭activity。）As discussed in the following section about the activity lifecycle, （下面会讨论到activity的生命周期）the Android system manages the life of an activity for you,（Android系统帮你管理activity的生命周期） so you do not need to finish your own activities.（所以，你不需要关闭它们。） Calling these methods could adversely affect the expected user experience and should only be used when you absolutely do not want the user to return to this instance of the activity.（调用这些方法会不利于用户的体验，除非你非常确定不让用户回到这个activity。）