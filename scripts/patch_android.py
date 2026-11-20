import re
p='android/app/src/main/AndroidManifest.xml'
s=open(p,encoding='utf-8').read()
perms=['android.permission.CAMERA','android.permission.ACCESS_FINE_LOCATION','android.permission.ACCESS_COARSE_LOCATION','android.permission.INTERNET','android.permission.WAKE_LOCK']
add=''
for q in perms:
    if q not in s: add+='    <uses-permission android:name="%s" />\n'%q
add+='    <uses-feature android:name="android.hardware.camera" android:required="false" />\n'
s=s.replace('</manifest>',add+'</manifest>')
if 'screenOrientation' not in s:
    s=s.replace('android:name=".MainActivity"','android:name=".MainActivity"\n            android:screenOrientation="sensorLandscape"',1)
open(p,'w',encoding='utf-8').write(s)
print(s)
