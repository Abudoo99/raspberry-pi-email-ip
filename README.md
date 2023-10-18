# Email from Raspberry Pi with its IP address
It is very annoying to connect your Raspberry Pi to your monitor everytime you want to ssh it to your PC. It eats up your time too!!
This python script sends the raspberry pi ip address to an email you have configured in the setup python script.

## Steps to set up your Raspberry Pi to send emails
  *  Create an app password in your google account to access your mail to send the IP address
  *  Replace the app password generated in the python script in this repository
  *  Also replace the from and to email IDs to the ones you have. The app password must be set in the 'From' email

## Steps to find your device IP address
The python script will fetch the IP address from the device and pass it onto the email message content. To verify if it is correct, you can type the following command in your terminal to get your device IP address.
```
ifconfig
```

## Steps to get email immediately after you boot the Raspberry pi
* In order to send email on boot, we need to set up a cron tab (command that runs on regular intervals). It can be done using the following command
```
sudo crontab -e
```
* Enter the following commands in the crontab file
```
reboot sleep 60 && while ! ping -c1 google.com > /dev/null;
do sleep 15;
done && python <path where your script is located>
```
