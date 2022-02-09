import re

# email_re = re.compile(r"([^@]+)@([^@]+)\.([^@]+)") von Stefan, matcht aber gesamte Zeile (was mies ist wenn man keine \n mehr im Text hat)
email_re = re.compile(r"([\w\-]+)@([^@]+)\.([\w\-]+)")

at_re = re.compile(r'\s*@\s*')


def replace_mail_addresses(text):
  text = re.sub(email_re, r"\1 at \2 dot \3", text)
  return text


def replace_at_symbols(text):
  text = re.sub(at_re, ' at ', text)
  return text


def normalize_emails_and_at(text):
  text = replace_mail_addresses(text)
  text = replace_at_symbols(text)
  return text
