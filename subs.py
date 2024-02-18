import requests
import tldextract

def check_takeover(url):
  """
  Bir web sitesinin alt domainlerini kontrol eder ve takeover olup olmadığını yazdırır.

  Parametreler:
    url: Kontrol edilecek web sitesinin URL'si.

  Dönüş Değeri:
    Yok.
  """

  # Ana domain ve alt domainleri ayır
  tld = tldextract.extract(url)
  domain = tld.domain + "." + tld.suffix
  subdomains = tld.subdomain.split(".")

  # Ana domainin IP adresini al
  try:
    main_domain_ip = requests.get(domain).headers['Host']
  except:
    print(f"Ana domain {domain} için IP adresi alınamadı.")
    return

  # Alt domainlerin IP adreslerini kontrol et
  for subdomain in subdomains:
    try:
      subdomain_ip = requests.get(f"{subdomain}.{domain}").headers['Host']
    except:
      print(f"Alt domain {subdomain}.{domain} için IP adresi alınamadı.")
      continue

    # IP adresleri farklıysa takeover olabilir
    if main_domain_ip != subdomain_ip:
      print(f"{subdomain}.{domain} muhtemelen takeover edilmiş!")

# Kullanıcıdan URL girmesini iste
url = input("Kontrol edilecek web sitesinin URL'sini girin: ")

# Takeover olup olmadığını kontrol et
check_takeover(url)
