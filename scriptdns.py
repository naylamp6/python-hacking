# Este script devolverá consultas de IP, DNS, MAIL y, en su caso, IPv4 de un objetivo asignado.

#	1. Importando las dependencias necesarias
import dns
import dns.resolver
import dns.query
import dns.zone
import ipwhois
from ipwhois import IPWhois

#	2. Para introducir al inicio el dominio o IP a escanear
dominio=input("Por favor, introduce el dominio o ip a resolver: ")
ipaddr=input("Por favor, introduce la dirección IP para whois: ")

#	3. Resolviendo DNS
ip=(dns.resolver.query(dominio,"A"))
dns=(dns.resolver.query(dominio,"NS"))
#mail=(dns.resolver.query(dominio,"MX"))
#ipv6=(dns.resolver.query(dominio,"AAAA"))

#	4. Imprimiendo los resultados DNS
print ()
print ()
print ("DIRECCIÓN/ES IP (v4)")
print (ip.response.to_text())
print ()
print ()
print ("RESPUESTAS DNS")
print (dns.response.to_text())
#print (mail.response.to_text())
#print (ipv6.response.to_text())

#	5. Ejecutando whois e imprimiendolo
obj = IPWhois(ipaddr)
resultados = obj.lookup_rdap(depth=1)
print (resultados)
