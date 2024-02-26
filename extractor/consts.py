SUPPORTED_LANGS = ["ru", "en", "uk"]
# https://en.wikipedia.org/wiki/Email_address
RFC_5322_EMAIL_PATTERN = r'''([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|"([]!#-[^-~ \t]|(\\[\t -~]))+")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])\.(\w+)'''
EMAIL_PATTERN = r"\w+\S*\w+@[\w-]+\.[\w.-]+"
