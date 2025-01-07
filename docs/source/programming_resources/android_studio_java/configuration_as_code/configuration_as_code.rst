Version controlling robot configuration
====================================
After you have created a robot configuration, you can put it in your code so 
that it can be version controlled.

Saving the Configuration Information Instructions
-------------------------------------------------
1. Go to the root of your Android Studio Project
2. cd TeamCode/src/main/res/xml
3. adb pull /sdcard/FIRST/<name of config>.xml
4. The next time you build your code, this will be installed as a read only config
5. To not have two with the same name, you can adb shell rm /sdcard/FIRST/<name of config>.xml