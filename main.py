import re
import expynent.patterns as expas


if re.match(expas.PHONE_NUMBER['US'], '1 (800) 233-2742'):
    print('match')
else:
    print('not match')
