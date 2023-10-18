import socket
import fcntl
import struct
import smtplib

def get_ip_address():
    ip_address = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

address = get_ip_address()
fromaddr = '<FROM_ADDRESS>'         #Enter from address here
toaddrs  = '<TO_ADDRESS>'           #Enter email to which the IP address needs to be sent
msg = "\r\n".join(["From:<FROM_ADDRESS>", "To:<TO_ADDRESS>", "Subject: IP Address from Raspberry Pi", "", "IP Address: ", address])
username = '<LOGIN_EMAIL>'          #Enter your login email here
password = '<APP_PASSWORD>'       #Enter your google generated app password here
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
