# note that you can change stable to unifi5 for v5
echo 'deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti' | sudo tee -a /etc/apt/sources.list.d/100-ubnt.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
sudo apt-get update
sudo apt-get install unifi -y
#
# Generate SSl Certificate
wget https://dl.eff.org/certbot-auto
chmod a+x certbot-auto
./certbot-auto
./certbot-auto certonly

# Load Certificate into Services
sudo openssl pkcs12 -export -inkey /etc/letsencrypt/live/unifi.jcvdesigns.com/privkey.pem -in /etc/letsencrypt/live/unifi.jcvdesigns.com/fullchain.pem -out /home/ubuntu/cert.p12 -name ubnt -password pass:temppass

#
sudo keytool -importkeystore -deststorepass aircontrolenterprise -destkeypass aircontrolenterprise -destkeystore /var/lib/unifi/keystore -srckeystore /home/ubuntu/cert.p12 -srcstoretype PKCS12 -srcstorepass temppass -alias ubnt -noprompt

# Restart Services
sudo rm /home/ubuntu/cert.p12
sudo /etc/init.d/unifi restart
