import ldap3
import config
import logging
import sys
from ldap3.utils.hashed import hashed
from ldap3 import * 


def connexion_ldaps_serveur():
    tls = Tls(local_private_key_file = config.PRIVATE_KEY, local_certificate_file = config.CERT, ca_certs_file = config.ROOT_CA)
    serveur = Server(config.LDAPS_SERVEUR, port = config.LDAPS_PORT, use_ssl = True, tls = tls)
   
    try:
        connected = Connection(serveur, user=Config.SVC_USER, password=config.SVC_PASSWORD)
        return connected
    
    except:
        logging.info(f'Error in connexion_ldpas_serveur: {connected.result}')


def change_passwords(user_name, new_password):
    connexion = connexion_ldaps_serveur()
    user_dn = f'uid={user_name},cn=users,cn=accounts,dc=rncp,dc=lab'
    connexion.bind()
    hashed_password = hashed(HASHED_SALTED_SHA, new_password)

    try:
        success = connexion.modify(user_dn, {'userPassword': [(MODIFY_REPLACE,[new_password])]})
        
        if success:
            print(f'{user_name} password changed with success')
            
    
    except(Exception,) as error:
        logging.error(f'Error in change_ad_passwords: {error}')


if __name__ == '__main__':
    connexion_ldaps_serveur()
    change_passwords(sys.argv[1], sys.argv[2])
