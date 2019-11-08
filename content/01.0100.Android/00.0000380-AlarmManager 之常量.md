# AlarmManager 之常量
- Android,alarmmanager,常量,
- 2015-12-08 07:24:06

- *ELAPSED_REALTIME*  API level 1

以SystemClock.elapsedRealtime()(设备启动以来的时间，包括休眠的时间)的时间来设置闹钟。这个闹钟不会唤醒设备，如果闹钟在设备休眠的时候到达了，闹钟不会处罚，直到下一次设备唤醒的时候。
Constant Value: 3 (0x00000003)

 - *ELAPSED_REALTIME_WAKEUP* API level 1
 
以SystemClock.elapsedRealtime()的时间设置闹钟。这个闹钟触发的时候会唤醒设备。
Constant Value: 2 (0x00000002)

- *INTERVAL_DAY* API level 3

在Android API 19之前，setInexactRepeating(int,long,long,PendingIntent)可识别的，可用的不精确的复发的间隔。
Constant Value: 86400000 (0x0000000005265c00)常量值是一天

 - *INTERVAL_FIFTEEN_MINUTES* API level 3

 在Android API 19之前，setInexactRepeating(int,long,long,PendingIntent)可识别的，可用的不精确的复发的间隔。
Constant Value: 900000 (0x00000000000dbba0)常量值是十五分钟

 - *INTERVAL_HALF_DAY* API level 3

 在Android API 19之前，setInexactRepeating(int,long,long,PendingIntent)可识别的，可用的不精确的复发的间隔。
Constant Value: 43200000 (0x0000000002932e00)常量值是半天

 - *INTERVAL_HALF_HOUR* API level 3

 在Android API 19之前，setInexactRepeating(int,long,long,PendingIntent)可识别的，可用的不精确的复发的间隔。
Constant Value: 1800000 (0x00000000001b7740)常量值是半小时

 - *INTERVAL_HOUR* API level 3

 在Android API 19之前，setInexactRepeating(int,long,long,PendingIntent)可识别的，可用的不精确的复发的间隔。
Constant Value: 3600000 (0x000000000036ee80)常量值是一小时

 - *RTC* API level 1

 使用System.currentTimeMillis()的时间来设置闹钟。闹钟不会唤醒设备，如果设备正在休眠，闹钟不会被触发，直到下次设备被唤醒的时候。
Constant Value: 1 (0x00000001)

 - *RTC_WAKEUP* API level 1

 使用System.currentTimeMillis()的时间来设置闹钟，闹钟触发的时候会唤醒设备。
Constant Value: 0 (0x00000000)